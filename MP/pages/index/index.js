//index.js
//获取应用实例
const app = getApp()

Page({
  data: {
    motto: 'Hello World',
    brief_info_bg: '***brief_info_bg Path***',
    detail_info_bg: '***detail_info_bg Path***',
    br: '\n',
    userInfo: {},
    hasUserInfo: false,
    canIUse: wx.canIUse('button.open-type.getUserInfo'),
    brief_content: '预留信息',
    detail_list: [
      '预留信息'
    ],
    tips_list: []
  },
    //事件处理函数
  bindViewTap: function() {
    wx.navigateTo({
      url: '../logs/logs'
    })
  },
  onLoad: function () {
    // 数据获取
    var that = this
    wx.request({
        url: 'https://***API Domain***/dx/detail',
        success: function (res) {
            console.log(res.data['detail'])
            that.setData({
                detail_list: res.data['detail']
            })
        }
    })
    wx.request({
      url: 'https://***API Domain***/dx/brief',
      success: function (res) {
        console.log(res.data)
        that.setData({
          brief_content: res.data
        })
      }
    })
    wx.request({
      url: 'https://***API Domain***/dx/tips',
      success: function (res) {
        console.log(res.data)
        that.setData({
          tips_list: res.data['tips']
        })
      }
    })
    if (app.globalData.userInfo) {
      this.setData({
        userInfo: app.globalData.userInfo,
        hasUserInfo: true
      })
    } else if (this.data.canIUse){
      // 由于 getUserInfo 是网络请求，可能会在 Page.onLoad 之后才返回
      // 所以此处加入 callback 以防止这种情况
      app.userInfoReadyCallback = res => {
        this.setData({
          userInfo: res.userInfo,
          hasUserInfo: true
        })
      }
    } else {
      // 在没有 open-type=getUserInfo 版本的兼容处理
      wx.getUserInfo({
        success: res => {
          app.globalData.userInfo = res.userInfo
          this.setData({
            userInfo: res.userInfo,
            hasUserInfo: true
          })
        }
      })
    }
  },
  onPullDownRefresh: function () {
    wx.stopPullDownRefresh()
    var that = this;
    this.onLoad();
  },
  getUserInfo: function(e) {
    console.log(e)
    app.globalData.userInfo = e.detail.userInfo
    this.setData({
      userInfo: e.detail.userInfo,
      hasUserInfo: true
    })
  }
})
