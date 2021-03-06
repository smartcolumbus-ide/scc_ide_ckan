<!DOCTYPE html>
<html class="" lang="en">
<head prefix="og: http://ogp.me/ns#">
<meta charset="utf-8">
<meta content="IE=edge" http-equiv="X-UA-Compatible">
<meta content="object" property="og:type">
<meta content="GitLab" property="og:site_name">
<meta content="usr/lib/ckan/default/src/ckan/sc_datasets2.sh · master · smartcolumbus-ide / dataportal / ckan" property="og:title">
<meta content="GitLab.com" property="og:description">
<meta content="https://gitlab.com/assets/gitlab_logo-7ae504fe4f68fdebb3c2034e36621930cd36ea87924c11ff65dbcb8ed50dca58.png" property="og:image">
<meta content="64" property="og:image:width">
<meta content="64" property="og:image:height">
<meta content="https://gitlab.com/smartcolumbus-ide/dataportal/ckan/blob/master/usr/lib/ckan/default/src/ckan/sc_datasets2.sh" property="og:url">
<meta content="summary" property="twitter:card">
<meta content="usr/lib/ckan/default/src/ckan/sc_datasets2.sh · master · smartcolumbus-ide / dataportal / ckan" property="twitter:title">
<meta content="GitLab.com" property="twitter:description">
<meta content="https://gitlab.com/assets/gitlab_logo-7ae504fe4f68fdebb3c2034e36621930cd36ea87924c11ff65dbcb8ed50dca58.png" property="twitter:image">

<title>usr/lib/ckan/default/src/ckan/sc_datasets2.sh · master · smartcolumbus-ide / dataportal / ckan · GitLab</title>
<meta content="GitLab.com" name="description">
<link rel="shortcut icon" type="image/x-icon" href="/assets/favicon-075eba76312e8421991a0c1f89a89ee81678bcde72319dd3e8047e2a47cd3a42.ico" id="favicon" />
<link rel="stylesheet" media="all" href="/assets/application-61d4cb7e100f2fac8ccaeac5e18d08f97554f0639e84004165d6f9697cfbe08c.css" />
<link rel="stylesheet" media="print" href="/assets/print-74b3d49adeaada27337e759b75a34af7cf3d80051de91d60d40570f5a382e132.css" />


<!-- / TODO: Combine these 2 stylesheets into application.scss -->
<link rel="stylesheet" media="all" href="/assets/new_nav-9dc36451d6461185b3c501b73a23f48936cda9ee5b0b8f9b1001c951ce12eabf.css" />
<link rel="stylesheet" media="all" href="/assets/new_sidebar-1f383f3cb338b8ecf8062dab06052141f414f51165f656b97a0930c0d38cd7dc.css" />
<script>
//<![CDATA[
window.gon={};gon.api_version="v4";gon.default_avatar_url="https:\/\/gitlab.com\/assets\/no_avatar-849f9c04a3a0d0cea2424ae97b27447dc64a7dbfae83c036c45b403392f0e8ba.png";gon.max_file_size=10;gon.asset_host=null;gon.webpack_public_path="\/assets\/webpack\/";gon.relative_url_root="";gon.shortcuts_path="\/help\/shortcuts";gon.user_color_scheme="white";gon.katex_css_url="\/assets\/katex-dc07578acd203b2dd73a8c78cdb8dcb79144ba11a23749d80904496b7ff8a650.css";gon.katex_js_url="\/assets\/katex-04bcf56379fcda0ee7c7a63f71d0fc15ffd2e014d017cd9d51fd6554dfccf40a.js";gon.sentry_dsn="https:\/\/526a2f38a53d44e3a8e69bfa001d1e8b@sentry.gitlap.com\/15";gon.gitlab_url="https:\/\/gitlab.com";gon.revision="9c3a3ca";gon.gitlab_logo="\/assets\/gitlab_logo-7ae504fe4f68fdebb3c2034e36621930cd36ea87924c11ff65dbcb8ed50dca58.png";gon.current_user_id=1228399;gon.current_username="rajones";gon.current_user_fullname="Richard Jones";gon.current_user_avatar_url="https:\/\/secure.gravatar.com\/avatar\/ccec7695c9067b41ae74a273cb4a04af?s=80\u0026d=identicon";
//]]>
</script>
<script src="/assets/webpack/webpack_runtime.294a69f1dca44b9962ff.bundle.js" defer="defer"></script>
<script src="/assets/webpack/common.c04294b903455a34f707.bundle.js" defer="defer"></script>
<script src="/assets/webpack/locale.b9a56fbc6e00d576d16c.bundle.js" defer="defer"></script>
<script src="/assets/webpack/main.78a00e6bb497a127e58c.bundle.js" defer="defer"></script>
<script src="/assets/webpack/raven.c94699aec8e665da5599.bundle.js" defer="defer"></script>


<script src="/assets/webpack/blob.6043bed197eb079db95f.bundle.js" defer="defer"></script>
<script src="/assets/webpack/blob.6043bed197eb079db95f.bundle.js" defer="defer"></script>

<script>
  window.uploads_path = "/smartcolumbus-ide/dataportal/ckan/uploads";
</script>

<meta name="csrf-param" content="authenticity_token" />
<meta name="csrf-token" content="KLSdCb/WDZi3fIvPYlxZI3hjCPZGzh0qFku2LcvoGzh/Me+H/i8aSU4Rx0jb1Ry8Vns0AjJ1gDozB9YfErbzgg==" />
<meta content="origin-when-cross-origin" name="referrer">
<meta content="width=device-width, initial-scale=1, maximum-scale=1" name="viewport">
<meta content="#474D57" name="theme-color">
<link rel="apple-touch-icon" type="image/x-icon" href="/assets/touch-icon-iphone-5a9cee0e8a51212e70b90c87c12f382c428870c0ff67d1eb034d884b78d2dae7.png" />
<link rel="apple-touch-icon" type="image/x-icon" href="/assets/touch-icon-ipad-a6eec6aeb9da138e507593b464fdac213047e49d3093fc30e90d9a995df83ba3.png" sizes="76x76" />
<link rel="apple-touch-icon" type="image/x-icon" href="/assets/touch-icon-iphone-retina-72e2aadf86513a56e050e7f0f2355deaa19cc17ed97bbe5147847f2748e5a3e3.png" sizes="120x120" />
<link rel="apple-touch-icon" type="image/x-icon" href="/assets/touch-icon-ipad-retina-8ebe416f5313483d9c1bc772b5bbe03ecad52a54eba443e5215a22caed2a16a2.png" sizes="152x152" />
<link color="rgb(226, 67, 41)" href="/assets/logo-d36b5212042cebc89b96df4bf6ac24e43db316143e89926c0db839ff694d2de4.svg" rel="mask-icon">
<meta content="/assets/msapplication-tile-1196ec67452f618d39cdd85e2e3a542f76574c071051ae7effbfde01710eb17d.png" name="msapplication-TileImage">
<meta content="#30353E" name="msapplication-TileColor">


<!-- Piwik -->
<script>
  var _paq = _paq || [];
  _paq.push(['trackPageView']);
  _paq.push(['enableLinkTracking']);
  (function() {
    var u="//piwik.gitlab.com/";
    _paq.push(['setTrackerUrl', u+'piwik.php']);
    _paq.push(['setSiteId', 1]);
    var d=document, g=d.createElement('script'), s=d.getElementsByTagName('script')[0];
    g.type='text/javascript'; g.async=true; g.defer=true; g.src=u+'piwik.js'; s.parentNode.insertBefore(g,s);
  })();
</script>
<noscript><p><img src="//piwik.gitlab.com/piwik.php?idsite=1" style="border:0;" alt="" /></p></noscript>
<!-- End Piwik Code -->


</head>

<body class="ui_indigo " data-find-file="/smartcolumbus-ide/dataportal/ckan/find_file/master" data-group="" data-page="projects:blob:show" data-project="ckan">



