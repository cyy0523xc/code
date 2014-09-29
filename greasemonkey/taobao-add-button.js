
var ibbdQuery = window.ibbdQuery = jQuery.noConflict();

var ibbd_timeout_delay = 200;
var ibbdWait = function(selector, selector_text)
{
　　 var dtd = ibbdQuery.Deferred(); //在函数内部，新建一个Deferred对象
    
    var tasks = function(selector, selector_text) {
        var loaded_ok = false;
        try {
            if (ibbdQuery(selector).size() > 0) {
                if ('undefined' != typeof selector_text) {
                    // 指定了对象的值，分页使用
                    if (ibbdQuery(selector).text() == selector_text) {
                        loaded_ok = true;
                    }
                } else {
                    loaded_ok = true;
                }
            }
        } catch(e) {}
        
        if (loaded_ok) {
            dtd.resolve();
        }
        
        setTimeout(function(){tasks(selector, selector_text);}, ibbd_timeout_delay);
    };
    
    tasks(selector, selector_text);
    
    return dtd.promise();
};


var ibbdPromise = window.ibbdPromise = function(selector, selector_text) 
{
    return ibbdQuery.when(ibbdWait(selector, selector_text));
};


var ibbdAddButton = window.ibbdAddButton = function()
{
    ibbdQuery("li.item").each(function(){
        var html=ibbdQuery(this).html();
        var text=ibbdQuery("div.name", this).text();
        text = ibbdQuery.trim(text);
        text = text.replace(/^\d+[\s\n]*/, '');
        text = ibbdQuery.trim(text);
        //console.log(ibbdQuery('div.name', this).toArray());
        ibbdQuery(this).html(html + "<span><button onclick='alert(\""+text+"\")'>选择</button></span>");
    });
};

//console.log('begin');
//ibbdPromise('li.item')
//.done(ibbdAddButton);

//console.log('end');
