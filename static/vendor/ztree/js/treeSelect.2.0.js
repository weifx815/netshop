;(function ($) {
    let defaults = {
        zNodes: [],
        async: {
            enable: false,
            url: "",
            autoParam: ["id"]
        },
        data: {
            key: {
                name: "name",
                isParent: "isParent"
            },
            simpleData: {
                enable: true,
                idKey: "id",
                pIdKey: "pId",
                rootPId: 0
            }
        },
        callback: {
            onCheck: function (treeSelectObj,treeNode) {
            }
        },
        checks: [],
        blur: function () {
        },
        chkStyle: "checkbox",
        radioType: "all",
        height: 'auto',
        direction: "auto",
        filter: true,
        slideModel: 'click',
        searchShowParent: false,
        textModel: 'detail',/*simple*/
        searchPlaceholder: 'search',
        searchKeys: null,
        containerClass: "",
        chkboxType: {"Y": "ps", "N": "ps"},
        beforeSearchPromise: function (defer, treeSelectObj, keyWord) {
            /*妯℃嫙寮傛鍔犺浇*/
            defer.resolve();
        },
        renderText: undefined
    };
    let TreeSelect = function (el, options) {
        this.$el = $(el);
        var _this = this;
        if (!Function.prototype.bind) {
            Function.prototype.bind = function (obj) {
                var _self = this
                    , args = arguments;
                return function () {
                    _self.apply(obj, Array.prototype.slice.call(args, 1));
                }
            }
        }
        let $options = function () {
            return $.extend({}, defaults, options, _this.$el.data());//鍚堝苟涓氬姟鏁版嵁
        };
        /*閬垮厤鍏辩敤鍚屼竴涓厤缃椂涓よ竟骞叉壈*/
        this.options = this.cloneObj(new $options());
        this.init();
    };
    TreeSelect.prototype = {
        constructor: TreeSelect,
        init: function () {
            let elChecks = this.$el.attr("checks");
            if (!this.options.checks) {
                this.options.checks = [];
            }
            if (elChecks != "" && elChecks != undefined && elChecks != null) {
                this.options.checks = $.merge(this.options.checks, elChecks.split(','));
            }
            this.render();
            this.initTree();
            this.bindEvent();
        },
        getCheckedObject: function () {
            return this.$zTreeObj.getCheckedNodes(true);
        },
        val: function (ids) {
            let nodes = this.$zTreeObj.getCheckedNodes(true);
            let _this = this;

            if (ids == undefined) {
                ids = [];
                $(nodes).each(function (index, node) {
                    ids.push(node[_this.options.data.simpleData.idKey]);
                });
                return ids;
            } else {
                /*璧嬪€�*/
                this.options.checks = ids;
                $(nodes).each(function (index, node) {
                    node.checked = false;
                    _this.$zTreeObj.updateNode(node);
                });
                $(ids).each(function (index, id) {
                    let node = _this.$zTreeObj.getNodeByParam("id", id);
                    node.checked = true;
                    _this.$zTreeObj.updateNode(node);
                });
                _this.m2v();
                return this;
            }

        },
        text: function () {
            let nodes = this.$zTreeObj.getCheckedNodes(true);
            let texts = [];
            let _this = this;
            $(nodes).each(function (index, node) {
                let names = [node[_this.options.data.key.name]];
                _this.getNodeName(node, names);
                texts.push(names.join("/"));
            });
            return texts;
        },
        bindEvent: function () {
            if (this.options.slideModel == 'click') {
                this.bindDrawerEventClick();
            } else {
                this.bindDrawerEventSlide();
            }
            if (this.options.filter) {
                this.bindSearch();
            }
        },
        bindSearch: function () {
            this.searchTime = null;
            let _this = this;
            this.clearbtn.click(function () {
                _this.searchInput.val('');
                _this.search_tree_el.hide();
                _this.tree_el.show();
                if (_this.$searchZTreeObj) {
                    _this.$searchZTreeObj.destroy();
                }
                _this.clearbtn.hide();
            });
            this.searchInput.keyup(function (event) {
                let keyWord = $(this).val().trim();
                if (keyWord === "") {
                    _this.clearbtn.hide();
                } else {
                    _this.clearbtn.show();
                }
                if (event.keyCode !== 13) {
                    return false;
                }
                if (_this.options.beforeSearchPromise) {
                    _this.doBeforeSearchPromise(keyWord).then(function () {
                        _this.doSearch(keyWord);
                    });
                } else {
                    _this.doSearch(keyWord);
                }
            });
        },
        doBeforeSearchPromise: function (keyWord) {
            let _this = this;
            return $.Deferred(function (defer) {
                /*杩涜ajax璇锋眰骞朵笖鍔犺浇瀹屾垚鏁版嵁鍚庢寜鐓т笅闈㈡柟寮忚繘琛岃皟鐢ㄥ嵆鍙Е鍙戞悳绱�*/
                _this.options.beforeSearchPromise(defer, _this, keyWord);
            }).promise();
        },
        doSearch: function (keyWord) {
            let _this = this;
            /*寮傛鎵ц浣庨鐜囨墽琛岃В鍐虫€ц兘闂*/
            if (_this.searchTime) {
                clearTimeout(_this.searchTime);
            }
            _this.searchTime = setTimeout(function () {
                if (keyWord === "") {
                    _this.search_tree_el.hide();
                    _this.tree_el.show();
                    if (_this.$searchZTreeObj) {
                        _this.$searchZTreeObj.destroy();
                    }
                    return;
                }
                _this.search_tree_el.show();
                _this.tree_el.hide();

                let nodeList = _this.$zTreeObj.getNodesByFilter(function (node) {
                    return _this.ifHit(node, keyWord);
                });//閫氳繃鍏抽敭瀛楁ā绯婃悳绱�
                /* let nodeList = _this.$zTreeObj.getNodesByParamFuzzy(_this.options.data.key.name, keyWord, null);*/
                let datasMap = {};
                $(nodeList).each(function (index, item) {
                    datasMap[item[_this.options.data.simpleData.idKey]] = item;
                });

                if (_this.options.searchShowParent) {
                    $(nodeList).each(function (index, node) {
                        _this.loadParents(node, datasMap);
                    })
                }
                _this.initSearchTree(Object.values(datasMap), keyWord);
            }, 500);

        },
        ifHit: function (node, keyWord) {
            let _this = this;
            if (_this.options.searchKeys instanceof Array && _this.options.searchKeys.length > 0) {
                let flag = false;
                $(_this.options.searchKeys).each(function (index, item) {
                    if (item.startsWith("like_")) {
                        if (node[item.replace("like_", "")].indexOf(keyWord) != -1) {
                            flag = true;
                            return;
                        }
                    } else if (item.startsWith("eq_")) {
                        if (node[item.replace("eq_", "")] === keyWord) {
                            flag = true;
                            return;
                        }
                    }

                });
                return flag;
            } else {
                return node[_this.options.data.key.name].indexOf(keyWord) != -1;
            }
        },
        loadParents: function (node, datasMap) {
            let parent = node.getParentNode();
            if (parent) {
                let copyparent = $.extend({}, parent);
                copyparent.children = null;
                copyparent.open = true;
                datasMap[parent[this.options.data.simpleData.idKey]] = copyparent;
                this.loadParents(parent, datasMap);
            } else {
                return;
            }
        },
        randomID: function (randomLength) {
            return Number(Math.random().toString().substr(3, randomLength) + new Date().getTime()).toString(36)
        },
        ifSlideUp: function () {
            let _this = this;
            if (_this.options.direction == 'auto') {
                /*鍏冪礌楂樺害*/
                let elH = _this.$el.height();
                /*鍏冪礌璺濈椤堕儴楂樺害*/
                let el2top = _this.$el.offset().top;
                /*涓嬫媺妗嗛珮搴�*/
                let drowdownHeight = _this.dropdown_container.height();

                /*婊氬姩鏉′綅缃�*/
                let scrollTop = $(document).scrollTop();
                /*涓嬫媺妗嗗簳閮ㄨ窛绂荤獥鍙ｅ簳閮ㄧ殑璺濈*/
                let height2top = el2top - scrollTop;
                /*绐楀彛楂樺害*/
                let wh = window.innerHeight;
                let height2bottom = wh - el2top - elH;

                if (height2bottom >= drowdownHeight) {
                    return false;
                }
                if (height2top > height2bottom) {
                    return true;
                } else {
                    return false;
                }
            } else if (_this.options.direction != 'up') {
                return false;
            } else {
                return true;
            }

        },
        bindDrawerEventSlide: function () {
            let dropdown_container = this.dropdown_container;
            /*璁＄畻鎶藉眽鏂瑰悜*/
            let _this = this;
            this.$el.click(function (event) {
                if (_this.ifSlideUp()) {
                    dropdown_container.addClass("up")
                    dropdown_container.css("bottom", _this.$el.outerHeight());
                    dropdown_container.css("top", '');
                } else {
                    dropdown_container.css("bottom", '');
                    dropdown_container.css("top", _this.$el.outerHeight());
                }
                event.stopPropagation();
                if (!dropdown_container.is(':visible')) {
                    dropdown_container.slideDown("fast");
                } else {
                    dropdown_container.animate({height: 'toggle', opacity: 'toggle'}, "fast");
                }
            });
            this.container.mouseleave(function () {
                if (dropdown_container.is(':visible')) {
                    dropdown_container.animate({height: 'toggle', opacity: 'toggle'}, "fast");
                }
            });

        },
        bindDrawerEventClick: function () {
            let dropdown_container = this.dropdown_container;
            /*璁＄畻鎶藉眽鏂瑰悜*/
            let _this = this;
            let onBodyMusedown = function (event) {
                if (!$(event.target).parents("#" + _this.id).length > 0) {
                    dropdown_container.fadeOut("fast");
                    $("body").unbind("mousedown", onBodyMusedown);
                }
            };
            this.$el.click(function () {
                if (_this.ifSlideUp()) {
                    dropdown_container.addClass("up")
                    dropdown_container.css("bottom", _this.$el.outerHeight());
                    dropdown_container.css("top", '');
                } else {
                    dropdown_container.css("bottom", '');
                    dropdown_container.css("top", _this.$el.outerHeight());
                }
                if (!dropdown_container.is(':visible')) {
                    dropdown_container.slideDown("fast");
                    _this.searchInput.focus();
                    $("body").bind("mousedown", onBodyMusedown);
                } else {
                    dropdown_container.fadeOut("fast");
                    $("body").unbind("mousedown", onBodyMusedown);
                }

            });
        },
        render: function () {
            this.$el.css({display: 'block'});
            this.container = this.$el.wrap('<div class="mts-container ' + this.options.containerClass + '"/>').parent();
            this.searchInput = $('<input class="searchInput" placeholder=' + this.options.searchPlaceholder + ' type="text" style="width: ' + (this.$el.outerWidth() - 20) + 'px;">');
            this.clearbtn = $('<span href="javascript:void(0);" class="clearbtn">x</span>')
            let height = this.options.height + (this.options.height == "auto" ? "" : "px");
            this.tree_el = $('<ul class="ztree" style="height:' + height + '; width:' + (this.$el.outerWidth() - 2) + 'px;"></ul>');
            this.search_tree_el = $('<ul class="ztree" style="height:' + height + '; width:' + (this.$el.outerWidth() - 2) + 'px;"></ul>');

            this.dropdown_container = $('<div  class="dropdown_container"  ></div>');
            if (this.options.filter) {
                this.dropdown_container.append(this.searchInput);
                this.dropdown_container.append(this.clearbtn);
            }
            this.dropdown_container.append(this.tree_el);
            this.dropdown_container.append(this.search_tree_el.hide());
            this.container.append(this.dropdown_container);
            this.id = this.randomID(3);
            this.dropdown_container.attr("id", this.id);
            this.tree_el.attr("id", this.randomID(3));
            this.search_tree_el.attr("id", this.randomID(3));
            return this.container;
        },
        initDefaultCheckedStatus: function (nodes) {
            let _this = this;
            let needUpdateNodes = [];
            if (this.options.checks && this.options.checks.length > 0) {
                $(nodes).each(function (index, node) {
                    let checkFlag = false;
                    $(_this.options.checks).each(function (i, id) {
                        if (id == node[_this.options.data.simpleData.idKey]) {
                            checkFlag = true;
                            if (node.checked != true) {
                                node.checked = true;
                                needUpdateNodes.push(node);
                            }
                            return false;
                        }
                    });
                    if (!checkFlag) {
                        if (node.checked != false) {
                            node.checked = false;
                            needUpdateNodes.push(node)
                        }
                    }
                });
            }
            return needUpdateNodes;
        },
        initTree: function () {
            let _this = this;
            let setting = {
                check: {
                    enable: true,
                    chkboxType: this.options.chkboxType,
                    chkStyle: this.options.chkStyle,
                    radioType: this.options.radioType
                },
                view: {
                    dblClickExpand: false,
                    showIcon: false
                },
                data: _this.options.data,
                callback: {
                    onCheck: _this.onCheck.bind(_this),
                    onAsyncSuccess: _this.onAsyncSuccess.bind(_this),
                    beforeAsync: function (treeId, treeNode) {
                        if (treeNode && treeNode.__notAsync__) {
                            return false;
                        }
                        return true;
                    },
                    onClick: function (e, treeId, treeNode, clickFlag) {
                        _this.$zTreeObj.checkNode(treeNode, !treeNode.checked, true);
                        _this.onCheck(e, treeId, treeNode);
                    }
                },
                async: this.options.async
            };
            /*寮傛瀹屾垚鍚庤缃垵濮嬮€変腑鐨勫€�*/
            setting.async.dataFilter = function (treeId, parentNode, responseData) {
                if (responseData) {
                    _this.initDefaultCheckedStatus(responseData);
                }
                return responseData;
            };
            _this.initDefaultCheckedStatus(this.options.zNodes);
            this.$zTreeObj = $.fn.zTree.init(this.tree_el, setting, this.options.zNodes);
            this.onCheck(null, _this);
            return this;
        },
        initSearchTree: function (data, param) {
            let _this = this;
            let async = this.options.async;
            if (data.length == 0) {
                async = {
                    enable: false,
                    url: "",
                    autoParam: ["id"]
                }
            }
            let setting = {
                check: {
                    enable: true,
                    chkboxType: this.options.chkboxType,
                    chkStyle: this.options.chkStyle,
                    radioType: this.options.radioType
                },
                view: {
                    dblClickExpand: false,
                    showIcon: false,
                    fontCss: function (treeId, treeNode) {
                        if (_this.ifHit(treeNode, param)) {
                            return {color: "#FFA200", "font-weight": "bold"};
                        }
                        return {}
                    }
                },
                async: async,
                /* 绠€鍗曟爲缁撴瀯浼氬鑷撮粯璁hildren涓簁ey锛屼粠涓绘爲涓婂彇寰楃殑鏁版嵁甯hildren灞炴€�;浼氬鑷村瓙鑺傜偣閲嶅 */
                data: $.extend({}, _this.options.data, {
                    data: {
                        key: {
                            children: "__nodes__"
                        }
                    }
                }),
                callback: {
                    onCheck: function (e, treeId, treeNode) {
                        let node = _this.$zTreeObj.getNodeByParam(_this.options.data.simpleData.idKey, treeNode[_this.options.data.simpleData.idKey]);
                        _this.$zTreeObj.checkNode(node, treeNode.checked, true);
                        _this.onCheck(e, treeId, treeNode);
                    },
                    onClick: function (e, treeId, treeNode, clickFlag) {
                        _this.$searchZTreeObj.checkNode(treeNode, !treeNode.checked, true);
                        _this.$searchZTreeObj.setting.callback.onCheck(e, treeId, treeNode);
                    },
                    onAsyncSuccess: function (event, treeId, treeNode, msg) {
                        /*鎼滅储鏍戣妭鐐瑰睍寮€鐨勫悓鏃讹紝鍔犺浇涓绘爲鍝嶅簲鏁版嵁*/
                        if (treeNode) {
                            let node = _this.$zTreeObj.getNodeByParam(_this.options.data.simpleData.idKey, treeNode[_this.options.data.simpleData.idKey]);
                            node.__notAsync__ = true;
                            _this.$zTreeObj.addNodes(node, 0, treeNode.children);
                        }
                    }
                }
            };
            this.$searchZTreeObj = $.fn.zTree.init(this.search_tree_el, setting, data);
        },
        onCheck: function (e, treeId, treeNode) {
            this.m2v();
            this.options.callback.onCheck(this, treeNode);
        },
        m2v: function () {
            let nodes = this.$zTreeObj.getCheckedNodes(true);
            let text = "";
            let checks = "";
            if (this.options.renderText) {
                text = this.options.renderText(nodes);
                for (let i = 0, l = nodes.length; i < l; i++) {
                    checks += nodes[i][this.options.data.simpleData.idKey] + ",";
                }
            } else {
                for (let i = 0, l = nodes.length; i < l; i++) {
                    let texts = [nodes[i][this.options.data.key.name]];
                    this.getNodeName(nodes[i], texts);
                    text += texts.join("/") + ",";
                    checks += nodes[i][this.options.data.simpleData.idKey] + ",";
                }
                if (text.length > 0) {
                    text = text.substring(0, text.length - 1);
                }
            }
            if (checks.length > 0) {
                checks = checks.substring(0, checks.length - 1);
            }
            this.$el.attr("checks", checks);
            this.$el.val(text);
            this.$el.attr("title", "缂栫爜:" + checks + ";鍚嶇О:" + text);
        },
        getNodeName: function (node, texts) {
            if (this.options.textModel == 'simple') {
                return texts;
            }
            let parent = node.getParentNode();
            if (parent) {
                texts.unshift(parent[this.options.data.key.name]);
                return this.getNodeName(parent, texts);
            } else {
                return texts;
            }
        },
        onAsyncSuccess: function (event, treeId, treeNode, msg) {
            this.m2v();
            this.tree_el.find("a").mouseleave(function () {
                event.stopPropagation();
            });
            this.tree_el.find("span").mouseleave(function () {
                event.stopPropagation();
            });
        },
        cloneObj: function (obj) {
            let newObj = {};
            if (obj instanceof Array) {
                newObj = [];
            }
            for (let key in obj) {
                let val = obj[key];
                newObj[key] = typeof val === 'object' ? this.cloneObj(val) : val;
            }
            return newObj;
        },
        destory: function () {
            if (this.container) {
                this.$el.removeData('treeSelect');
                this.$el.val('');
                this.$el.attr("checks", "")
                this.$el.attr("title", "")
                this.container.replaceWith(this.$el);
                this.container = null;
                this.$zTreeObj.destroy();
                if (this.$searchZTreeObj) {
                    this.$searchZTreeObj.destroy();
                }

            }
        }
    };
    $.fn.treeSelect = function (options) {
        let resultArr = [];
        this.each(function () {
            let $this = $(this);
            let treeSelectObj = $this.data('treeSelect');
            if (!treeSelectObj) {
                treeSelectObj = new TreeSelect(this, options);
                $.data(this, 'treeSelect', treeSelectObj);
            }
            resultArr.push(treeSelectObj);
        });
        return resultArr.length == 1 ? resultArr[0] : resultArr;
    };
})(jQuery);