<header class="navbar navbar-gitlab navbar-gitlab-new">
<a class="sr-only gl-accessibility" href="#content-body" tabindex="1">Skip to content</a>
<div class="container-fluid">
<div class="header-content">
<div class="title-container">
<h1 class="title">
<a title="Dashboard" id="logo" href="/"><svg width="24" height="24" class="tanuki-logo" viewBox="0 0 36 36">
  <path class="tanuki-shape tanuki-left-ear" fill="#e24329" d="M2 14l9.38 9v-9l-4-12.28c-.205-.632-1.176-.632-1.38 0z"/>
  <path class="tanuki-shape tanuki-right-ear" fill="#e24329" d="M34 14l-9.38 9v-9l4-12.28c.205-.632 1.176-.632 1.38 0z"/>
  <path class="tanuki-shape tanuki-nose" fill="#e24329" d="M18,34.38 3,14 33,14 Z"/>
  <path class="tanuki-shape tanuki-left-eye" fill="#fc6d26" d="M18,34.38 11.38,14 2,14 6,25Z"/>
  <path class="tanuki-shape tanuki-right-eye" fill="#fc6d26" d="M18,34.38 24.62,14 34,14 30,25Z"/>
  <path class="tanuki-shape tanuki-left-cheek" fill="#fca326" d="M2 14L.1 20.16c-.18.565 0 1.2.5 1.56l17.42 12.66z"/>
  <path class="tanuki-shape tanuki-right-cheek" fill="#fca326" d="M34 14l1.9 6.16c.18.565 0 1.2-.5 1.56L18 34.38z"/>
</svg>

<span class="logo-text hidden-xs">
<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 617 169"><path d="M315.26 2.97h-21.8l.1 162.5h88.3v-20.1h-66.5l-.1-142.4M465.89 136.95c-5.5 5.7-14.6 11.4-27 11.4-16.6 0-23.3-8.2-23.3-18.9 0-16.1 11.2-23.8 35-23.8 4.5 0 11.7.5 15.4 1.2v30.1h-.1m-22.6-98.5c-17.6 0-33.8 6.2-46.4 16.7l7.7 13.4c8.9-5.2 19.8-10.4 35.5-10.4 17.9 0 25.8 9.2 25.8 24.6v7.9c-3.5-.7-10.7-1.2-15.1-1.2-38.2 0-57.6 13.4-57.6 41.4 0 25.1 15.4 37.7 38.7 37.7 15.7 0 30.8-7.2 36-18.9l4 15.9h15.4v-83.2c-.1-26.3-11.5-43.9-44-43.9M557.63 149.1c-8.2 0-15.4-1-20.8-3.5V70.5c7.4-6.2 16.6-10.7 28.3-10.7 21.1 0 29.2 14.9 29.2 39 0 34.2-13.1 50.3-36.7 50.3m9.2-110.6c-19.5 0-30 13.3-30 13.3v-21l-.1-27.8h-21.3l.1 158.5c10.7 4.5 25.3 6.9 41.2 6.9 40.7 0 60.3-26 60.3-70.9-.1-35.5-18.2-59-50.2-59M77.9 20.6c19.3 0 31.8 6.4 39.9 12.9l9.4-16.3C114.5 6 97.3 0 78.9 0 32.5 0 0 28.3 0 85.4c0 59.8 35.1 83.1 75.2 83.1 20.1 0 37.2-4.7 48.4-9.4l-.5-63.9V75.1H63.6v20.1h38l.5 48.5c-5 2.5-13.6 4.5-25.3 4.5-32.2 0-53.8-20.3-53.8-63-.1-43.5 22.2-64.6 54.9-64.6M231.43 2.95h-21.3l.1 27.3v94.3c0 26.3 11.4 43.9 43.9 43.9 4.5 0 8.9-.4 13.1-1.2v-19.1c-3.1.5-6.4.7-9.9.7-17.9 0-25.8-9.2-25.8-24.6v-65h35.7v-17.8h-35.7l-.1-38.5M155.96 165.47h21.3v-124h-21.3v124M155.96 24.37h21.3V3.07h-21.3v21.3"/></svg>

</span>
</a></h1>
<ul class="list-unstyled navbar-sub-nav">
<li id="nav-projects-dropdown" class="home dropdown header-projects"><a data-toggle="dropdown" href="#">
Projects
<svg xmlns="http://www.w3.org/2000/svg" width="16" height="16" class="caret-down" viewBox="0 0 16 16"><path fill-rule="evenodd" d="M8 10.243l-4.95-4.95a1 1 0 0 0-1.414 1.414l5.657 5.657a.997.997 0 0 0 1.414 0l5.657-5.657a1 1 0 0 0-1.414-1.414L8 10.243z"/></svg>

</a>
<div class="dropdown-menu projects-dropdown-menu">
<div class="projects-dropdown-container">
<div class="project-dropdown-sidebar">
<ul>
<li class=""><a href="/dashboard/projects">Your projects
</a></li><li class=""><a href="/dashboard/projects/starred">Starred projects
</a></li><li class=""><a href="/explore">Explore projects
</a></li></ul>
</div>
<div class="project-dropdown-content">
<div data-project-id="3560504" data-project-name="ckan" data-project-namespace="smartcolumbus-ide / dataportal / ckan" data-project-web-url="https://gitlab.com/smartcolumbus-ide/dataportal/ckan" data-user-name="rajones" id="js-projects-dropdown"></div>
</div>
</div>

</div>
</li><li class="hidden-xs"><a class="dashboard-shortcuts-groups" title="Groups" href="/dashboard/groups">Groups
</a></li><li class="visible-lg"><a class="dashboard-shortcuts-activity" title="Activity" href="/dashboard/activity">Activity
</a></li><li class="visible-lg"><a class="dashboard-shortcuts-milestones" title="Milestones" href="/dashboard/milestones">Milestones
</a></li><li class="visible-lg"><a class="dashboard-shortcuts-snippets" title="Snippets" href="/dashboard/snippets">Snippets
</a></li><li class="header-more dropdown hidden-lg">
<a data-toggle="dropdown" href="#">
More
<svg xmlns="http://www.w3.org/2000/svg" width="16" height="16" class="caret-down" viewBox="0 0 16 16"><path fill-rule="evenodd" d="M8 10.243l-4.95-4.95a1 1 0 0 0-1.414 1.414l5.657 5.657a.997.997 0 0 0 1.414 0l5.657-5.657a1 1 0 0 0-1.414-1.414L8 10.243z"/></svg>

</a>
<div class="dropdown-menu">
<ul>
<li class="visible-xs"><a class="dashboard-shortcuts-groups" title="Groups" href="/dashboard/groups">Groups
</a></li><li class=""><a title="Activity" href="/dashboard/activity">Activity
</a></li><li class=""><a class="dashboard-shortcuts-milestones" title="Milestones" href="/dashboard/milestones">Milestones
</a></li><li class=""><a class="dashboard-shortcuts-snippets" title="Snippets" href="/dashboard/snippets">Snippets
</a></li></ul>
</div>
</li>
<li class="hidden">
<a title="Projects" class="dashboard-shortcuts-projects" href="/dashboard/projects">Projects
</a></li>
</ul>

</div>
<div class="navbar-collapse collapse">
<ul class="nav navbar-nav">
<li class="header-new dropdown">
<a class="header-new-dropdown-toggle has-tooltip" title="New..." ref="tooltip" aria-label="New..." data-toggle="dropdown" data-placement="bottom" data-container="body" href="/projects/new"><svg xmlns="http://www.w3.org/2000/svg" width="16" height="16" viewBox="0 0 16 16"><path fill-rule="evenodd" d="M9 7V4c0-.552-.448-1-1-1s-1 .448-1 1v3H4c-.552 0-1 .448-1 1s.448 1 1 1h3v3c0 .552.448 1 1 1s1-.448 1-1V9h3c.552 0 1-.448 1-1s-.448-1-1-1H9zM3 0h10c1.657 0 3 1.343 3 3v10c0 1.657-1.343 3-3 3H3c-1.657 0-3-1.343-3-3V3c0-1.657 1.343-3 3-3z"/></svg>

