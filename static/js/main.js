var smartSpeedMS=800;function catsServsTabs(){$(".c-tabs button").click((function(e){e.preventDefault();var t=$(this).data("panel"),n=$(this).data("panel-class");$(this).parent().find("button").removeClass("active"),$(this).addClass("active"),$(n).slideUp(0),$(t).slideDown(0)}))}function vilSelect(){$(".vil-select-wrap select").each((function(){vilSelectHandleText($(this))})),$(document).on("change",".vil-select-wrap select",(function(){vilSelectHandleText($(this))}))}function vilSelectHandleText(e){var t=e.parent().find("span"),n=e.find("option:selected").text();t.text(n)}function topNewsCarouselOwl(){$(".single-slide").each((function(){$(this).owlCarousel({loop:!1,margin:0,items:1,dots:!1,nav:!0,smartSpeed:smartSpeedMS,autoplay:!0,responsive:{0:{items:1}},onInitialized:function(e){$(e.target).append('<div class="owl-counter"><span class="owl-counter-index">'+(e.item.index+1)+'</span><span class="owl-counter-total">'+e.item.count+"</span></div>")},onChanged:function(e){$(e.target).find(".owl-counter-index").text(e.item.index+1)}})}))}function directorsCarouselOwl(){$(".directors-slider").owlCarousel({loop:!0,margin:0,items:1,dots:!1,nav:!0,smartSpeed:smartSpeedMS,autoplay:!1,onTranslated:function(e){setItemHeight($(e.target))},onInitialized:function(e){setTimeout((function(){setItemHeight($(e.target))}),100)}})}function setItemHeight(e){var t=e.find(".owl-item.active").innerHeight();e.css("height",t+90)}function initMyServicesSlider(){$(".my-services.owl-carousel").each((function(){$(this).owlCarousel({margin:20,items:1,dots:!0,nav:!0,autoWidth:!0,smartSpeed:smartSpeedMS,autoHeight:!1,autoplay:!1,responsive:{0:{items:1},576:{items:2},768:{items:3},992:{items:4},1024:{items:3},1280:{items:4}}})}))}window.addEventListener("DOMContentLoaded",(function(){var e=document.getElementById("preloader");e&&setTimeout((function(){e.remove()}),300)})),$(document).ready((function(){topNewsCarouselOwl(),directorsCarouselOwl(),catsServsTabs(),vilSelect(),$(".vil-main-nav__inner").each((function(){$(this).prev("a").click((function(e){e.preventDefault(),$(this).next().toggleClass("active")}))})),$(".main-nav-toggle").click((function(e){e.preventDefault(),$(this).toggleClass("active"),$(this).next("ul").toggleClass("active")})),$(".nur-services-box__item.__expand").click((function(e){e.preventDefault(),$(this).parents(".nur-services").toggleClass("active"),$(this).parents(".nur-services").prevAll().toggleClass("passive")})),$(".app-request__form .__close").click((function(e){e.preventDefault(),$(".app-request__form").fadeOut("fast")})),$(".nur-nav-button").click((function(e){e.preventDefault(),$(".nur-main-nav").slideToggle("fast")})),$(".nur-main-nav-close").click((function(e){e.preventDefault(),$(".nur-main-nav").fadeOut("fast")})),$(".inner-menu-toggle").click((function(e){e.preventDefault(),$(this).toggleClass("active"),$(".interactive-services").slideToggle("fast")})),$(".vil-header-search > button").on("click",(function(e){e.preventDefault(),$(this).parent().toggleClass("active")}))}));





