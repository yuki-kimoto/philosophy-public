<!DOCTYPE html>
<html>
  <head>
    <!-- meta -->
<!-- Google Automatic Advertising -->
<script async src="https://pagead2.googlesyndication.com/pagead/js/adsbygoogle.js?client=ca-pub-4525414114581084"
     crossorigin="anonymous"></script>

<meta charset="UTF-8">
<meta name="viewport" content="width=device-width,initial-scale=1.0,minimum-scale=1.0">
<link rel="icon" type="image/x-icon" href="/images/logo.png">
<link rel="stylesheet" type="text/css" href="/css/common.css">

<script type="text/javascript" src="/js/jquery-1.9.0.min.js"></script>
<script type="text/javascript" src="/js/google-code-prettify/prettify.js"></script>
<link  type="text/css" rel="stylesheet" href="/js/google-code-prettify/prettify.css"/>
<script>
  $(function(){
    // google code prettifyの有効化
    $("pre").addClass("prettyprint");
    function init(event){
      prettyPrint();
    }
    if(window.addEventListener)window.addEventListener("load",init,false);
    else if(window.attachEvent)window.attachEvent("onload",init);
    
    $(".to-top").click(function() {
      // ページの一番上までスクロールさせます。
      $('body, html').animate({scrollTop: 0}, 300, 'linear');;
    });
  });
</script>


<!-- Global site tag (gtag.js) - Google Analytics -->
<script async src="https://www.googletagmanager.com/gtag/js?id=G-YB6G48MD78"></script>
<script>
  window.dataLayer = window.dataLayer || [];
  function gtag(){dataLayer.push(arguments);}
  gtag('js', new Date());

  gtag('config', 'G-YB6G48MD78');
</script>
<title>Title - Perlの哲学 - Perlの誤解を解きたい</title>
<meta name="description" content="#!/usr/bin/env perl">
  </head>
  <body>
    <div class="container">
      <div class="header">
        <div class="header_main">
  <h1>
    <a href="/"><img src="/images/logo.png">Perlの哲学</a>
  </h1>
  <div class="header_right">
    <a rel="nofollow" href="https://perlclub.net/account/create">会員登録</a>
  </div>
</div>

      </div>
      <div class="main">
        <div class="content">
          <div class="entry">
  <div class="top">
    <!-- top -->

  </div>
  <div class="middle">
    <p>
  #!/usr/bin/env perl
</p>
<div style="width:calc(100% - 30px);margin:10px auto;">
  <script async src="https://pagead2.googlesyndication.com/pagead/js/adsbygoogle.js?client=ca-pub-4525414114581084"
       crossorigin="anonymous"></script>
  <!-- 最初の段落下 - ディスプレイ 横長 レスポンシブ -->
  <ins class="adsbygoogle"
       style="display:block"
       data-ad-client="ca-pub-4525414114581084"
       data-ad-slot="2828858335"
       data-ad-format="auto"
       data-full-width-responsive="true"></ins>
  <script>
       (adsbygoogle = window.adsbygoogle || []).push({});
  </script>
</div>


<p>
  use strict;
</p>
<p>
  use warnings;
</p>
<p>
  use utf8;
</p>
<p>
  use Encode 'encode';
</p>
<p>
  # Title mail form
</p>
<p>
  my $title = 'Mail form';
</p>
<p>
  # Content mail form
</p>
<p>
  my $content = <<"EOS";
</p>
<h2><a href="/test.cgi">Title</a></h2>
<div>
  Content
</div>
<p>
  EOS
</p>
<p>
  $content = build_html($title, $content);
</p>
<p>
  my $html = <<"EOS";
</p>
<p>
  Content-type: text/html; charset=UTF-8
</p>
<p>
  $content
</p>
<p>
  EOS
</p>
<p>
  print encode('UTF-8', $html);
</p>
<p>
  sub build_html {
</p>
  my ($title, $content) = @_;
  
  local $/;
  my $html = <DATA>;
  
  $html =~ s/\$TITLE/$title/;
  $html =~ s/\$CONTENT/$content/;
  
  return $html;
<p>
  }
</p>
<p>
  __DATA__
</p>

  </div>
  <div class="bottom">
    <h3>関連情報</h3>

<div style="margin:10px 0">
<script async src="https://pagead2.googlesyndication.com/pagead/js/adsbygoogle.js?client=ca-pub-4525414114581084"
     crossorigin="anonymous"></script>
<ins class="adsbygoogle"
     style="display:block"
     data-ad-format="autorelaxed"
     data-ad-client="ca-pub-4525414114581084"
     data-ad-slot="9163995495"></ins>
<script>
     (adsbygoogle = window.adsbygoogle || []).push({});
</script>
</div>

  </div>
</div>

        </div>
        <div class="side">
          <div style="margin-bottom:30px">
<script async src="https://pagead2.googlesyndication.com/pagead/js/adsbygoogle.js?client=ca-pub-4525414114581084"
     crossorigin="anonymous"></script>
<!-- ディスプレイ縦長 -->
<ins class="adsbygoogle"
     style="display:block"
     data-ad-client="ca-pub-4525414114581084"
     data-ad-slot="4544919209"
     data-ad-format="auto"
     data-full-width-responsive="true"></ins>
<script>
     (adsbygoogle = window.adsbygoogle || []).push({});
</script>
</div>

<div style="margin-bottom:30px;padding:0 8px;">
<script async src="https://pagead2.googlesyndication.com/pagead/js/adsbygoogle.js?client=ca-pub-4525414114581084"
     crossorigin="anonymous"></script>
<ins class="adsbygoogle"
     style="display:block"
     data-ad-format="autorelaxed"
     data-ad-client="ca-pub-4525414114581084"
     data-ad-slot="9163995495"></ins>
<script>
     (adsbygoogle = window.adsbygoogle || []).push({});
</script>
</div>

        </div>
      </div>
      <div class="footer">
        <div class="perlri_link">
  <a rel="nofollow" href="https://perlclub.net">Perlクラブ</a>
</div>

<script async src="https://pagead2.googlesyndication.com/pagead/js/adsbygoogle.js?client=ca-pub-4525414114581084"
     crossorigin="anonymous"></script>
     
      </div>
    </div>
  </body>
</html>