<svg xmlns="http://www.w3.org/2000/svg" width="16" height="16" class="caret-down" viewBox="0 0 16 16"><path fill-rule="evenodd" d="M8 10.243l-4.95-4.95a1 1 0 0 0-1.414 1.414l5.657 5.657a.997.997 0 0 0 1.414 0l5.657-5.657a1 1 0 0 0-1.414-1.414L8 10.243z"/></svg>

</a><div class="dropdown-menu-nav dropdown-menu-align-right">
<ul>
<li class="dropdown-bold-header">This project</li>
<li>
<a href="/smartcolumbus-ide/dataportal/ckan/issues/new">New issue</a>
</li>
<li>
<a href="/smartcolumbus-ide/dataportal/ckan/merge_requests/new">New merge request</a>
</li>
<li class="header-new-project-snippet">
<a href="/smartcolumbus-ide/dataportal/ckan/snippets/new">New snippet</a>
</li>
<li class="divider"></li>
<li class="dropdown-bold-header">GitLab</li>
<li>
<a href="/projects/new">New project</a>
</li>
<li>
<a href="/groups/new">New group</a>
</li>
<li>
<a href="/snippets/new">New snippet</a>
</li>
</ul>
</div>
</li>

<li class="hidden-sm hidden-xs">
<div class="has-location-badge search search-form">
<form class="navbar-form" action="/search" accept-charset="UTF-8" method="get"><input name="utf8" type="hidden" value="&#x2713;" /><div class="search-input-container">
<div class="location-badge">This project</div>
<div class="search-input-wrap">
<div class="dropdown" data-url="/search/autocomplete">
<input type="search" name="search" id="search" placeholder="Search" class="search-input dropdown-menu-toggle no-outline js-search-dashboard-options" spellcheck="false" tabindex="1" autocomplete="off" data-toggle="dropdown" data-issues-path="https://gitlab.com/dashboard/issues" data-mr-path="https://gitlab.com/dashboard/merge_requests" aria-label="Search" />
<div class="dropdown-menu dropdown-select">
<div class="dropdown-content"><ul>
<li class="dropdown-menu-empty-item">
<a>
Loading...
</a>
</li>
</ul>
</div><div class="dropdown-loading"><i aria-hidden="true" data-hidden="true" class="fa fa-spinner fa-spin"></i></div>
</div>
<i class="search-icon"></i>
<i class="clear-icon js-clear-input"></i>
</div>
</div>
</div>
<input type="hidden" name="group_id" id="group_id" class="js-search-group-options" />
<input type="hidden" name="project_id" id="search_project_id" value="3560504" class="js-search-project-options" data-project-path="ckan" data-name="ckan" data-issues-path="/smartcolumbus-ide/dataportal/ckan/issues" data-mr-path="/smartcolumbus-ide/dataportal/ckan/merge_requests" />
<input type="hidden" name="search_code" id="search_code" value="true" />
<input type="hidden" name="repository_ref" id="repository_ref" value="master" />

<div class="search-autocomplete-opts hide" data-autocomplete-path="/search/autocomplete" data-autocomplete-project-id="3560504" data-autocomplete-project-ref="master"></div>
</form></div>

</li>
<li class="visible-sm-inline-block visible-xs-inline-block">
<a title="Search" aria-label="Search" data-toggle="tooltip" data-placement="bottom" data-container="body" href="/search"><i aria-hidden="true" data-hidden="true" class="fa fa-search"></i>
</a></li>
<li class="user-counter">
<a title="Issues" class="dashboard-shortcuts-issues" aria-label="Issues" data-toggle="tooltip" data-placement="bottom" data-container="body" href="/dashboard/issues?assignee_id=1228399"><svg xmlns="http://www.w3.org/2000/svg" width="16" height="16" viewBox="0 0 16 16"><path d="M10.458 15.012l.311.055a3 3 0 0 0 3.476-2.433l1.389-7.879A3 3 0 0 0 13.2 1.28L11.23.933a3.002 3.002 0 0 0-.824-.031c.364.59.58 1.28.593 2.02l1.854.328a1 1 0 0 1 .811 1.158l-1.389 7.879a1 1 0 0 1-1.158.81l-.118-.02a3.98 3.98 0 0 1-.541 1.935zM3 0h4a3 3 0 0 1 3 3v10a3 3 0 0 1-3 3H3a3 3 0 0 1-3-3V3a3 3 0 0 1 3-3zm0 2a1 1 0 0 0-1 1v10a1 1 0 0 0 1 1h4a1 1 0 0 0 1-1V3a1 1 0 0 0-1-1H3z"/></svg>

<span class="badge hidden issues-count">
0
</span>
</a></li>
<li class="user-counter">
<a title="Merge requests" class="dashboard-shortcuts-merge_requests" aria-label="Merge requests" data-toggle="tooltip" data-placement="bottom" data-container="body" href="/dashboard/merge_requests?assignee_id=1228399"><svg xmlns="http://www.w3.org/2000/svg" height="16" width="16" viewBox="0 0 16 16"><path d="m5 5.563v4.875c1.024.4 1.75 1.397 1.75 2.563 0 1.519-1.231 2.75-2.75 2.75-1.519 0-2.75-1.231-2.75-2.75 0-1.166.726-2.162 1.75-2.563v-4.875c-1.024-.4-1.75-1.397-1.75-2.563 0-1.519 1.231-2.75 2.75-2.75 1.519 0 2.75 1.231 2.75 2.75 0 1.166-.726 2.162-1.75 2.563m-1 8.687c.69 0 1.25-.56 1.25-1.25 0-.69-.56-1.25-1.25-1.25-.69 0-1.25.56-1.25 1.25 0 .69.56 1.25 1.25 1.25m0-10c.69 0 1.25-.56 1.25-1.25 0-.69-.56-1.25-1.25-1.25-.69 0-1.25.56-1.25 1.25 0 .69.56 1.25 1.25 1.25"/><path d="m10.501 2c1.381.001 2.499 1.125 2.499 2.506v5.931c1.024.4 1.75 1.397 1.75 2.563 0 1.519-1.231 2.75-2.75 2.75-1.519 0-2.75-1.231-2.75-2.75 0-1.166.726-2.162 1.75-2.563v-5.931c0-.279-.225-.506-.499-.506v.926c0 .346-.244.474-.569.271l-2.952-1.844c-.314-.196-.325-.507 0-.71l2.952-1.844c.314-.196.569-.081.569.271v.93m1.499 12.25c.69 0 1.25-.56 1.25-1.25 0-.69-.56-1.25-1.25-1.25-.69 0-1.25.56-1.25 1.25 0 .69.56 1.25 1.25 1.25"/></svg>

<span class="badge hidden merge-requests-count">
0
</span>
</a></li>
<li class="user-counter">
<a title="Todos" aria-label="Todos" class="shortcuts-todos" data-toggle="tooltip" data-placement="bottom" data-container="body" href="/dashboard/todos"><svg xmlns="http://www.w3.org/2000/svg" width="16" height="16" viewBox="0 0 16 16"><path d="M8.243 7.485l4.95-4.95a1 1 0 1 1 1.414 1.415L8.95 9.607a.997.997 0 0 1-1.414 0l-2.83-2.83a1 1 0 0 1 1.415-1.413l2.123 2.12zM12 11a1 1 0 0 1 2 0v2a3 3 0 0 1-3 3H3a3 3 0 0 1-3-3V5a3 3 0 0 1 3-3h2a1 1 0 1 1 0 2H3a1 1 0 0 0-1 1v8a1 1 0 0 0 1 1h8a1 1 0 0 0 1-1v-2z"/></svg>

