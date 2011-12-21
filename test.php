<?php
/**
 * Order ID	order	字符串(16字节)	订单ID：该值是唯一的，如果开发者接收到相同的订单号，那说明该订单已经存在。订单号的生成规则见公共参数及算法。
App ID	app	字符串(16字节)	开发者应用ID
Ad Name	ad	广告名（50字节）	广告名，如果是应用类型的广告则是应用名
User ID	user	字符串	用户ID：开发者可以设置自己的用户ID，如果没有设置为我们的CID
Device ID	did	字符串	设备ID：android是imei，ios是udid
Channel	chn	整型	渠道号
Points	points	整型	用户可以赚取的积分
 * @var unknown_type
 */
$subject = 'drt=2011-12-19+14:44:47&cl=01&ac=200&cid=5QsDcVv0zZAD&wad=46&app=25364&ipn=com.tuan800.android&opvn=&ipvn=4.0.3&npvn=&opv=0&ipv=40003&npv=0&ip=60.210.112.226&ipr=192.168.0.1&country=CN&prv=山东&cty=淄博&tc=移动&brd=摩托罗拉&mod=mb525&cst=0&os=3&osv=2.3.7&ui=&av=10000&sv=100&src=3&spc=0&out=0&pn=com.bearmedia.ringsthree&ei=356509044394054&si=460020684060559&bd=&mac=&apn=wifi&cn=%E4%B8%AD%E5%9B%BD%E7%A7%BB%E5%8A%A8&dd=MB525&dv=MOTO&po=android+2.3.7&rt=1324277207&sw=480&sh=854&cell=0|460|00|5792|25396&lat=&lon=&pv=1&ups=12&e1=&e2=&e3=&e4=&e5=&e6=&e7=&e8=&e9=&e10=&ua=Mozilla%2F5.0+%28Linux%3B+U%3B+Android+2.3.7%3B+zh-cn%3B+MB525+Build%2FDospy+ROM%29+AppleWebkit%2F533.1+%28KHTML%2C+like+Gecko%29+Version%2F4.0+Mobile+Safari%2F533.1
drt=2011-12-19+14:44:53&cl=01&ac=200&cid=RxP709EbYkCq&wad=125&app=25873&ipn=com.gamebox.kinguc31&opvn=&ipvn=1.31.1105&npvn=&opv=0&ipv=3&npv=0&ip=221.13.78.17&ipr=192.168.0.1&country=CN&prv=西藏&cty=拉萨&tc=联通&brd=三星&mod=gt-i9100&cst=0&os=3&osv=2.3.3&ui=&av=200&sv=100&src=3&spc=0&out=0&pn=com.nanoha.ziplock&ei=357470040046488&si=460019008611451&bd=&mac=&apn=3gnet&cn=chn-cugsm&dd=GT-I9100&dv=samsung&po=android+2.3.3&rt=1324190642&sw=480&sh=800&cell=0|460|01|112994136|58184&lat=&lon=&pv=1&ups=12&e1=&e2=&e3=&e4=&e5=&e6=&e7=&e8=&e9=&e10=&ua=Mozilla%2F5.0+%28Linux%3B+U%3B+Android+2.3.3%3B+zh-cn%3B+GT-I9100+Build%2FGINGERBREAD%29+AppleWebkit%2F533.1+%28KHTML%2C+like+Gecko%29+Version%2F4.0+Mobile+Safari%2F533.1
drt=2011-12-19+14:44:55&cl=01&ac=200&cid=7Rw5vh9Ke-yi&wad=28&app=14068&ipn=com.jingdong.app.mall&opvn=&ipvn=1.0.8&npvn=&opv=0&ipv=18&npv=0&ip=211.139.92.227&ipr=192.168.0.1&country=CN&prv=甘肃&cty=兰州&tc=移动&brd=天语&mod=u2&cst=0&os=3&osv=2.2.1&ui=&av=1500&sv=110&src=3&spc=0&out=0&pn=com.galeapp.ebookcity&ei=865334001490637&si=460023956880999&bd=&mac=&apn=cmnet&cn=%E4%B8%AD%E5%9B%BD%E7%A7%BB%E5%8A%A8&dd=U2&dv=qcom&po=android+2.2.1&rt=1324277078&sw=320&sh=480&cell=0|460|00|1291|37757&lat=&lon=&pv=1&ups=12&e1=1&e2=CN|zh&e3=&e4=&e5=&e6=&e7=&e8=&e9=&e10=&ua=Mozilla%2F5.0+%28Linux%3B+U%3B+Android+2.2.1%3B+zh-cn%3B+U2+Build%2FFRG83%29+AppleWebkit%2F533.1+%28KHTML%2C+like+Gecko%29+Version%2F4.0+Mobile+Safari%2F533.1
drt=2011-12-19+14:44:57&cl=01&ac=200&cid=pZ_CakIL6-j4&wad=94&app=22764&ipn=com.clou.sns.android.anywhered&opvn=&ipvn=1.09&npvn=&opv=0&ipv=109&npv=0&ip=112.97.192.30&ipr=192.168.0.1&country=CN&prv=广东&cty=深圳&tc=联通&brd=HTC&mod=glacier&cst=0&os=3&osv=2.3.4&ui=&av=100&sv=100&src=3&spc=0&out=0&pn=com.sheep.QQnczs&ei=354697045631137&si=460015917602415&bd=&mac=&apn=3gnet&cn=%E4%B8%AD%E5%9B%BD%E8%81%94%E9%80%9A&dd=HTC+Glacier&dv=htc_wwe&po=android+2.3.4&rt=1324277085&sw=480&sh=800&cell=&lat=&lon=&pv=1&ups=12&e1=&e2=&e3=&e4=&e5=&e6=&e7=&e8=&e9=&e10=&ua=Mozilla%2F5.0+%28Linux%3B+U%3B+Android+2.3.4%3B+zh-cn%3B+HTC+Glacier+Build%2FGRJ22%29+AppleWebkit%2F533.1+%28KHTML%2C+like+Gecko%29+Version%2F4.0+Mobile+Safari%2F533.1';

$pattern = '/drt=(?P<drt>[\d\-\+\:]*)&cl=\d+&ac=200&cid=(?P<cid>[^&]+)&wad=(?P<wad>\d+)&app=(?P<app>\d+)&[^\n]+&src=(?P<src>\d)&[^\n]+&ei=(?P<ei>[^&]*)&[^\n]*&ups=(?P<ups>[^&]*)&e1=(?P<chn>\d*)&/';


preg_match_all($pattern, $subject, $matches);

var_dump($matches);

exit;

$app = 2879;
$str = '22023|22727|2879|5161|888|25808|5970|7239|6343';

if (preg_match("/(?:^|\|){$app}(?:\||$)/", $str, $match))
{
    var_dump($match);
}
else
{
    echo 'not match';
}


$p = "/^[1-9]$|^(?:10)$/";
for ($i=0; $i<20; $i++)
{
    if (preg_match($p, ''.$i))
    {
        echo "\n$i   match";
    }
    else
    {
        echo "\n$i   not match";
    }
}

?>