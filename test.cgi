<!DOCTYPE html>
<html>
  <head>
    <!-- meta -->
<meta charset="UTF-8">
<meta name="viewport" content="width=device-width,initial-scale=1.0,minimum-scale=1.0">
<link rel="stylesheet" type="text/css" href="/css/common.css">
<link rel="shortcut icon" href="/images/philosophi-favicon.png">

<title>Title - Perlの哲学 - Perlに対する誤解を解きたい</title>
<meta name="description" content="#!/usr/bin/env perl">
  </head>
  <body>
    <div class="container">
      <div class="header">
        <!-- header -->
<h1>
  <a href="/"><img src="/images/philosophi-logo.png" alt="Perlの哲学 - Perlに対する誤解を解く"></a>
</h1>

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
    <!-- bottom -->

<h3>Perlの哲学 - Perlに対する誤解を解きたいのご紹介</h3>

<iframe width="560" height="315" src="https://www.youtube.com/embed/KfvdD9ns-m0" frameborder="0" allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture" allowfullscreen></iframe>


  </div>
</div>

        </div>
        <div class="side">
          <!-- side -->
<div class="side-list">
  <div class="side-list-title">
    目次
  </div>
  <ul>
    <li><a href="/list.html">記事の一覧</a></li>
  </ul>
</div>

        </div>
      </div>
      <div class="footer">
        <!-- footer -->
<a href="https://kimoto-system.co.jp/">サイト運営 木本システム</a> <span style="color:white">&</span> <span style="color:white">Copyright © 2020-2020 Yuki Kimoto</span>

      </div>
    </div>
  </body>
</html>