<span class="badge hidden todos-count">
0
</span>
</a></li>
<li class="header-user dropdown">
<a class="header-user-dropdown-toggle" data-toggle="dropdown" href="/rajones"><img width="23" height="23" class="header-user-avatar lazy" data-src="https://secure.gravatar.com/avatar/ccec7695c9067b41ae74a273cb4a04af?s=46&amp;d=identicon" src="data:image/gif;base64,R0lGODlhAQABAAAAACH5BAEKAAEALAAAAAABAAEAAAICTAEAOw==" />
<svg xmlns="http://www.w3.org/2000/svg" width="16" height="16" class="caret-down" viewBox="0 0 16 16"><path fill-rule="evenodd" d="M8 10.243l-4.95-4.95a1 1 0 0 0-1.414 1.414l5.657 5.657a.997.997 0 0 0 1.414 0l5.657-5.657a1 1 0 0 0-1.414-1.414L8 10.243z"/></svg>

</a><div class="dropdown-menu-nav dropdown-menu-align-right">
<ul>
<li class="current-user">
<div class="user-name bold">
Richard Jones
</div>
@rajones
</li>
<li class="divider"></li>
<li>
<a class="profile-link" data-user="rajones" href="/rajones">Profile</a>
</li>
<li>
<a href="/profile">Settings</a>
</li>
<li>
<a href="/help">Help</a>
</li>
<li class="divider"></li>
<li>
<a class="sign-out-link" rel="nofollow" data-method="delete" href="/users/sign_out">Sign out</a>
</li>
</ul>
</div>
</li>
</ul>
</div>
<button class="navbar-toggle hidden-sm hidden-md hidden-lg" type="button">
<span class="sr-only">Toggle navigation</span>
<i aria-hidden="true" data-hidden="true" class="fa fa-ellipsis-v js-navbar-toggle-right"></i>
<i aria-hidden="true" data-hidden="true" class="fa fa-times js-navbar-toggle-left"></i>
</button>
</div>
</div>
</header>


<div class="page-with-new-sidebar page-with-sidebar">
<div class="nav-sidebar">
<div class="nav-sidebar-inner-scroll">
<div class="context-header">
<a title="ckan" href="/smartcolumbus-ide/dataportal/ckan"><div class="avatar-container s40 project-avatar">
<div class="avatar s40 avatar-tile identicon" style="background-color: #E3F2FD; color: #555">C</div>
</div>
<div class="sidebar-context-title">
ckan
</div>
</a></div>
<ul class="sidebar-top-level-items">
<li class="home"><a class="shortcuts-project" aria-label="Project overview" href="/smartcolumbus-ide/dataportal/ckan"><div class="nav-icon-container">
<svg xmlns="http://www.w3.org/2000/svg" width="16" height="16" viewBox="0 0 16 16"><path d="M8.462 2.177l-.038.044a.505.505 0 0 0 .038-.044zm-.787 0a.5.5 0 0 0 .038.043l-.038-.043zM3.706 7h8.725L8.069 2.585 3.706 7zM7 13.369V12a1 1 0 0 1 2 0v1.369h3V9H4v4.369h3zM14 9v4.836c0 .833-.657 1.533-1.5 1.533h-9c-.843 0-1.5-.7-1.5-1.533V9h-.448a1.1 1.1 0 0 1-.783-1.873L6.934.887a1.5 1.5 0 0 1 2.269 0l6.165 6.24A1.1 1.1 0 0 1 14.585 9H14z"/></svg>

</div>
<span class="nav-item-name">
Overview
</span>
</a><ul class="sidebar-sub-level-items">
<li class="fly-out-top-item"><a href="/smartcolumbus-ide/dataportal/ckan"><strong class="fly-out-top-item-name">
Overview
</strong>
</a></li><li class="divider fly-out-top-item"></li>
<li class=""><a title="Project details" class="shortcuts-project" href="/smartcolumbus-ide/dataportal/ckan"><span>Details</span>
</a></li><li class=""><a title="Activity" class="shortcuts-project-activity" href="/smartcolumbus-ide/dataportal/ckan/activity"><span>Activity</span>
</a></li><li class=""><a title="Cycle Analytics" class="shortcuts-project-cycle-analytics" href="/smartcolumbus-ide/dataportal/ckan/cycle_analytics"><span>Cycle Analytics</span>
</a></li></ul>
</li><li class="active"><a class="shortcuts-tree" aria-label="Repository" href="/smartcolumbus-ide/dataportal/ckan/tree/master"><div class="nav-icon-container">
<svg xmlns="http://www.w3.org/2000/svg" width="16" height="16" viewBox="0 0 16 16"><path d="M8 2H5a2 2 0 0 0-2 2v8a2 2 0 0 0 2 2h6a2 2 0 0 0 2-2V7h-3a2 2 0 0 1-2-2V2zm2 .414V5h2.586L10 2.414zM5 0h4.586A2 2 0 0 1 11 .586L14.414 4A2 2 0 0 1 15 5.414V12a4 4 0 0 1-4 4H5a4 4 0 0 1-4-4V4a4 4 0 0 1 4-4zm.5 11h5a.5.5 0 1 1 0 1h-5a.5.5 0 1 1 0-1zm0-2h5a.5.5 0 1 1 0 1h-5a.5.5 0 0 1 0-1zm0-2h2a.5.5 0 0 1 0 1h-2a.5.5 0 0 1 0-1z"/></svg>

</div>
<span class="nav-item-name">
Repository
</span>
</a><ul class="sidebar-sub-level-items">
<li class="fly-out-top-item active"><a href="/smartcolumbus-ide/dataportal/ckan/tree/master"><strong class="fly-out-top-item-name">
Repository
</strong>
</a></li><li class="divider fly-out-top-item"></li>
<li class="active"><a href="/smartcolumbus-ide/dataportal/ckan/tree/master">Files
</a></li><li class=""><a href="/smartcolumbus-ide/dataportal/ckan/commits/master">Commits
</a></li><li class=""><a href="/smartcolumbus-ide/dataportal/ckan/branches">Branches
</a></li><li class=""><a href="/smartcolumbus-ide/dataportal/ckan/tags">Tags
</a></li><li class=""><a href="/smartcolumbus-ide/dataportal/ckan/graphs/master">Contributors
</a></li><li class=""><a href="/smartcolumbus-ide/dataportal/ckan/network/master">Graph
</a></li><li class=""><a href="/smartcolumbus-ide/dataportal/ckan/compare?from=master&amp;to=master">Compare
</a></li><li class=""><a href="/smartcolumbus-ide/dataportal/ckan/graphs/master/charts">Charts
</a></li><li class=""><a href="/smartcolumbus-ide/dataportal/ckan/path_locks">Locked Files
</a></li></ul>
</li><li class=""><a class="shortcuts-container-registry" aria-label="Container Registry" href="/smartcolumbus-ide/dataportal/ckan/container_registry"><div class="nav-icon-container">
<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 16 16"><path d="m16 11.764v-8.764c0-1.657-1.343-3-3-3h-10c-1.657 0-3 1.343-3 3v8.764c.531-.475 1.232-.764 2-.764v-8c0-.552.448-1 1-1h10c.552 0 1 .448 1 1v8c.768 0 1.469.289 2 .764m-14 .236h12c1.105 0 2 .895 2 2 0 1.105-.895 2-2 2h-12c-1.105 0-2-.895-2-2 0-1.105.895-2 2-2m10 1c-.552 0-1 .448-1 1 0 .552.448 1 1 1 .552 0 1-.448 1-1 0-.552-.448-1-1-1"/></svg>

