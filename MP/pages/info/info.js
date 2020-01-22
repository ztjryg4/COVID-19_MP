// pages/info/info.js
Page({

  /**
   * 页面的初始数据
   */
  data: {
    info_list_bak: [
      {
        "title": "信息一",
        "content": "内容一"
      },
      {
        "title": "信息二",
        "content": "内容二"
      }
    ],
    info_list: []
  },

  /**
   * 生命周期函数--监听页面加载
   */
  onLoad: function (options) {
    // 数据获取
    var that = this
        wx.request({
      url: 'https://dxapi.imztj.cn/dx/info',
      success: function (res) {
        console.log(res.data['news'])
        that.setData({
          info_list: res.data['news']
        })
      }
    })
  },

  /**
   * 生命周期函数--监听页面初次渲染完成
   */
  onReady: function () {

  },

  /**
   * 生命周期函数--监听页面显示
   */
  onShow: function () {

  },

  /**
   * 生命周期函数--监听页面隐藏
   */
  onHide: function () {

  },

  /**
   * 生命周期函数--监听页面卸载
   */
  onUnload: function () {

  },

  /**
   * 页面相关事件处理函数--监听用户下拉动作
   */
  onPullDownRefresh: function () {
    wx.stopPullDownRefresh()
    var that = this;
    this.onLoad();
  },

  /**
   * 页面上拉触底事件的处理函数
   */
  onReachBottom: function () {

  },

  /**
   * 用户点击右上角分享
   */
  onShareAppMessage: function () {

  }
})