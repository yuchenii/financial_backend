/*!
 *  build: vue-admin-better 
 *  vue-admin-beautiful.com 
 *  https://gitee.com/chu1204505056/vue-admin-better 
 *  time: 2022-6-29 14:31:04
 */
(window["webpackJsonp"]=window["webpackJsonp"]||[]).push([["chunk-32ceed26"],{"0b1d":function(t,e,a){},"802d":function(t,e,a){"use strict";a.r(e),a.d(e,"getUserInfo",(function(){return r})),a.d(e,"getUserBankCardInfo",(function(){return n})),a.d(e,"getUserAssetInfo",(function(){return o}));var l=a("b775");function r(t){var e="/user?user_id="+t;return-1===t&&(e="/user"),Object(l["default"])({url:e,method:"get"})}function n(t){var e="/user/bank_card?user_id="+t;return-1===t&&(e="/user/bank_card"),Object(l["default"])({url:e,method:"get"})}function o(t){var e="/user/asset?user_id="+t;return-1===t&&(e="/user/asset"),Object(l["default"])({url:e,method:"get"})}},c5ce:function(t,e,a){"use strict";a.r(e);var l=function(){var t=this,e=t.$createElement,a=t._self._c||e;return a("div",{staticClass:"asset-info-container"},[a("el-form",{attrs:{inline:!0,align:"right"},nativeOn:{submit:function(t){t.preventDefault()}}},[a("el-form-item",[a("el-input",{attrs:{placeholder:"请输入用户ID",clearable:""},model:{value:t.userId,callback:function(e){t.userId="string"===typeof e?e.trim():e},expression:"userId"}})],1),a("el-form-item",[a("el-button",{attrs:{icon:"el-icon-search",type:"primary","native-type":"submit"},on:{click:t.queryData}},[t._v(" 查询 ")])],1)],1),a("el-tabs",{attrs:{type:"border-card"}},[a("el-tab-pane",{attrs:{label:"基金"}},[a("el-table",{staticStyle:{width:"100%"},attrs:{data:t.fundInfo}},[a("el-table-column",{attrs:{type:"expand"},scopedSlots:t._u([{key:"default",fn:function(e){return[a("el-form",{staticClass:"demo-table-expand",attrs:{"label-position":"left",inline:""}},[a("el-form-item",{attrs:{label:"资产ID"}},[a("span",[t._v(t._s(e.row.a_id))])]),a("el-form-item",{attrs:{label:"基金ID"}},[a("span",[t._v(t._s(e.row.a_product_info.f_id))])]),a("el-form-item",{attrs:{label:"基金名称"}},[a("span",[t._v(t._s(e.row.a_product_info.f_name))])]),a("el-form-item",{attrs:{label:"风险等级"}},[a("span",[t._v(t._s(e.row.a_product_info.f_risk_level))])]),a("el-form-item",{attrs:{label:"基金管理员"}},[a("span",[t._v(t._s(e.row.a_product_info.f_administrator))])]),a("el-form-item",{attrs:{label:"基金金额"}},[a("span",[t._v(t._s(Number(e.row.a_product_info.f_amount)))])]),a("el-form-item",{attrs:{label:"资产状态"}},[a("span",[t._v(t._s(t.assetState(e.row.a_state)))])]),a("el-form-item",{attrs:{label:"购买数量"}},[a("span",[t._v(t._s(e.row.a_number))])]),a("el-form-item",{attrs:{label:"购买时间"}},[a("span",[t._v(t._s(e.row.a_time))])]),a("el-form-item",{attrs:{label:"持有收益"}},[a("span",[t._v(t._s(Number(e.row.a_profit)))])])],1)]}}])}),a("el-table-column",{attrs:{label:"基金编码",prop:"a_product_info.f_code"}}),a("el-table-column",{attrs:{label:"基金名称",prop:"a_product_info.f_name"}}),a("el-table-column",{attrs:{label:"购买数量",prop:"a_number"}}),a("el-table-column",{attrs:{label:"持有收益"},scopedSlots:t._u([{key:"default",fn:function(e){return[a("span",[t._v(t._s(Number(e.row.a_profit)))])]}}])}),a("el-table-column",{attrs:{label:"购买时间",prop:"a_time",width:"150%"}}),a("el-table-column",{attrs:{label:"资产状态"},scopedSlots:t._u([{key:"default",fn:function(e){return[a("el-tag",{attrs:{type:e.row.a_state?"success":"danger",effect:"plain"}},[t._v(" "+t._s(t.assetState(e.row.a_state))+" ")])]}}])}),a("el-table-column",{attrs:{"show-overflow-tooltip":"",label:"操作",width:"200"},scopedSlots:t._u([{key:"default",fn:function(e){var l=e.row;return[a("el-button",{on:{click:function(e){return t.handleEdit(l)}}},[t._v("编辑")]),a("el-button",{attrs:{type:"danger"},on:{click:function(e){return t.handleDelete(l)}}},[t._v(" 删除 ")])]}}])})],1)],1),a("el-tab-pane",{attrs:{label:"保险"}},[a("el-table",{staticStyle:{width:"100%"},attrs:{data:t.insuranceInfo}},[a("el-table-column",{attrs:{type:"expand"},scopedSlots:t._u([{key:"default",fn:function(e){return[a("el-form",{staticClass:"demo-table-expand",attrs:{"label-position":"left",inline:""}},[a("el-form-item",{attrs:{label:"资产ID"}},[a("span",[t._v(t._s(e.row.a_id))])]),a("el-form-item",{attrs:{label:"保险ID"}},[a("span",[t._v(t._s(e.row.a_product_info.i_id))])]),a("el-form-item",{attrs:{label:"保险名称"}},[a("span",[t._v(t._s(e.row.a_product_info.i_name))])]),a("el-form-item",{attrs:{label:"适用人群"}},[a("span",[t._v(t._s(e.row.a_product_info.i_people))])]),a("el-form-item",{attrs:{label:"保险年限"}},[a("span",[t._v(t._s(e.row.a_product_info.i_time))])]),a("el-form-item",{attrs:{label:"保险项目"}},[a("span",[t._v(t._s(e.row.a_product_info.i_item))])]),a("el-form-item",{attrs:{label:"保险金额"}},[a("span",[t._v(t._s(Number(e.row.a_product_info.i_amount)))])]),a("el-form-item",{attrs:{label:"资产状态"}},[a("span",[t._v(t._s(t.assetState(e.row.a_state)))])]),a("el-form-item",{attrs:{label:"购买数量"}},[a("span",[t._v(t._s(e.row.a_number))])]),a("el-form-item",{attrs:{label:"购买时间"}},[a("span",[t._v(t._s(e.row.a_time))])]),a("el-form-item",{attrs:{label:"持有收益"}},[a("span",[t._v(t._s(Number(e.row.a_profit)))])])],1)]}}])}),a("el-table-column",{attrs:{label:"保险编码",prop:"a_product_info.i_code"}}),a("el-table-column",{attrs:{label:"保险名称",prop:"a_product_info.i_name"}}),a("el-table-column",{attrs:{label:"购买数量",prop:"a_number"}}),a("el-table-column",{attrs:{label:"持有收益"},scopedSlots:t._u([{key:"default",fn:function(e){return[a("span",[t._v(t._s(Number(e.row.a_profit)))])]}}])}),a("el-table-column",{attrs:{label:"购买时间",prop:"a_time",width:"150%"}}),a("el-table-column",{attrs:{label:"资产状态"},scopedSlots:t._u([{key:"default",fn:function(e){return[a("el-tag",{attrs:{type:e.row.a_state?"success":"danger",effect:"plain"}},[t._v(" "+t._s(t.assetState(e.row.a_state))+" ")])]}}])}),a("el-table-column",{attrs:{"show-overflow-tooltip":"",label:"操作",width:"200"},scopedSlots:t._u([{key:"default",fn:function(e){var l=e.row;return[a("el-button",{on:{click:function(e){return t.handleEdit(l)}}},[t._v("编辑")]),a("el-button",{attrs:{type:"danger"},on:{click:function(e){return t.handleDelete(l)}}},[t._v(" 删除 ")])]}}])})],1)],1),a("el-tab-pane",{attrs:{label:"理财产品"}},[a("el-table",{staticStyle:{width:"100%"},attrs:{data:t.financialInfo}},[a("el-table-column",{attrs:{type:"expand"},scopedSlots:t._u([{key:"default",fn:function(e){return[a("el-form",{staticClass:"demo-table-expand",attrs:{"label-position":"left",inline:""}},[a("el-form-item",{attrs:{label:"资产ID"}},[a("span",[t._v(t._s(e.row.a_id))])]),a("el-form-item",{attrs:{label:"产品ID"}},[a("span",[t._v(t._s(e.row.a_product_info.fp_id))])]),a("el-form-item",{attrs:{label:"产品名称"}},[a("span",[t._v(t._s(e.row.a_product_info.fp_name))])]),a("el-form-item",{attrs:{label:"产品详情"}},[a("span",[t._v(t._s(e.row.a_product_info.fp_detail))])]),a("el-form-item",{attrs:{label:"理财年限"}},[a("span",[t._v(t._s(e.row.a_product_info.fp_time))])]),a("el-form-item",{attrs:{label:"产品金额"}},[a("span",[t._v(t._s(Number(e.row.a_product_info.fp_amount)))])]),a("el-form-item",{attrs:{label:"资产状态"}},[a("span",[t._v(t._s(t.assetState(e.row.a_state)))])]),a("el-form-item",{attrs:{label:"购买数量"}},[a("span",[t._v(t._s(e.row.a_number))])]),a("el-form-item",{attrs:{label:"购买时间"}},[a("span",[t._v(t._s(e.row.a_time))])]),a("el-form-item",{attrs:{label:"持有收益"}},[a("span",[t._v(t._s(Number(e.row.a_profit)))])])],1)]}}])}),a("el-table-column",{attrs:{label:"产品编码",prop:"a_product_info.fp_code"}}),a("el-table-column",{attrs:{label:"产品名称",prop:"a_product_info.fp_name"}}),a("el-table-column",{attrs:{label:"购买数量",prop:"a_number"}}),a("el-table-column",{attrs:{label:"持有收益"},scopedSlots:t._u([{key:"default",fn:function(e){return[a("span",[t._v(t._s(Number(e.row.a_profit)))])]}}])}),a("el-table-column",{attrs:{label:"购买时间",prop:"a_time",width:"150%"}}),a("el-table-column",{attrs:{label:"资产状态"},scopedSlots:t._u([{key:"default",fn:function(e){return[a("el-tag",{attrs:{type:e.row.a_state?"success":"danger",effect:"plain"}},[t._v(" "+t._s(t.assetState(e.row.a_state))+" ")])]}}])}),a("el-table-column",{attrs:{"show-overflow-tooltip":"",label:"操作",width:"200"},scopedSlots:t._u([{key:"default",fn:function(e){var l=e.row;return[a("el-button",{on:{click:function(e){return t.handleEdit(l)}}},[t._v("编辑")]),a("el-button",{attrs:{type:"danger"},on:{click:function(e){return t.handleDelete(l)}}},[t._v(" 删除 ")])]}}])})],1)],1)],1)],1)},r=[],n=a("802d"),o={name:"UserAssetInfo",data:function(){return{userId:1,fundInfo:[],insuranceInfo:[],financialInfo:[],assetInfo:{},search:""}},computed:{assetState:function(){return function(t){switch(t){case 1:return"正常";case 0:return"已冻结";default:return"未知"}}}},mounted:function(){this.fetchUserAssetInfo()},methods:{queryData:function(){this.fetchUserAssetInfo()},fetchUserAssetInfo:function(){var t=this;Object(n["getUserAssetInfo"])(this.userId).then((function(e){console.log(e),t.assetInfo=e.data,t.putData(e.data.asset_list)}))},putData:function(t){for(var e in this.financialInfo=[],this.fundInfo=[],this.insuranceInfo=[],t)0==t[e].a_product_type?this.financialInfo.push(t[e]):1==t[e].a_product_type?this.insuranceInfo.push(t[e]):2==t[e].a_product_type&&this.fundInfo.push(t[e])},handleEdit:function(t,e){console.log(t,e),this.$baseMessage("正在开发中","warning")},handleDelete:function(t,e){this.$baseMessage("正在开发中","warning"),console.log(t,e)}}},s=o,i=(a("dfa7"),a("2877")),u=Object(i["a"])(s,l,r,!1,null,"3e2ea496",null);e["default"]=u.exports},dfa7:function(t,e,a){"use strict";a("0b1d")}}]);