</div>
<span class="nav-item-name">
Registry
</span>
</a><ul class="sidebar-sub-level-items is-fly-out-only">
<li class="fly-out-top-item"><a href="/smartcolumbus-ide/dataportal/ckan/container_registry"><strong class="fly-out-top-item-name">
Registry
</strong>
</a></li></ul>
</li><li class=""><a class="shortcuts-issues" aria-label="Issues" href="/smartcolumbus-ide/dataportal/ckan/issues"><div class="nav-icon-container">
<svg xmlns="http://www.w3.org/2000/svg" width="16" height="16" viewBox="0 0 16 16"><path d="M10.458 15.012l.311.055a3 3 0 0 0 3.476-2.433l1.389-7.879A3 3 0 0 0 13.2 1.28L11.23.933a3.002 3.002 0 0 0-.824-.031c.364.59.58 1.28.593 2.02l1.854.328a1 1 0 0 1 .811 1.158l-1.389 7.879a1 1 0 0 1-1.158.81l-.118-.02a3.98 3.98 0 0 1-.541 1.935zM3 0h4a3 3 0 0 1 3 3v10a3 3 0 0 1-3 3H3a3 3 0 0 1-3-3V3a3 3 0 0 1 3-3zm0 2a1 1 0 0 0-1 1v10a1 1 0 0 0 1 1h4a1 1 0 0 0 1-1V3a1 1 0 0 0-1-1H3z"/></svg>

</div>
<span class="nav-item-name">
Issues
</span>
<span class="badge count issue_counter">
0
</span>
</a><ul class="sidebar-sub-level-items">
<li class="fly-out-top-item"><a href="/smartcolumbus-ide/dataportal/ckan/issues"><strong class="fly-out-top-item-name">
Issues
</strong>
<span class="badge count issue_counter fly-out-badge">
0
</span>
</a></li><li class="divider fly-out-top-item"></li>
<li class=""><a title="Issues" href="/smartcolumbus-ide/dataportal/ckan/issues"><span>
List
</span>
</a></li><li class=""><a title="Boards" href="/smartcolumbus-ide/dataportal/ckan/boards"><span>
Boards
</span>
</a></li><li class=""><a title="Labels" href="/smartcolumbus-ide/dataportal/ckan/labels"><span>
Labels
</span>
</a></li><li class=""><a title="Service Desk" href="/smartcolumbus-ide/dataportal/ckan/issues/service_desk"><span>Service Desk</span>
</a></li><li class=""><a title="Milestones" href="/smartcolumbus-ide/dataportal/ckan/milestones"><span>
Milestones
</span>
</a></li></ul>
</li><li class=""><a class="shortcuts-merge_requests" aria-label="Merge Requests" href="/smartcolumbus-ide/dataportal/ckan/merge_requests"><div class="nav-icon-container">
<svg xmlns="http://www.w3.org/2000/svg" height="16" width="16" viewBox="0 0 16 16"><path d="m5 5.563v4.875c1.024.4 1.75 1.397 1.75 2.563 0 1.519-1.231 2.75-2.75 2.75-1.519 0-2.75-1.231-2.75-2.75 0-1.166.726-2.162 1.75-2.563v-4.875c-1.024-.4-1.75-1.397-1.75-2.563 0-1.519 1.231-2.75 2.75-2.75 1.519 0 2.75 1.231 2.75 2.75 0 1.166-.726 2.162-1.75 2.563m-1 8.687c.69 0 1.25-.56 1.25-1.25 0-.69-.56-1.25-1.25-1.25-.69 0-1.25.56-1.25 1.25 0 .69.56 1.25 1.25 1.25m0-10c.69 0 1.25-.56 1.25-1.25 0-.69-.56-1.25-1.25-1.25-.69 0-1.25.56-1.25 1.25 0 .69.56 1.25 1.25 1.25"/><path d="m10.501 2c1.381.001 2.499 1.125 2.499 2.506v5.931c1.024.4 1.75 1.397 1.75 2.563 0 1.519-1.231 2.75-2.75 2.75-1.519 0-2.75-1.231-2.75-2.75 0-1.166.726-2.162 1.75-2.563v-5.931c0-.279-.225-.506-.499-.506v.926c0 .346-.244.474-.569.271l-2.952-1.844c-.314-.196-.325-.507 0-.71l2.952-1.844c.314-.196.569-.081.569.271v.93m1.499 12.25c.69 0 1.25-.56 1.25-1.25 0-.69-.56-1.25-1.25-1.25-.69 0-1.25.56-1.25 1.25 0 .69.56 1.25 1.25 1.25"/></svg>

</div>
<span class="nav-item-name">
Merge Requests
</span>
<span class="badge count merge_counter js-merge-counter">
0
</span>
</a><ul class="sidebar-sub-level-items is-fly-out-only">
<li class="fly-out-top-item"><a href="/smartcolumbus-ide/dataportal/ckan/merge_requests"><strong class="fly-out-top-item-name">
Merge Requests
</strong>
<span class="badge count merge_counter js-merge-counter fly-out-badge">
0
</span>
</a></li></ul>
</li><li class=""><a class="shortcuts-pipelines" aria-label="CI / CD" href="/smartcolumbus-ide/dataportal/ckan/pipelines"><div class="nav-icon-container">
<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 16 16" enable-background="new 0 0 16 16"><path d="m8 0c-4.4 0-8 3.6-8 8s3.6 8 8 8 8-3.6 8-8-3.6-8-8-8m0 14c-3.3 0-6-2.7-6-6s2.7-6 6-6 6 2.7 6 6-2.7 6-6 6"/><circle cx="12.5" cy="9.5" r=".5"/><circle cx="12.5" cy="6.5" r=".5"/><circle cx="10.5" cy="12.5" r=".5"/><circle cx="10.5" cy="3.5" r=".5"/><circle cx="5.5" cy="12.5" r=".5"/><circle cx="5.5" cy="3.5" r=".5"/><circle cx="3.5" cy="9.5" r=".5"/><circle cx="3.5" cy="6.5" r=".5"/><path d="m9 7.2c0 0 0-.1 0-.2v-1.9c0-.1 0-.1-.1-.2l-.8-.8c0 0-.1 0-.1 0l-.9.8c-.1.1-.1.1-.1.2v1.9c0 .1 0 .2 0 .2-.6.4-1 1-1 1.8 0 1.1.9 2 2 2s2-.9 2-2c0-.8-.4-1.4-1-1.8m-1 2.8c-.6 0-1-.4-1-1s.4-1 1-1 1 .4 1 1-.4 1-1 1"/></svg>

</div>
<span class="nav-item-name">
CI / CD
</span>
</a><ul class="sidebar-sub-level-items">
<li class="fly-out-top-item"><a href="/smartcolumbus-ide/dataportal/ckan/pipelines"><strong class="fly-out-top-item-name">
CI / CD
</strong>
</a></li><li class="divider fly-out-top-item"></li>
<li class=""><a title="Pipelines" class="shortcuts-pipelines" href="/smartcolumbus-ide/dataportal/ckan/pipelines"><span>
Pipelines
</span>
</a></li><li class=""><a title="Jobs" class="shortcuts-builds" href="/smartcolumbus-ide/dataportal/ckan/-/jobs"><span>
Jobs
</span>
</a></li><li class=""><a title="Schedules" class="shortcuts-builds" href="/smartcolumbus-ide/dataportal/ckan/pipeline_schedules"><span>
Schedules
</span>
</a></li><li class=""><a title="Environments" class="shortcuts-environments" href="/smartcolumbus-ide/dataportal/ckan/environments"><span>
Environments
</span>
</a></li><li class=""><a title="Charts" class="shortcuts-pipelines-charts" href="/smartcolumbus-ide/dataportal/ckan/pipelines/charts"><span>
Charts
</span>
</a></li></ul>
</li><li class=""><a class="shortcuts-wiki" aria-label="Wiki" href="/smartcolumbus-ide/dataportal/ckan/wikis/home"><div class="nav-icon-container">
<svg xmlns="http://www.w3.org/2000/svg" width="16" height="16" viewBox="0 0 16 16"><path d="M8 2H4a1 1 0 0 0-1 1v10a1 1 0 0 0 1 1h8a1 1 0 0 0 1-1V3a1 1 0 0 0-1-1v4.191a.5.5 0 0 1-.724.447l-1.052-.526a.5.5 0 0 0-.448 0l-1.052.526A.5.5 0 0 1 8 6.191V2zM4 0h8a3 3 0 0 1 3 3v10a3 3 0 0 1-3 3H4a3 3 0 0 1-3-3V3a3 3 0 0 1 3-3z"/></svg>

