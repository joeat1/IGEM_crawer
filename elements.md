# summary #
## basic setting ##

+ css&js style
> You need to use some personal scripts.
```
<link href="https://2019.igem.org/Template:NUDT_CHINA/bootstrap_css?action=raw&ctype=text/css" rel="stylesheet"/>
<script type="text/javascript" src="https://2019.igem.org/Template:NUDT_CHINA/bootstrap_js?action=raw&ctype=text/javascript"></script>
```
+ common style
> You need to remove the effects of the original platform's style and unify the basic style of key labels ,such as p,img,li,div.
```
/* ==========================================================================
   Component: The basic settings
 ============================================================================ */
#mw-content-text p{
    font-size: 1rem;
    font-weight: 400;
    line-height: 1.5;
    color: #212529;
    text-align: justify;
    margin: 0px;}
#content {
    padding: 0px;
    margin: 0px;
    width: 100%;
}
#bodyContent h1,
#bodyContent h2,
#bodyContent h3,
#bodyContent h4,
#bodyContent h5 {
    margin-bottom: 0px;
    border-bottom: none;
}
body {background-color:white; }

#bodyContent {
    padding-right: 0px;
}
#globalWrapper {
    font-size: 100%;
    padding: 0px;
    margin: 0px;
}
#top_title {
    visibility: hidden;
    display:none;
}

.modal-backdrop {
  display: none;
}
p {
  text-align: center;
  font-size: 24px
}
p img {
  margin: 0 auto;
  display: block;
}
img {
  max-width: 100%;
}
li  {
  text-align: left;
}
/* ==========================================================================
   Component: Nav
 ============================================================================ */
 
/* ==========================================================================
   Component: Cover-pic
 ============================================================================ */
```

## Some useful elements ##
+ carousel
> Maybe you need a carousel to show the pictures.
```
<div class="carousel slide" id="carousel">
    <ol class="carousel-indicators" style="width:40%">
        <li data-slide-to="0" data-target="#carousel"></li>
        <li data-slide-to="1" data-target="#carousel"></li>
        <li data-slide-to="2" data-target="#carousel"></li>
    </ol>
    <div class="carousel-inner">
        <div class="item active" style="width:100%">
            <img src="team.jpg" class="img-responsive center-block"/>
            <div class="carousel-caption">
                <h4>WE ARE FAMILY!</h4>
            </div>
        </div>
        <div class="item" style="width:100%">
            <img src="trim.jpg" class="img-responsive center-block"/>
            <div class="carousel-caption">
                <h4>FAMILY</h4>
            </div>
        </div>
        <div class="item" style="width:100%">
            <img src="all1.jpg" class="img-responsive center-block"/>
            <div class="carousel-caption">
            <h4>FAMILY SELFIE</h4>
        </div>
      </div>
    </div> 
    <a class="left carousel-control" href="#carousel" data-slide="prev" style="background:url('/left.png')  no-repeat center center;">
    </a> 
    <a class="right carousel-control" href="#carousel" data-slide="next" style="background:url('/left.png')  no-repeat center center; transform: rotate(180deg);">
    </a>
</div>
```
+ Large picture
> Maybe you need a large picture to cover the screen.
```
<style>
/* Jumbotron */
        .jumbotron {
			height: calc(100vh);
			background-position: center;
			background-size: cover;
			background-attachment: fixed;
			position: relative;
		}
		.jumbotron div {
			background: linear-gradient(rgba(0, 0, 0, 0), rgba(0, 0, 0, .8));
			position: absolute;
			bottom: 0;
			width: 100%;
			text-align: center;
		}
		.jumbotron div h1, .jumbotron div h2 {
			color: #fff;
			text-shadow: rgba(0,0,0,0.6) 0 0.3vh 0.5vh
		}
		.jumbotron div h1 {
			font-size: 7em;
		}
		.jumbotron div h2 {
			font-size: 1.5em;
		}
		.jumbotron div svg {
			margin: 2em 0 3em 0;
			transition: all 0.5s ease;
			height: 3em;
			cursor: pointer;
		}
		.jumbotron div svg:hover {
			height: 3.5em;
			margin: 2em 0 3em 0;
		}
		.jumbotron div svg path {
			transition: stroke 0.5s ease;
			stroke: #ccc;
		}
		.jumbotron div svg:hover path {
			stroke: #fff;
		}
</style>
<div class="jumbotron" style="background-image: url('background.jpg');">
        <div>
            <h1>Human Practices</h1>
            <h2>Tying it all together</h2>
            <svg onclick="$('html, body').animate({scrollTop: $(this.parentNode.parentNode.nextElementSibling).offset().top - 69 }, 500);" height="4vh" xmlns="http://www.w3.org/2000/svg" viewBox="0 0 109.7 39.6">
                <path fill="none" stroke="#fff" stroke-width="10" d="M104.6 5L54.8 33.8 5 5" stroke-linecap="round"></path>
            </svg>
        </div>
</div>
```
+ basic container
> If you use the framework named bootstrap, you need to known the basic construction.
```
<div class="container">
    <div class="row" >
        <div class="col-md-12 column">
            
        </div>
    </div>
</div>
```
+ href
> If you need to set the inner-link, you need to known the style.
```
<style>
.anchorOffset {
    display: block !important;
    position: relative !important;
    top: -80px !important;
    visibility: hidden !important;
}
</style>
<a href="#Title" style="text-decoration: none;">Title</a>
....
....
<a class="anchorOffset" id="Title" data-scroll-id="Title" tabindex="-1" style="outline: none;"></a>
<h3>Title</h3>
```
+ pic
> If you use the framework named bootstrap, you need to known the way to placing pictures.
```
<div class="col-md-12" style="display: -webkit-box;">
	<div class="col-md-6 thumbnail">
		<img src="background.jpg">
		<p style="text-align: center;">Description of the pic </p>
	</div>
	<div class="col-md-6 thumbnail">
		<img src="_background.jpg">
		<p style=" text-align: center;">Description of the pic </p>
	</div>
</div>
```
