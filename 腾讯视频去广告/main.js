// ==UserScript==
// @name         腾讯视频去广告
// @namespace    http://tampermonkey.net/
// @version      1.0
// @description  去除腾讯视频广告
// @author       王子周棋洛
// @match        https://v.qq.com/x/cover/*
// @icon         https://img.fy6b.com/2022/08/28/1478991e577ea.png
// @license      MIT
// @grant        none
// ==/UserScript==

(function() {
    // 设置定时器，60毫秒执行一次
    setInterval(() => {
        // 获取所有广告的video标签
        var adVideos = document.querySelector(".txp_ad").children[0].children[0].childNodes;
        // 遍历广告集合
        adVideos.forEach(ad => {
            // 判断广告集合中每一个哪个广告正在播放
            if (ad.duration !== ad.currentTime) {
                // 设置src广告地址为空，就会继续填装下一个广告地址，直到所有广告填充完成
                ad.setAttribute('src', '');
            }
        })
    }, 70);
})();