</div>
<span class="nav-item-name">
Wiki
</span>
</a><ul class="sidebar-sub-level-items is-fly-out-only">
<li class="fly-out-top-item"><a href="/smartcolumbus-ide/dataportal/ckan/wikis/home"><strong class="fly-out-top-item-name">
Wiki
</strong>
</a></li></ul>
</li><li class=""><a class="shortcuts-snippets" aria-label="Snippets" href="/smartcolumbus-ide/dataportal/ckan/snippets"><div class="nav-icon-container">
<svg xmlns="http://www.w3.org/2000/svg" width="16" height="16" viewBox="0 0 16 16"><path d="M10.67 9.31a3.001 3.001 0 0 1 2.062 5.546 3 3 0 0 1-3.771-4.559 1.007 1.007 0 0 1-.095-.137l-4.5-7.794a1 1 0 1 1 1.732-1l4.5 7.794c.028.05.052.1.071.15zm-3.283.35l-.289.5c-.028.05-.06.095-.095.137a3.001 3.001 0 0 1-3.77 4.56A3 3 0 0 1 5.294 9.31c.02-.051.043-.102.071-.15l.866-1.5 1.155 2zm2.31-4l-1.156-2 1.325-2.294a1 1 0 1 1 1.732 1L9.696 5.66zm-5.465 7.464a1 1 0 1 0 1-1.732 1 1 0 0 0-1 1.732zm7.5 0a1 1 0 1 0-1-1.732 1 1 0 0 0 1 1.732z"/></svg>

</div>
<span class="nav-item-name">
Snippets
</span>
</a><ul class="sidebar-sub-level-items is-fly-out-only">
<li class="fly-out-top-item"><a href="/smartcolumbus-ide/dataportal/ckan/snippets"><strong class="fly-out-top-item-name">
Snippets
</strong>
</a></li></ul>
</li><li class=""><a class="shortcuts-tree" aria-label="Settings" href="/smartcolumbus-ide/dataportal/ckan/edit"><div class="nav-icon-container">
<svg xmlns="http://www.w3.org/2000/svg" width="16" height="16" viewBox="0 0 16 16"><path fill-rule="evenodd" d="M2.415 5.803L1.317 4.084A.5.5 0 0 1 1.35 3.5l.805-.994a.5.5 0 0 1 .564-.153l1.878.704a5.975 5.975 0 0 1 1.65-.797L6.885.342A.5.5 0 0 1 7.36 0h1.28a.5.5 0 0 1 .474.342l.639 1.918c.594.181 1.15.452 1.65.797l1.877-.704a.5.5 0 0 1 .565.153l.805.994a.5.5 0 0 1 .032.584l-1.097 1.719c.217.551.354 1.143.399 1.76l1.731 1.058a.5.5 0 0 1 .227.54l-.288 1.246a.5.5 0 0 1-.44.385l-2.008.19a6.026 6.026 0 0 1-1.142 1.431l.265 1.995a.5.5 0 0 1-.277.516l-1.15.56a.5.5 0 0 1-.576-.1l-1.424-1.452a6.047 6.047 0 0 1-1.804 0l-1.425 1.453a.5.5 0 0 1-.576.1l-1.15-.561a.5.5 0 0 1-.276-.516l.265-1.995a6.026 6.026 0 0 1-1.143-1.43l-2.008-.191a.5.5 0 0 1-.44-.385L.058 9.16a.5.5 0 0 1 .226-.539l1.732-1.058a5.968 5.968 0 0 1 .399-1.76zM8 11a3 3 0 1 0 0-6 3 3 0 0 0 0 6z"/></svg>

</div>
<span class="nav-item-name">
Settings
</span>
</a><ul class="sidebar-sub-level-items">
<li class="fly-out-top-item"><a href="/smartcolumbus-ide/dataportal/ckan/edit"><strong class="fly-out-top-item-name">
Settings
</strong>
</a></li><li class="divider fly-out-top-item"></li>
<li class=""><a title="General" href="/smartcolumbus-ide/dataportal/ckan/edit"><span>
General
</span>
</a></li><li class=""><a title="Members" href="/smartcolumbus-ide/dataportal/ckan/project_members"><span>
Members
</span>
</a></li><li class=""><a title="Integrations" href="/smartcolumbus-ide/dataportal/ckan/settings/integrations"><span>
Integrations
</span>
</a></li><li class=""><a title="Repository" href="/smartcolumbus-ide/dataportal/ckan/settings/repository"><span>
Repository
</span>
</a></li><li class=""><a title="CI / CD" href="/smartcolumbus-ide/dataportal/ckan/settings/ci_cd"><span>
CI / CD
</span>
</a></li><li class=""><a title="Audit Events" href="/smartcolumbus-ide/dataportal/ckan/audit_events"><span>
Audit Events
</span>
</a></li>
</ul>
</li><a class="toggle-sidebar-button js-toggle-sidebar" role="button" title="Toggle sidebar" type="button">
<i aria-hidden="true" data-hidden="true" class="fa fa-angle-double-left"></i>
<i aria-hidden="true" data-hidden="true" class="fa fa-angle-double-right"></i>
<span class="collapse-text">Collapse sidebar</span>
</a>
<button name="button" type="button" class="close-nav-button"><i aria-hidden="true" data-hidden="true" class="fa fa-times"></i>
<span class="collapse-text">Close sidebar</span>
</button>
<li class="hidden">
<a title="Activity" class="shortcuts-project-activity" href="/smartcolumbus-ide/dataportal/ckan/activity"><span>
Activity
</span>
</a></li>
<li class="hidden">
<a title="Network" class="shortcuts-network" href="/smartcolumbus-ide/dataportal/ckan/network/master">Graph
</a></li>
<li class="hidden">
<a title="Charts" class="shortcuts-repository-charts" href="/smartcolumbus-ide/dataportal/ckan/graphs/master/charts">Charts
</a></li>
<li class="hidden">
<a class="shortcuts-new-issue" href="/smartcolumbus-ide/dataportal/ckan/issues/new">Create a new issue
</a></li>
<li class="hidden">
<a title="Jobs" class="shortcuts-builds" href="/smartcolumbus-ide/dataportal/ckan/-/jobs">Jobs
</a></li>
<li class="hidden">
<a title="Commits" class="shortcuts-commits" href="/smartcolumbus-ide/dataportal/ckan/commits/master">Commits
</a></li>
<li class="hidden">
<a title="Issue Boards" class="shortcuts-issue-boards" href="/smartcolumbus-ide/dataportal/ckan/boards">Issue Boards</a>
</li>
</ul>
</div>
</div>

<div class="content-wrapper page-with-new-nav">
<div class="mobile-overlay"></div>
<div class="alert-wrapper">


<nav class="breadcrumbs container-fluid container-limited" role="navigation">
<div class="breadcrumbs-container">
<button name="button" type="button" class="toggle-mobile-nav"><span class="sr-only">Open sidebar</span>
<i aria-hidden="true" data-hidden="true" class="fa fa-bars"></i>
</button><div class="breadcrumbs-links js-title-container">
<ul class="list-unstyled breadcrumbs-list js-breadcrumbs-list">
<li><a class="group-path breadcrumb-item-text js-breadcrumb-item-text " href="/smartcolumbus-ide">smartcolumbus-ide</a><i aria-hidden="true" data-hidden="true" class="fa fa-angle-right breadcrumbs-list-angle"></i></li><li><a class="group-path breadcrumb-item-text js-breadcrumb-item-text " href="/smartcolumbus-ide/dataportal">dataportal</a><i aria-hidden="true" data-hidden="true" class="fa fa-angle-right breadcrumbs-list-angle"></i></li> <li><a href="/smartcolumbus-ide/dataportal/ckan"><span class="breadcrumb-item-text js-breadcrumb-item-text">ckan</span></a><i aria-hidden="true" data-hidden="true" class="fa fa-angle-right breadcrumbs-list-angle"></i></li>

