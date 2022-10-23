(function () {

    // 只需要在此处定义需要隐藏元素
    var clearElementArr = [
        
    ];

    // 这是架子代码，不用改动
    console.log("准备隐藏以下元素 >>> " + clearElementArr);
    window.pageC = function (clearElements) {
        let style = document.createElement("style");
        if (typeof (clearElements) === "object") {
            clearElements.forEach(cE => {
                style.innerText += `${cE} {display: none !important;} `
            });
        } else { 
            console.error("param error,require array!"); 
        }
        document.head.appendChild(style);
    };
    pageC(clearElementArr);
    console.log("清理完成！");
})();