<li>
<h2 class="breadcrumbs-sub-title">Repository</h2>
</li>
</ul>
</div>

</div>
</nav>

<div class="flash-container flash-container-page">
</div>

</div>
<div class=" ">
<div class="content" id="content-body">


<div class="container-fluid container-limited">
<div class="tree-holder" id="tree-holder">
<div class="nav-block">
<div class="tree-ref-container">
<div class="tree-ref-holder">
<form class="project-refs-form" action="/smartcolumbus-ide/dataportal/ckan/refs/switch" accept-charset="UTF-8" method="get"><input name="utf8" type="hidden" value="&#x2713;" /><input type="hidden" name="destination" id="destination" value="blob" />
<input type="hidden" name="path" id="path" value="usr/lib/ckan/default/src/ckan/sc_datasets2.sh" />
<div class="dropdown">
<button class="dropdown-menu-toggle js-project-refs-dropdown" type="button" data-toggle="dropdown" data-selected="master" data-ref="master" data-refs-url="/smartcolumbus-ide/dataportal/ckan/refs" data-field-name="ref" data-submit-form-on-click="true" data-visit="true"><span class="dropdown-toggle-text ">master</span><i aria-hidden="true" data-hidden="true" class="fa fa-chevron-down"></i></button>
<div class="dropdown-menu dropdown-menu-selectable git-revision-dropdown">
<div class="dropdown-title"><span>Switch branch/tag</span><button class="dropdown-title-button dropdown-menu-close" aria-label="Close" type="button"><i aria-hidden="true" data-hidden="true" class="fa fa-times dropdown-menu-close-icon"></i></button></div>
<div class="dropdown-input"><input type="search" id="" class="dropdown-input-field" placeholder="Search branches and tags" autocomplete="off" /><i aria-hidden="true" data-hidden="true" class="fa fa-search dropdown-input-search"></i><i role="button" aria-hidden="true" data-hidden="true" class="fa fa-times dropdown-input-clear js-dropdown-input-clear"></i></div>
<div class="dropdown-content"></div>
<div class="dropdown-loading"><i aria-hidden="true" data-hidden="true" class="fa fa-spinner fa-spin"></i></div>
</div>
</div>
</form>
</div>
<ul class="breadcrumb repo-breadcrumb">
<li>
<a href="/smartcolumbus-ide/dataportal/ckan/tree/master">ckan
</a></li>
<li>
<a href="/smartcolumbus-ide/dataportal/ckan/tree/master/usr/lib/ckan/default/src">..</a>
</li>
<li>
<a href="/smartcolumbus-ide/dataportal/ckan/tree/master/usr/lib/ckan">ckan</a>
</li>
<li>
<a href="/smartcolumbus-ide/dataportal/ckan/tree/master/usr/lib/ckan/default/src/ckan">ckan</a>
</li>
<li>
<a href="/smartcolumbus-ide/dataportal/ckan/blob/master/usr/lib/ckan/default/src/ckan/sc_datasets2.sh"><strong>sc_datasets2.sh</strong>
</a></li>
</ul>
</div>
<div class="tree-controls">
<a class="btn shortcuts-find-file" rel="nofollow" href="/smartcolumbus-ide/dataportal/ckan/find_file/master"><i aria-hidden="true" data-hidden="true" class="fa fa-search"></i>
<span>Find file</span>
</a>
<div class="btn-group" role="group"><a class="btn js-blob-blame-link" href="/smartcolumbus-ide/dataportal/ckan/blame/master/usr/lib/ckan/default/src/ckan/sc_datasets2.sh">Blame</a><a class="btn" href="/smartcolumbus-ide/dataportal/ckan/commits/master/usr/lib/ckan/default/src/ckan/sc_datasets2.sh">History</a><a class="btn js-data-file-blob-permalink-url" href="/smartcolumbus-ide/dataportal/ckan/blob/8ed2de44a069f391e74c357912d8678a23938ff2/usr/lib/ckan/default/src/ckan/sc_datasets2.sh">Permalink</a></div>
</div>
</div>

<div class="info-well hidden-xs">
<div class="well-segment">
<ul class="blob-commit-info">
<li class="commit flex-row js-toggle-container" id="commit-a348cc4f">
<div class="avatar-cell hidden-xs">
<a href="/rajones"><img class="avatar s36 hidden-xs has-tooltip  lazy" alt="Richard Jones&#39;s avatar" title="Richard Jones" data-container="body" data-src="https://secure.gravatar.com/avatar/ccec7695c9067b41ae74a273cb4a04af?s=72&amp;d=identicon" src="data:image/gif;base64,R0lGODlhAQABAAAAACH5BAEKAAEALAAAAAABAAEAAAICTAEAOw==" /></a>
</div>
<div class="commit-detail">
<div class="commit-content">
<a class="commit-row-message item-title" href="/smartcolumbus-ide/dataportal/ckan/commit/a348cc4f9d4fea5d8c10d7fb94fb7da8ff9e1aca">Upload New File - Adds custom tags to harvested datasets from a defined list.</a>
<span class="commit-row-message visible-xs-inline">
&middot;
a348cc4f
</span>
<div class="commiter">
<a class="commit-author-link has-tooltip" title="rajones@hntb.com" href="/rajones">Richard Jones</a> committed <time class="js-timeago" title="Aug 29, 2017 7:09pm" datetime="2017-08-29T19:09:24Z" data-toggle="tooltip" data-placement="top" data-container="body">Aug 29, 2017</time>
</div>
</div>
<div class="commit-actions hidden-xs">

<a class="commit-sha btn btn-transparent" href="/smartcolumbus-ide/dataportal/ckan/commit/a348cc4f9d4fea5d8c10d7fb94fb7da8ff9e1aca">a348cc4f</a>
<button class="btn btn-clipboard btn-transparent" data-toggle="tooltip" data-placement="bottom" data-container="body" data-title="Copy commit SHA to clipboard" data-clipboard-text="a348cc4f9d4fea5d8c10d7fb94fb7da8ff9e1aca" type="button" title="Copy commit SHA to clipboard" aria-label="Copy commit SHA to clipboard"><i aria-hidden="true" aria-hidden="true" data-hidden="true" class="fa fa-clipboard"></i></button>

</div>
</div>
</li>

</ul>
</div>

</div>
<div class="blob-content-holder" id="blob-content-holder">
<article class="file-holder">
<div class="js-file-title file-title-flex-parent">
<div class="file-header-content">
<i aria-hidden="true" data-hidden="true" class="fa fa-file-text-o fa-fw"></i>
<strong class="file-title-name">
sc_datasets2.sh
</strong>
<button class="btn btn-clipboard btn-transparent prepend-left-5" data-toggle="tooltip" data-placement="bottom" data-container="body" data-class="btn-clipboard btn-transparent prepend-left-5" data-title="Copy file path to clipboard" data-clipboard-text="{&quot;text&quot;:&quot;usr/lib/ckan/default/src/ckan/sc_datasets2.sh&quot;,&quot;gfm&quot;:&quot;`usr/lib/ckan/default/src/ckan/sc_datasets2.sh`&quot;}" type="button" title="Copy file path to clipboard" aria-label="Copy file path to clipboard"><i aria-hidden="true" aria-hidden="true" data-hidden="true" class="fa fa-clipboard"></i></button>
<small>
1.16 KB
</small>
</div>

<div class="file-actions hidden-xs">

<div class="btn-group" role="group"><button class="btn btn btn-sm js-copy-blob-source-btn" data-toggle="tooltip" data-placement="bottom" data-container="body" data-class="btn btn-sm js-copy-blob-source-btn" data-title="Copy source to clipboard" data-clipboard-target=".blob-content[data-blob-id=&#39;94466a02397985f7c9533e2322582c7a67976ab8&#39;]" type="button" title="Copy source to clipboard" aria-label="Copy source to clipboard"><i aria-hidden="true" aria-hidden="true" data-hidden="true" class="fa fa-clipboard"></i></button><a class="btn btn-sm has-tooltip" target="_blank" rel="noopener noreferrer" title="Open raw" data-container="body" href="/smartcolumbus-ide/dataportal/ckan/raw/master/usr/lib/ckan/default/src/ckan/sc_datasets2.sh"><i aria-hidden="true" data-hidden="true" class="fa fa-file-code-o"></i></a></div>
<div class="btn-group" role="group"><a class="btn btn-sm path-lock has-tooltip" data-state="lock" data-toggle="tooltip" title="" href="#">Lock</a><a class="btn js-edit-blob  btn-sm" href="/smartcolumbus-ide/dataportal/ckan/edit/master/usr/lib/ckan/default/src/ckan/sc_datasets2.sh">Edit</a><button name="button" type="submit" class="btn btn-default" data-target="#modal-upload-blob" data-toggle="modal">Replace</button><button name="button" type="submit" class="btn btn-remove" data-target="#modal-remove-blob" data-toggle="modal">Delete</button></div>
</div>
</div>
<div class="js-file-fork-suggestion-section file-fork-suggestion hidden">
<span class="file-fork-suggestion-note">
You're not allowed to
<span class="js-file-fork-suggestion-section-action">
edit
</span>
files in this project directly. Please fork this project,
make your changes there, and submit a merge request.
</span>
<a class="js-fork-suggestion-button btn btn-grouped btn-inverted btn-new" rel="nofollow" data-method="post" href="/smartcolumbus-ide/dataportal/ckan/blob/master/usr/lib/ckan/default/src/ckan/sc_datasets2.sh">Fork</a>
<button class="js-cancel-fork-suggestion-button btn btn-grouped" type="button">
Cancel
</button>
</div>

<script id="js-file-lock" type="application/json">
{"path":"usr/lib/ckan/default/src/ckan/sc_datasets2.sh","toggle_path":"/smartcolumbus-ide/dataportal/ckan/path_locks/toggle"}
</script>

<div class="blob-viewer" data-type="simple" data-url="/smartcolumbus-ide/dataportal/ckan/blob/master/usr/lib/ckan/default/src/ckan/sc_datasets2.sh?format=json&amp;viewer=simple">
<div class="text-center prepend-top-default append-bottom-default">
<i aria-hidden="true" aria-label="Loading content…" class="fa fa-spinner fa-spin fa-2x"></i>
</div>

</div>


</article>
</div>

</div>
<div class="modal" id="modal-remove-blob">
<div class="modal-dialog">
<div class="modal-content">
<div class="modal-header">
<a class="close" data-dismiss="modal" href="#">×</a>
<h3 class="page-title">Delete sc_datasets2.sh</h3>
</div>
<div class="modal-body">
<form class="form-horizontal js-delete-blob-form js-quick-submit js-requires-input" action="/smartcolumbus-ide/dataportal/ckan/blob/master/usr/lib/ckan/default/src/ckan/sc_datasets2.sh" accept-charset="UTF-8" method="post"><input name="utf8" type="hidden" value="&#x2713;" /><input type="hidden" name="_method" value="delete" /><input type="hidden" name="authenticity_token" value="Zuki9Uc34khzbftLkLtwXAsB/uL4nB3UpvQp4vtiG40xbFB7Bs71mYoAt8wpMjXDJRnCFowngMSDuEnQIjzzNw==" /><div class="form-group commit_message-group">
<label class="control-label" for="commit_message-9dc398148dc00e4586f0291f28865f81">Commit message
</label><div class="col-sm-10">
<div class="commit-message-container">
<div class="max-width-marker"></div>
<textarea name="commit_message" id="commit_message-9dc398148dc00e4586f0291f28865f81" class="form-control js-commit-message" placeholder="Delete sc_datasets2.sh" required="required" rows="3">
Delete sc_datasets2.sh</textarea>
</div>
</div>
</div>

<div class="form-group branch">
<label class="control-label" for="branch_name">Target Branch</label>
<div class="col-sm-10">
<input type="text" name="branch_name" id="branch_name" value="master" required="required" class="form-control js-branch-name ref-name" />
<div class="js-create-merge-request-container">
<div class="checkbox">
<label for="create_merge_request-da86efeaa037a21315988c4be478d915"><input type="checkbox" name="create_merge_request" id="create_merge_request-da86efeaa037a21315988c4be478d915" value="1" class="js-create-merge-request" checked="checked" />
Start a <strong>new merge request</strong> with these changes
</label></div>

</div>
</div>
</div>
<input type="hidden" name="original_branch" id="original_branch" value="master" class="js-original-branch" />

<div class="form-group">
<div class="col-sm-offset-2 col-sm-10">
<button name="button" type="submit" class="btn btn-remove btn-remove-file">Delete file</button>
<a class="btn btn-cancel" data-dismiss="modal" href="#">Cancel</a>
</div>
</div>
</form></div>
</div>
</div>
</div>

<div class="modal" id="modal-upload-blob">
<div class="modal-dialog">
<div class="modal-content">
<div class="modal-header">
<a class="close" data-dismiss="modal" href="#">×</a>
<h3 class="page-title">Replace sc_datasets2.sh</h3>
</div>
<div class="modal-body">
<form class="js-quick-submit js-upload-blob-form form-horizontal" data-method="put" action="/smartcolumbus-ide/dataportal/ckan/update/master/usr/lib/ckan/default/src/ckan/sc_datasets2.sh" accept-charset="UTF-8" method="post"><input name="utf8" type="hidden" value="&#x2713;" /><input type="hidden" name="_method" value="put" /><input type="hidden" name="authenticity_token" value="ACL1irrxDOBqVGwKGB5S2aBbYSbbvvU7UA123Jeayv9Xp4cE+wgbMZM5II2hlxdGjkNd0q8FaCt1QRbuTsQiRQ==" /><div class="dropzone">
<div class="dropzone-previews blob-upload-dropzone-previews">
<p class="dz-message light">
Attach a file by drag &amp; drop or <a class="markdown-selector" href="#">click to upload</a>
</p>
</div>
</div>
<br>
<div class="dropzone-alerts alert alert-danger data" style="display:none"></div>
<div class="form-group commit_message-group">
<label class="control-label" for="commit_message-83823c707607eaf318f9c92984a7dd9c">Commit message
</label><div class="col-sm-10">
<div class="commit-message-container">
<div class="max-width-marker"></div>
<textarea name="commit_message" id="commit_message-83823c707607eaf318f9c92984a7dd9c" class="form-control js-commit-message" placeholder="Replace sc_datasets2.sh" required="required" rows="3">
Replace sc_datasets2.sh</textarea>
</div>
</div>
</div>

<div class="form-group branch">
<label class="control-label" for="branch_name">Target Branch</label>
<div class="col-sm-10">
<input type="text" name="branch_name" id="branch_name" value="master" required="required" class="form-control js-branch-name ref-name" />
<div class="js-create-merge-request-container">
<div class="checkbox">
<label for="create_merge_request-8ebd3eb68d6f8f482c19698f4a77431e"><input type="checkbox" name="create_merge_request" id="create_merge_request-8ebd3eb68d6f8f482c19698f4a77431e" value="1" class="js-create-merge-request" checked="checked" />
Start a <strong>new merge request</strong> with these changes
</label></div>

</div>
</div>
</div>
<input type="hidden" name="original_branch" id="original_branch" value="master" class="js-original-branch" />

<div class="form-actions">
<button name="button" type="button" class="btn btn-create btn-upload-file" id="submit-all"><i aria-hidden="true" data-hidden="true" class="fa fa-spin fa-spinner js-loading-icon hidden"></i>
Replace file
</button><a class="btn btn-cancel" data-dismiss="modal" href="#">Cancel</a>
</div>
</form></div>
</div>
</div>
</div>

</div>

</div>
</div>
</div>
</div>


</body>
</html>
