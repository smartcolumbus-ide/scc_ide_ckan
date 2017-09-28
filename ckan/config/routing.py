





<!DOCTYPE html>
<html lang="en">
  <head>
    <meta charset="utf-8">
  <link rel="dns-prefetch" href="https://assets-cdn.github.com">
  <link rel="dns-prefetch" href="https://avatars0.githubusercontent.com">
  <link rel="dns-prefetch" href="https://avatars1.githubusercontent.com">
  <link rel="dns-prefetch" href="https://avatars2.githubusercontent.com">
  <link rel="dns-prefetch" href="https://avatars3.githubusercontent.com">
  <link rel="dns-prefetch" href="https://github-cloud.s3.amazonaws.com">
  <link rel="dns-prefetch" href="https://user-images.githubusercontent.com/">



  <link crossorigin="anonymous" href="https://assets-cdn.github.com/assets/frameworks-bedfc518345498ab3204d330c1727cde7e733526a09cd7df6867f6a231565091.css" integrity="sha256-vt/FGDRUmKsyBNMwwXJ83n5zNSagnNffaGf2ojFWUJE=" media="all" rel="stylesheet" />
  <link crossorigin="anonymous" href="https://assets-cdn.github.com/assets/github-76a453a954138bb17e8b3feb0422f525074bf6718abb559d97c72c7c4a5e2a00.css" integrity="sha256-dqRTqVQTi7F+iz/rBCL1JQdL9nGKu1Wdl8csfEpeKgA=" media="all" rel="stylesheet" />
  
  
  
  

  <meta name="viewport" content="width=device-width">
  
  <title>ckan/routing.py at master · ckan/ckan</title>
  <link rel="search" type="application/opensearchdescription+xml" href="/opensearch.xml" title="GitHub">
  <link rel="fluid-icon" href="https://github.com/fluidicon.png" title="GitHub">
  <meta property="fb:app_id" content="1401488693436528">

    
    <meta content="https://avatars1.githubusercontent.com/u/1630326?v=4&amp;s=400" property="og:image" /><meta content="GitHub" property="og:site_name" /><meta content="object" property="og:type" /><meta content="ckan/ckan" property="og:title" /><meta content="https://github.com/ckan/ckan" property="og:url" /><meta content="ckan - CKAN is an open-source DMS (data management system) for powering data hubs and data portals. CKAN makes it easy to publish, share and use data. It powers datahub.io, catalog.data.gov and dat..." property="og:description" />

  <link rel="assets" href="https://assets-cdn.github.com/">
  <link rel="web-socket" href="wss://live.github.com/_sockets/VjI6MjA4MDA1MTQwOmVhNmUyMTMwZWNiMTJkZGZiZmY1OWFlY2Q4Nzg0YjZlYmFmYjg3MWFkMGVkZmUyZmJkNjI5OTNkNTgyODM1MjU=--658a46081495ca96352c12dc1bbf8439030ee828">
  <meta name="pjax-timeout" content="1000">
  <link rel="sudo-modal" href="/sessions/sudo_modal">
  <meta name="request-id" content="CA58:3858:9CFFA6:113E7F3:59CD6BCB" data-pjax-transient>
  

  <meta name="selected-link" value="repo_source" data-pjax-transient>

  <meta name="google-site-verification" content="KT5gs8h0wvaagLKAVWq8bbeNwnZZK1r1XQysX3xurLU">
<meta name="google-site-verification" content="ZzhVyEFwb7w3e0-uOTltm8Jsck2F5StVihD0exw2fsA">
    <meta name="google-analytics" content="UA-3769691-2">

<meta content="collector.githubapp.com" name="octolytics-host" /><meta content="github" name="octolytics-app-id" /><meta content="https://collector.githubapp.com/github-external/browser_event" name="octolytics-event-url" /><meta content="CA58:3858:9CFFA6:113E7F3:59CD6BCB" name="octolytics-dimension-request_id" /><meta content="iad" name="octolytics-dimension-region_edge" /><meta content="iad" name="octolytics-dimension-region_render" /><meta content="32200864" name="octolytics-actor-id" /><meta content="smartcolumbus-ide" name="octolytics-actor-login" /><meta content="fadc0d03f1a182a0cae60d9dd87d8a4b8b4144ba685678436377abeed35cb5c4" name="octolytics-actor-hash" />
<meta content="/&lt;user-name&gt;/&lt;repo-name&gt;/blob/show" data-pjax-transient="true" name="analytics-location" />




  <meta class="js-ga-set" name="dimension1" content="Logged In">


  

      <meta name="hostname" content="github.com">
  <meta name="user-login" content="smartcolumbus-ide">

      <meta name="expected-hostname" content="github.com">
    <meta name="js-proxy-site-detection-payload" content="ZjQzZWNmYTExMDFiNzAzODgxYWY5M2Q0MGVhNjIxMjczMjI3ZDUwZWYxYTk2NGI3OTdjMTBkNGJlNzI5ZTEzNHx7InJlbW90ZV9hZGRyZXNzIjoiMTYyLjIzMC4yMDYuMTIwIiwicmVxdWVzdF9pZCI6IkNBNTg6Mzg1ODo5Q0ZGQTY6MTEzRTdGMzo1OUNENkJDQiIsInRpbWVzdGFtcCI6MTUwNjYzNDY5OSwiaG9zdCI6ImdpdGh1Yi5jb20ifQ==">

    <meta name="enabled-features" content="UNIVERSE_BANNER">

  <meta name="html-safe-nonce" content="438c43ede71859aaa4fb535601bf074c027f301e">

  <meta http-equiv="x-pjax-version" content="08264d188a7a36bbba1c1fff036496e1">
  

      <link href="https://github.com/ckan/ckan/commits/master.atom" rel="alternate" title="Recent Commits to ckan:master" type="application/atom+xml">

  <meta name="description" content="ckan - CKAN is an open-source DMS (data management system) for powering data hubs and data portals. CKAN makes it easy to publish, share and use data. It powers datahub.io, catalog.data.gov and data.gov.uk among many other sites.">
  <meta name="go-import" content="github.com/ckan/ckan git https://github.com/ckan/ckan.git">

  <meta content="1630326" name="octolytics-dimension-user_id" /><meta content="ckan" name="octolytics-dimension-user_login" /><meta content="2750721" name="octolytics-dimension-repository_id" /><meta content="ckan/ckan" name="octolytics-dimension-repository_nwo" /><meta content="true" name="octolytics-dimension-repository_public" /><meta content="false" name="octolytics-dimension-repository_is_fork" /><meta content="2750721" name="octolytics-dimension-repository_network_root_id" /><meta content="ckan/ckan" name="octolytics-dimension-repository_network_root_nwo" /><meta content="false" name="octolytics-dimension-repository_explore_github_marketplace_ci_cta_shown" />


    <link rel="canonical" href="https://github.com/ckan/ckan/blob/master/ckan/config/routing.py" data-pjax-transient>


  <meta name="browser-stats-url" content="https://api.github.com/_private/browser/stats">

  <meta name="browser-errors-url" content="https://api.github.com/_private/browser/errors">

  <link rel="mask-icon" href="https://assets-cdn.github.com/pinned-octocat.svg" color="#000000">
  <link rel="icon" type="image/x-icon" href="https://assets-cdn.github.com/favicon.ico">

<meta name="theme-color" content="#1e2327">


  <meta name="u2f-support" content="true">

  </head>

  <body class="logged-in env-production page-blob">
    

  <div class="position-relative js-header-wrapper ">
    <a href="#start-of-content" tabindex="1" class="bg-black text-white p-3 show-on-focus js-skip-to-content">Skip to content</a>
    <div id="js-pjax-loader-bar" class="pjax-loader-bar"><div class="progress"></div></div>

    
    
    



        
<header class="Header  f5" role="banner">
  <div class="d-flex px-3 flex-justify-between container-lg">
    <div class="d-flex flex-justify-between">
      <a class="header-logo-invertocat" href="https://github.com/" data-hotkey="g d" aria-label="Homepage" data-ga-click="Header, go to dashboard, icon:logo">
  <svg aria-hidden="true" class="octicon octicon-mark-github" height="32" version="1.1" viewBox="0 0 16 16" width="32"><path fill-rule="evenodd" d="M8 0C3.58 0 0 3.58 0 8c0 3.54 2.29 6.53 5.47 7.59.4.07.55-.17.55-.38 0-.19-.01-.82-.01-1.49-2.01.37-2.53-.49-2.69-.94-.09-.23-.48-.94-.82-1.13-.28-.15-.68-.52-.01-.53.63-.01 1.08.58 1.23.82.72 1.21 1.87.87 2.33.66.07-.52.28-.87.51-1.07-1.78-.2-3.64-.89-3.64-3.95 0-.87.31-1.59.82-2.15-.08-.2-.36-1.02.08-2.12 0 0 .67-.21 2.2.82.64-.18 1.32-.27 2-.27.68 0 1.36.09 2 .27 1.53-1.04 2.2-.82 2.2-.82.44 1.1.16 1.92.08 2.12.51.56.82 1.27.82 2.15 0 3.07-1.87 3.75-3.65 3.95.29.25.54.73.54 1.48 0 1.07-.01 1.93-.01 2.2 0 .21.15.46.55.38A8.013 8.013 0 0 0 16 8c0-4.42-3.58-8-8-8z"/></svg>
</a>


    </div>

    <div class="HeaderMenu d-flex flex-justify-between flex-auto">
      <div class="d-flex">
            <div class="">
              <div class="header-search scoped-search site-scoped-search js-site-search" role="search">
  <!-- '"` --><!-- </textarea></xmp> --></option></form><form accept-charset="UTF-8" action="/ckan/ckan/search" class="js-site-search-form" data-scoped-search-url="/ckan/ckan/search" data-unscoped-search-url="/search" method="get"><div style="margin:0;padding:0;display:inline"><input name="utf8" type="hidden" value="&#x2713;" /></div>
    <label class="form-control header-search-wrapper js-chromeless-input-container">
        <a href="/ckan/ckan/blob/master/ckan/config/routing.py" class="header-search-scope no-underline">This repository</a>
      <input type="text"
        class="form-control header-search-input js-site-search-focus js-site-search-field is-clearable"
        data-hotkey="s"
        name="q"
        value=""
        placeholder="Search"
        aria-label="Search this repository"
        data-unscoped-placeholder="Search GitHub"
        data-scoped-placeholder="Search"
        autocapitalize="off">
        <input type="hidden" class="js-site-search-type-field" name="type" >
    </label>
</form></div>

            </div>

          <ul class="d-flex pl-2 flex-items-center text-bold list-style-none" role="navigation">
            <li>
              <a href="/pulls" aria-label="Pull requests you created" class="js-selected-navigation-item HeaderNavlink px-2" data-ga-click="Header, click, Nav menu - item:pulls context:user" data-hotkey="g p" data-selected-links="/pulls /pulls/assigned /pulls/mentioned /pulls">
                Pull requests
</a>            </li>
            <li>
              <a href="/issues" aria-label="Issues you created" class="js-selected-navigation-item HeaderNavlink px-2" data-ga-click="Header, click, Nav menu - item:issues context:user" data-hotkey="g i" data-selected-links="/issues /issues/assigned /issues/mentioned /issues">
                Issues
</a>            </li>
                <li>
                  <a href="/marketplace" class="js-selected-navigation-item HeaderNavlink px-2" data-ga-click="Header, click, Nav menu - item:marketplace context:user" data-selected-links=" /marketplace">
                    Marketplace
</a>                </li>
            <li>
              <a href="/explore" class="js-selected-navigation-item HeaderNavlink px-2" data-ga-click="Header, click, Nav menu - item:explore" data-selected-links="/explore /trending /trending/developers /integrations /integrations/feature/code /integrations/feature/collaborate /integrations/feature/ship showcases showcases_search showcases_landing /explore">
                Explore
</a>            </li>
          </ul>
      </div>

      <div class="d-flex">
        
<ul class="user-nav d-flex flex-items-center list-style-none" id="user-links">
  <li class="dropdown js-menu-container js-header-notifications">
    <span class="d-inline-block  px-2">
      

    </span>
  </li>

  <li class="dropdown js-menu-container">
    <details class="dropdown-details js-dropdown-details d-flex px-2 flex-items-center">
      <summary class="HeaderNavlink"
         aria-label="Create new…"
         data-ga-click="Header, create new, icon:add">
        <svg aria-hidden="true" class="octicon octicon-plus float-left mr-1 mt-1" height="16" version="1.1" viewBox="0 0 12 16" width="12"><path fill-rule="evenodd" d="M12 9H7v5H5V9H0V7h5V2h2v5h5z"/></svg>
        <span class="dropdown-caret mt-1"></span>
      </summary>

      <ul class="dropdown-menu dropdown-menu-sw">
        
<a class="dropdown-item" href="/new" data-ga-click="Header, create new repository">
  New repository
</a>

  <a class="dropdown-item" href="/new/import" data-ga-click="Header, import a repository">
    Import repository
  </a>

<a class="dropdown-item" href="https://gist.github.com/" data-ga-click="Header, create new gist">
  New gist
</a>

  <a class="dropdown-item" href="/organizations/new" data-ga-click="Header, create new organization">
    New organization
  </a>



  <div class="dropdown-divider"></div>
  <div class="dropdown-header">
    <span title="ckan/ckan">This repository</span>
  </div>
    <a class="dropdown-item" href="/ckan/ckan/issues/new" data-ga-click="Header, create new issue">
      New issue
    </a>

      </ul>
    </details>
  </li>

  <li class="dropdown js-menu-container">

    <details class="dropdown-details js-dropdown-details d-flex pl-2 flex-items-center">
      <summary class="HeaderNavlink name mt-1"
        aria-label="View profile and more"
        data-ga-click="Header, show menu, icon:avatar">
        <img alt="@smartcolumbus-ide" class="avatar float-left mr-1" src="https://avatars3.githubusercontent.com/u/32200864?v=4&amp;s=40" height="20" width="20">
        <span class="dropdown-caret"></span>
      </summary>

      <ul class="dropdown-menu dropdown-menu-sw">
        <li class="dropdown-header header-nav-current-user css-truncate">
          Signed in as <strong class="css-truncate-target">smartcolumbus-ide</strong>
        </li>

        <li class="dropdown-divider"></li>

        <li><a class="dropdown-item" href="/smartcolumbus-ide" data-ga-click="Header, go to profile, text:your profile">
          Your profile
        </a></li>
        <li><a class="dropdown-item" href="/smartcolumbus-ide?tab=stars" data-ga-click="Header, go to starred repos, text:your stars">
          Your stars
        </a></li>
          <li><a class="dropdown-item" href="https://gist.github.com/" data-ga-click="Header, your gists, text:your gists">Your Gists</a></li>

        <li class="dropdown-divider"></li>

        <li><a class="dropdown-item" href="https://help.github.com" data-ga-click="Header, go to help, text:help">
          Help
        </a></li>

        <li><a class="dropdown-item" href="/settings/profile" data-ga-click="Header, go to settings, icon:settings">
          Settings
        </a></li>

        <li><!-- '"` --><!-- </textarea></xmp> --></option></form><form accept-charset="UTF-8" action="/logout" class="logout-form" method="post"><div style="margin:0;padding:0;display:inline"><input name="utf8" type="hidden" value="&#x2713;" /><input name="authenticity_token" type="hidden" value="G2X09ybp3LSm5z7fgAJF7RY2+4oRfR02nHMh6LsryhHlKwkU3a2+AcfCOC74Ce1C1q5EDMHD1eqf17Nz5OlJHg==" /></div>
          <button type="submit" class="dropdown-item dropdown-signout" data-ga-click="Header, sign out, icon:logout">
            Sign out
          </button>
        </form></li>
      </ul>
    </details>
  </li>
</ul>


        <!-- '"` --><!-- </textarea></xmp> --></option></form><form accept-charset="UTF-8" action="/logout" class="sr-only right-0" method="post"><div style="margin:0;padding:0;display:inline"><input name="utf8" type="hidden" value="&#x2713;" /><input name="authenticity_token" type="hidden" value="b44TwJA3hhki0QcbftCIPbbYIxoYy397wSdMAElMwfWRwO4ja3PkrEP0AeoG2yCSdkCcnMh1t6fCg96bFo5C+g==" /></div>
          <button type="submit" class="dropdown-item dropdown-signout" data-ga-click="Header, sign out, icon:logout">
            Sign out
          </button>
</form>      </div>
    </div>
  </div>
</header>


      

  </div>

  <div id="start-of-content" class="show-on-focus"></div>

    <div id="js-flash-container">
</div>



  <div role="main">
        <div itemscope itemtype="http://schema.org/SoftwareSourceCode">
    <div id="js-repo-pjax-container" data-pjax-container>
      



  



    <div class="pagehead repohead instapaper_ignore readability-menu experiment-repo-nav">
      <div class="container repohead-details-container">

        <ul class="pagehead-actions">
  <li>
        <!-- '"` --><!-- </textarea></xmp> --></option></form><form accept-charset="UTF-8" action="/notifications/subscribe" class="js-social-container" data-autosubmit="true" data-remote="true" method="post"><div style="margin:0;padding:0;display:inline"><input name="utf8" type="hidden" value="&#x2713;" /><input name="authenticity_token" type="hidden" value="o8sSBBhNsWbXFlWKuzYDxU2s5NU1cvXVE0Q0PxlczhyLKin+TF0qo0zrdoBlIq3JTfWkupqMGeE01WDLHQd8fQ==" /></div>      <input class="form-control" id="repository_id" name="repository_id" type="hidden" value="2750721" />

        <div class="select-menu js-menu-container js-select-menu">
          <a href="/ckan/ckan/subscription"
            class="btn btn-sm btn-with-count select-menu-button js-menu-target"
            role="button"
            aria-haspopup="true"
            aria-expanded="false"
            aria-label="Toggle repository notifications menu"
            data-ga-click="Repository, click Watch settings, action:blob#show">
            <span class="js-select-button">
                <svg aria-hidden="true" class="octicon octicon-eye" height="16" version="1.1" viewBox="0 0 16 16" width="16"><path fill-rule="evenodd" d="M8.06 2C3 2 0 8 0 8s3 6 8.06 6C13 14 16 8 16 8s-3-6-7.94-6zM8 12c-2.2 0-4-1.78-4-4 0-2.2 1.8-4 4-4 2.22 0 4 1.8 4 4 0 2.22-1.78 4-4 4zm2-4c0 1.11-.89 2-2 2-1.11 0-2-.89-2-2 0-1.11.89-2 2-2 1.11 0 2 .89 2 2z"/></svg>
                Watch
            </span>
          </a>
            <a class="social-count js-social-count"
              href="/ckan/ckan/watchers"
              aria-label="161 users are watching this repository">
              161
            </a>

        <div class="select-menu-modal-holder">
          <div class="select-menu-modal subscription-menu-modal js-menu-content">
            <div class="select-menu-header js-navigation-enable" tabindex="-1">
              <svg aria-label="Close" class="octicon octicon-x js-menu-close" height="16" role="img" version="1.1" viewBox="0 0 12 16" width="12"><path fill-rule="evenodd" d="M7.48 8l3.75 3.75-1.48 1.48L6 9.48l-3.75 3.75-1.48-1.48L4.52 8 .77 4.25l1.48-1.48L6 6.52l3.75-3.75 1.48 1.48z"/></svg>
              <span class="select-menu-title">Notifications</span>
            </div>

              <div class="select-menu-list js-navigation-container" role="menu">

                <div class="select-menu-item js-navigation-item selected" role="menuitem" tabindex="0">
                  <svg aria-hidden="true" class="octicon octicon-check select-menu-item-icon" height="16" version="1.1" viewBox="0 0 12 16" width="12"><path fill-rule="evenodd" d="M12 5l-8 8-4-4 1.5-1.5L4 10l6.5-6.5z"/></svg>
                  <div class="select-menu-item-text">
                    <input checked="checked" id="do_included" name="do" type="radio" value="included" />
                    <span class="select-menu-item-heading">Not watching</span>
                    <span class="description">Be notified when participating or @mentioned.</span>
                    <span class="js-select-button-text hidden-select-button-text">
                      <svg aria-hidden="true" class="octicon octicon-eye" height="16" version="1.1" viewBox="0 0 16 16" width="16"><path fill-rule="evenodd" d="M8.06 2C3 2 0 8 0 8s3 6 8.06 6C13 14 16 8 16 8s-3-6-7.94-6zM8 12c-2.2 0-4-1.78-4-4 0-2.2 1.8-4 4-4 2.22 0 4 1.8 4 4 0 2.22-1.78 4-4 4zm2-4c0 1.11-.89 2-2 2-1.11 0-2-.89-2-2 0-1.11.89-2 2-2 1.11 0 2 .89 2 2z"/></svg>
                      Watch
                    </span>
                  </div>
                </div>

                <div class="select-menu-item js-navigation-item " role="menuitem" tabindex="0">
                  <svg aria-hidden="true" class="octicon octicon-check select-menu-item-icon" height="16" version="1.1" viewBox="0 0 12 16" width="12"><path fill-rule="evenodd" d="M12 5l-8 8-4-4 1.5-1.5L4 10l6.5-6.5z"/></svg>
                  <div class="select-menu-item-text">
                    <input id="do_subscribed" name="do" type="radio" value="subscribed" />
                    <span class="select-menu-item-heading">Watching</span>
                    <span class="description">Be notified of all conversations.</span>
                    <span class="js-select-button-text hidden-select-button-text">
                      <svg aria-hidden="true" class="octicon octicon-eye" height="16" version="1.1" viewBox="0 0 16 16" width="16"><path fill-rule="evenodd" d="M8.06 2C3 2 0 8 0 8s3 6 8.06 6C13 14 16 8 16 8s-3-6-7.94-6zM8 12c-2.2 0-4-1.78-4-4 0-2.2 1.8-4 4-4 2.22 0 4 1.8 4 4 0 2.22-1.78 4-4 4zm2-4c0 1.11-.89 2-2 2-1.11 0-2-.89-2-2 0-1.11.89-2 2-2 1.11 0 2 .89 2 2z"/></svg>
                        Unwatch
                    </span>
                  </div>
                </div>

                <div class="select-menu-item js-navigation-item " role="menuitem" tabindex="0">
                  <svg aria-hidden="true" class="octicon octicon-check select-menu-item-icon" height="16" version="1.1" viewBox="0 0 12 16" width="12"><path fill-rule="evenodd" d="M12 5l-8 8-4-4 1.5-1.5L4 10l6.5-6.5z"/></svg>
                  <div class="select-menu-item-text">
                    <input id="do_ignore" name="do" type="radio" value="ignore" />
                    <span class="select-menu-item-heading">Ignoring</span>
                    <span class="description">Never be notified.</span>
                    <span class="js-select-button-text hidden-select-button-text">
                      <svg aria-hidden="true" class="octicon octicon-mute" height="16" version="1.1" viewBox="0 0 16 16" width="16"><path fill-rule="evenodd" d="M8 2.81v10.38c0 .67-.81 1-1.28.53L3 10H1c-.55 0-1-.45-1-1V7c0-.55.45-1 1-1h2l3.72-3.72C7.19 1.81 8 2.14 8 2.81zm7.53 3.22l-1.06-1.06-1.97 1.97-1.97-1.97-1.06 1.06L11.44 8 9.47 9.97l1.06 1.06 1.97-1.97 1.97 1.97 1.06-1.06L13.56 8l1.97-1.97z"/></svg>
                        Stop ignoring
                    </span>
                  </div>
                </div>

              </div>

            </div>
          </div>
        </div>
</form>
  </li>

  <li>
    
  <div class="js-toggler-container js-social-container starring-container ">
    <!-- '"` --><!-- </textarea></xmp> --></option></form><form accept-charset="UTF-8" action="/ckan/ckan/unstar" class="starred" data-remote="true" method="post"><div style="margin:0;padding:0;display:inline"><input name="utf8" type="hidden" value="&#x2713;" /><input name="authenticity_token" type="hidden" value="RVxFEzjiZ8YzUC1J5yWoaJ+iYlWAgktwi/VtmGXAm/gNWx3sMPW5hKLUDw587tph2RhvgBCwltqof0TW9KCsmQ==" /></div>
      <button
        type="submit"
        class="btn btn-sm btn-with-count js-toggler-target"
        aria-label="Unstar this repository" title="Unstar ckan/ckan"
        data-ga-click="Repository, click unstar button, action:blob#show; text:Unstar">
        <svg aria-hidden="true" class="octicon octicon-star" height="16" version="1.1" viewBox="0 0 14 16" width="14"><path fill-rule="evenodd" d="M14 6l-4.9-.64L7 1 4.9 5.36 0 6l3.6 3.26L2.67 14 7 11.67 11.33 14l-.93-4.74z"/></svg>
        Unstar
      </button>
        <a class="social-count js-social-count" href="/ckan/ckan/stargazers"
           aria-label="1671 users starred this repository">
          1,671
        </a>
</form>
    <!-- '"` --><!-- </textarea></xmp> --></option></form><form accept-charset="UTF-8" action="/ckan/ckan/star" class="unstarred" data-remote="true" method="post"><div style="margin:0;padding:0;display:inline"><input name="utf8" type="hidden" value="&#x2713;" /><input name="authenticity_token" type="hidden" value="uFgn6a2sPuIwps+qUT8eB8DgModRLF1iMnC5AnH1qjFi9V15XWLgglyvOQGfjnbBH0cKKqZ3JrkNSNbaOUenBA==" /></div>
      <button
        type="submit"
        class="btn btn-sm btn-with-count js-toggler-target"
        aria-label="Star this repository" title="Star ckan/ckan"
        data-ga-click="Repository, click star button, action:blob#show; text:Star">
        <svg aria-hidden="true" class="octicon octicon-star" height="16" version="1.1" viewBox="0 0 14 16" width="14"><path fill-rule="evenodd" d="M14 6l-4.9-.64L7 1 4.9 5.36 0 6l3.6 3.26L2.67 14 7 11.67 11.33 14l-.93-4.74z"/></svg>
        Star
      </button>
        <a class="social-count js-social-count" href="/ckan/ckan/stargazers"
           aria-label="1671 users starred this repository">
          1,671
        </a>
</form>  </div>

  </li>

  <li>
          <!-- '"` --><!-- </textarea></xmp> --></option></form><form accept-charset="UTF-8" action="/ckan/ckan/fork" class="btn-with-count" method="post"><div style="margin:0;padding:0;display:inline"><input name="utf8" type="hidden" value="&#x2713;" /><input name="authenticity_token" type="hidden" value="KcohtFUzyukirO0meXu1AYwYYED5SD2uwokOpad5U9XMxFNaGq3MBZMa9CHhVcc9QZdGf/dUI9N6X2leQfbSHA==" /></div>
            <button
                type="submit"
                class="btn btn-sm btn-with-count"
                data-ga-click="Repository, show fork modal, action:blob#show; text:Fork"
                title="Fork your own copy of ckan/ckan to your account"
                aria-label="Fork your own copy of ckan/ckan to your account">
              <svg aria-hidden="true" class="octicon octicon-repo-forked" height="16" version="1.1" viewBox="0 0 10 16" width="10"><path fill-rule="evenodd" d="M8 1a1.993 1.993 0 0 0-1 3.72V6L5 8 3 6V4.72A1.993 1.993 0 0 0 2 1a1.993 1.993 0 0 0-1 3.72V6.5l3 3v1.78A1.993 1.993 0 0 0 5 15a1.993 1.993 0 0 0 1-3.72V9.5l3-3V4.72A1.993 1.993 0 0 0 8 1zM2 4.2C1.34 4.2.8 3.65.8 3c0-.65.55-1.2 1.2-1.2.65 0 1.2.55 1.2 1.2 0 .65-.55 1.2-1.2 1.2zm3 10c-.66 0-1.2-.55-1.2-1.2 0-.65.55-1.2 1.2-1.2.65 0 1.2.55 1.2 1.2 0 .65-.55 1.2-1.2 1.2zm3-10c-.66 0-1.2-.55-1.2-1.2 0-.65.55-1.2 1.2-1.2.65 0 1.2.55 1.2 1.2 0 .65-.55 1.2-1.2 1.2z"/></svg>
              Fork
            </button>
</form>
    <a href="/ckan/ckan/network" class="social-count"
       aria-label="945 users forked this repository">
      945
    </a>
  </li>
</ul>

        <h1 class="public ">
  <svg aria-hidden="true" class="octicon octicon-repo" height="16" version="1.1" viewBox="0 0 12 16" width="12"><path fill-rule="evenodd" d="M4 9H3V8h1v1zm0-3H3v1h1V6zm0-2H3v1h1V4zm0-2H3v1h1V2zm8-1v12c0 .55-.45 1-1 1H6v2l-1.5-1.5L3 16v-2H1c-.55 0-1-.45-1-1V1c0-.55.45-1 1-1h10c.55 0 1 .45 1 1zm-1 10H1v2h2v-1h3v1h5v-2zm0-10H2v9h9V1z"/></svg>
  <span class="author" itemprop="author"><a href="/ckan" class="url fn" rel="author">ckan</a></span><!--
--><span class="path-divider">/</span><!--
--><strong itemprop="name"><a href="/ckan/ckan" data-pjax="#js-repo-pjax-container">ckan</a></strong>

</h1>

      </div>
      <div class="container">
        
<nav class="reponav js-repo-nav js-sidenav-container-pjax"
     itemscope
     itemtype="http://schema.org/BreadcrumbList"
     role="navigation"
     data-pjax="#js-repo-pjax-container">

  <span itemscope itemtype="http://schema.org/ListItem" itemprop="itemListElement">
    <a href="/ckan/ckan" class="js-selected-navigation-item selected reponav-item" data-hotkey="g c" data-selected-links="repo_source repo_downloads repo_commits repo_releases repo_tags repo_branches /ckan/ckan" itemprop="url">
      <svg aria-hidden="true" class="octicon octicon-code" height="16" version="1.1" viewBox="0 0 14 16" width="14"><path fill-rule="evenodd" d="M9.5 3L8 4.5 11.5 8 8 11.5 9.5 13 14 8 9.5 3zm-5 0L0 8l4.5 5L6 11.5 2.5 8 6 4.5 4.5 3z"/></svg>
      <span itemprop="name">Code</span>
      <meta itemprop="position" content="1">
</a>  </span>

    <span itemscope itemtype="http://schema.org/ListItem" itemprop="itemListElement">
      <a href="/ckan/ckan/issues" class="js-selected-navigation-item reponav-item" data-hotkey="g i" data-selected-links="repo_issues repo_labels repo_milestones /ckan/ckan/issues" itemprop="url">
        <svg aria-hidden="true" class="octicon octicon-issue-opened" height="16" version="1.1" viewBox="0 0 14 16" width="14"><path fill-rule="evenodd" d="M7 2.3c3.14 0 5.7 2.56 5.7 5.7s-2.56 5.7-5.7 5.7A5.71 5.71 0 0 1 1.3 8c0-3.14 2.56-5.7 5.7-5.7zM7 1C3.14 1 0 4.14 0 8s3.14 7 7 7 7-3.14 7-7-3.14-7-7-7zm1 3H6v5h2V4zm0 6H6v2h2v-2z"/></svg>
        <span itemprop="name">Issues</span>
        <span class="Counter">207</span>
        <meta itemprop="position" content="2">
</a>    </span>

  <span itemscope itemtype="http://schema.org/ListItem" itemprop="itemListElement">
    <a href="/ckan/ckan/pulls" class="js-selected-navigation-item reponav-item" data-hotkey="g p" data-selected-links="repo_pulls /ckan/ckan/pulls" itemprop="url">
      <svg aria-hidden="true" class="octicon octicon-git-pull-request" height="16" version="1.1" viewBox="0 0 12 16" width="12"><path fill-rule="evenodd" d="M11 11.28V5c-.03-.78-.34-1.47-.94-2.06C9.46 2.35 8.78 2.03 8 2H7V0L4 3l3 3V4h1c.27.02.48.11.69.31.21.2.3.42.31.69v6.28A1.993 1.993 0 0 0 10 15a1.993 1.993 0 0 0 1-3.72zm-1 2.92c-.66 0-1.2-.55-1.2-1.2 0-.65.55-1.2 1.2-1.2.65 0 1.2.55 1.2 1.2 0 .65-.55 1.2-1.2 1.2zM4 3c0-1.11-.89-2-2-2a1.993 1.993 0 0 0-1 3.72v6.56A1.993 1.993 0 0 0 2 15a1.993 1.993 0 0 0 1-3.72V4.72c.59-.34 1-.98 1-1.72zm-.8 10c0 .66-.55 1.2-1.2 1.2-.65 0-1.2-.55-1.2-1.2 0-.65.55-1.2 1.2-1.2.65 0 1.2.55 1.2 1.2zM2 4.2C1.34 4.2.8 3.65.8 3c0-.65.55-1.2 1.2-1.2.65 0 1.2.55 1.2 1.2 0 .65-.55 1.2-1.2 1.2z"/></svg>
      <span itemprop="name">Pull requests</span>
      <span class="Counter">68</span>
      <meta itemprop="position" content="3">
</a>  </span>

    <a href="/ckan/ckan/projects" class="js-selected-navigation-item reponav-item" data-hotkey="g b" data-selected-links="repo_projects new_repo_project repo_project /ckan/ckan/projects">
      <svg aria-hidden="true" class="octicon octicon-project" height="16" version="1.1" viewBox="0 0 15 16" width="15"><path fill-rule="evenodd" d="M10 12h3V2h-3v10zm-4-2h3V2H6v8zm-4 4h3V2H2v12zm-1 1h13V1H1v14zM14 0H1a1 1 0 0 0-1 1v14a1 1 0 0 0 1 1h13a1 1 0 0 0 1-1V1a1 1 0 0 0-1-1z"/></svg>
      Projects
      <span class="Counter" >1</span>
</a>
    <a href="/ckan/ckan/wiki" class="js-selected-navigation-item reponav-item" data-hotkey="g w" data-selected-links="repo_wiki /ckan/ckan/wiki">
      <svg aria-hidden="true" class="octicon octicon-book" height="16" version="1.1" viewBox="0 0 16 16" width="16"><path fill-rule="evenodd" d="M3 5h4v1H3V5zm0 3h4V7H3v1zm0 2h4V9H3v1zm11-5h-4v1h4V5zm0 2h-4v1h4V7zm0 2h-4v1h4V9zm2-6v9c0 .55-.45 1-1 1H9.5l-1 1-1-1H2c-.55 0-1-.45-1-1V3c0-.55.45-1 1-1h5.5l1 1 1-1H15c.55 0 1 .45 1 1zm-8 .5L7.5 3H2v9h6V3.5zm7-.5H9.5l-.5.5V12h6V3z"/></svg>
      Wiki
</a>

    <div class="reponav-dropdown js-menu-container">
      <button type="button" class="btn-link reponav-item reponav-dropdown js-menu-target " data-no-toggle aria-expanded="false" aria-haspopup="true">
        Insights
        <svg aria-hidden="true" class="octicon octicon-triangle-down v-align-middle text-gray" height="11" version="1.1" viewBox="0 0 12 16" width="8"><path fill-rule="evenodd" d="M0 5l6 6 6-6z"/></svg>
      </button>
      <div class="dropdown-menu-content js-menu-content">
        <div class="dropdown-menu dropdown-menu-sw">
          <a class="dropdown-item" href="/ckan/ckan/pulse" data-skip-pjax>
            <svg aria-hidden="true" class="octicon octicon-pulse" height="16" version="1.1" viewBox="0 0 14 16" width="14"><path fill-rule="evenodd" d="M11.5 8L8.8 5.4 6.6 8.5 5.5 1.6 2.38 8H0v2h3.6l.9-1.8.9 5.4L9 8.5l1.6 1.5H14V8z"/></svg>
            Pulse
          </a>
          <a class="dropdown-item" href="/ckan/ckan/graphs" data-skip-pjax>
            <svg aria-hidden="true" class="octicon octicon-graph" height="16" version="1.1" viewBox="0 0 16 16" width="16"><path fill-rule="evenodd" d="M16 14v1H0V0h1v14h15zM5 13H3V8h2v5zm4 0H7V3h2v10zm4 0h-2V6h2v7z"/></svg>
            Graphs
          </a>
        </div>
      </div>
    </div>
</nav>

      </div>
    </div>

<div class="container new-discussion-timeline experiment-repo-nav">
  <div class="repository-content">

    
  <a href="/ckan/ckan/blob/2c1a6389456ce8706618998af2d8b3fa8dbb86a3/ckan/config/routing.py" class="d-none js-permalink-shortcut" data-hotkey="y">Permalink</a>

  <!-- blob contrib key: blob_contributors:v21:eba135959c7a084d4eac91deaedfaabf -->

  <div class="file-navigation js-zeroclipboard-container">
    
<div class="select-menu branch-select-menu js-menu-container js-select-menu float-left">
  <button class=" btn btn-sm select-menu-button js-menu-target css-truncate" data-hotkey="w"
    
    type="button" aria-label="Switch branches or tags" aria-expanded="false" aria-haspopup="true">
      <i>Branch:</i>
      <span class="js-select-button css-truncate-target">master</span>
  </button>

  <div class="select-menu-modal-holder js-menu-content js-navigation-container" data-pjax>

    <div class="select-menu-modal">
      <div class="select-menu-header">
        <svg aria-label="Close" class="octicon octicon-x js-menu-close" height="16" role="img" version="1.1" viewBox="0 0 12 16" width="12"><path fill-rule="evenodd" d="M7.48 8l3.75 3.75-1.48 1.48L6 9.48l-3.75 3.75-1.48-1.48L4.52 8 .77 4.25l1.48-1.48L6 6.52l3.75-3.75 1.48 1.48z"/></svg>
        <span class="select-menu-title">Switch branches/tags</span>
      </div>

      <div class="select-menu-filters">
        <div class="select-menu-text-filter">
          <input type="text" aria-label="Filter branches/tags" id="context-commitish-filter-field" class="form-control js-filterable-field js-navigation-enable" placeholder="Filter branches/tags">
        </div>
        <div class="select-menu-tabs">
          <ul>
            <li class="select-menu-tab">
              <a href="#" data-tab-filter="branches" data-filter-placeholder="Filter branches/tags" class="js-select-menu-tab" role="tab">Branches</a>
            </li>
            <li class="select-menu-tab">
              <a href="#" data-tab-filter="tags" data-filter-placeholder="Find a tag…" class="js-select-menu-tab" role="tab">Tags</a>
            </li>
          </ul>
        </div>
      </div>

      <div class="select-menu-list select-menu-tab-bucket js-select-menu-tab-bucket" data-tab-filter="branches" role="menu">

        <div data-filterable-for="context-commitish-filter-field" data-filterable-type="substring">


            <a class="select-menu-item js-navigation-item js-navigation-open "
               href="/ckan/ckan/blob/2.0-travis-fix/ckan/config/routing.py"
               data-name="2.0-travis-fix"
               data-skip-pjax="true"
               rel="nofollow">
              <svg aria-hidden="true" class="octicon octicon-check select-menu-item-icon" height="16" version="1.1" viewBox="0 0 12 16" width="12"><path fill-rule="evenodd" d="M12 5l-8 8-4-4 1.5-1.5L4 10l6.5-6.5z"/></svg>
              <span class="select-menu-item-text css-truncate-target js-select-menu-filter-text">
                2.0-travis-fix
              </span>
            </a>
            <a class="select-menu-item js-navigation-item js-navigation-open "
               href="/ckan/ckan/blob/2.3.5-fix-solr-circleci/ckan/config/routing.py"
               data-name="2.3.5-fix-solr-circleci"
               data-skip-pjax="true"
               rel="nofollow">
              <svg aria-hidden="true" class="octicon octicon-check select-menu-item-icon" height="16" version="1.1" viewBox="0 0 12 16" width="12"><path fill-rule="evenodd" d="M12 5l-8 8-4-4 1.5-1.5L4 10l6.5-6.5z"/></svg>
              <span class="select-menu-item-text css-truncate-target js-select-menu-filter-text">
                2.3.5-fix-solr-circleci
              </span>
            </a>
            <a class="select-menu-item js-navigation-item js-navigation-open "
               href="/ckan/ckan/blob/217-organization-helper-text/ckan/config/routing.py"
               data-name="217-organization-helper-text"
               data-skip-pjax="true"
               rel="nofollow">
              <svg aria-hidden="true" class="octicon octicon-check select-menu-item-icon" height="16" version="1.1" viewBox="0 0 12 16" width="12"><path fill-rule="evenodd" d="M12 5l-8 8-4-4 1.5-1.5L4 10l6.5-6.5z"/></svg>
              <span class="select-menu-item-text css-truncate-target js-select-menu-filter-text">
                217-organization-helper-text
              </span>
            </a>
            <a class="select-menu-item js-navigation-item js-navigation-open "
               href="/ckan/ckan/blob/222-test-branch/ckan/config/routing.py"
               data-name="222-test-branch"
               data-skip-pjax="true"
               rel="nofollow">
              <svg aria-hidden="true" class="octicon octicon-check select-menu-item-icon" height="16" version="1.1" viewBox="0 0 12 16" width="12"><path fill-rule="evenodd" d="M12 5l-8 8-4-4 1.5-1.5L4 10l6.5-6.5z"/></svg>
              <span class="select-menu-item-text css-truncate-target js-select-menu-filter-text">
                222-test-branch
              </span>
            </a>
            <a class="select-menu-item js-navigation-item js-navigation-open "
               href="/ckan/ckan/blob/224-masthead-active-state/ckan/config/routing.py"
               data-name="224-masthead-active-state"
               data-skip-pjax="true"
               rel="nofollow">
              <svg aria-hidden="true" class="octicon octicon-check select-menu-item-icon" height="16" version="1.1" viewBox="0 0 12 16" width="12"><path fill-rule="evenodd" d="M12 5l-8 8-4-4 1.5-1.5L4 10l6.5-6.5z"/></svg>
              <span class="select-menu-item-text css-truncate-target js-select-menu-filter-text">
                224-masthead-active-state
              </span>
            </a>
            <a class="select-menu-item js-navigation-item js-navigation-open "
               href="/ckan/ckan/blob/226-text-highlighting/ckan/config/routing.py"
               data-name="226-text-highlighting"
               data-skip-pjax="true"
               rel="nofollow">
              <svg aria-hidden="true" class="octicon octicon-check select-menu-item-icon" height="16" version="1.1" viewBox="0 0 12 16" width="12"><path fill-rule="evenodd" d="M12 5l-8 8-4-4 1.5-1.5L4 10l6.5-6.5z"/></svg>
              <span class="select-menu-item-text css-truncate-target js-select-menu-filter-text">
                226-text-highlighting
              </span>
            </a>
            <a class="select-menu-item js-navigation-item js-navigation-open "
               href="/ckan/ckan/blob/231-verbose-header-template/ckan/config/routing.py"
               data-name="231-verbose-header-template"
               data-skip-pjax="true"
               rel="nofollow">
              <svg aria-hidden="true" class="octicon octicon-check select-menu-item-icon" height="16" version="1.1" viewBox="0 0 12 16" width="12"><path fill-rule="evenodd" d="M12 5l-8 8-4-4 1.5-1.5L4 10l6.5-6.5z"/></svg>
              <span class="select-menu-item-text css-truncate-target js-select-menu-filter-text">
                231-verbose-header-template
              </span>
            </a>
            <a class="select-menu-item js-navigation-item js-navigation-open "
               href="/ckan/ckan/blob/236-html-in-popovers/ckan/config/routing.py"
               data-name="236-html-in-popovers"
               data-skip-pjax="true"
               rel="nofollow">
              <svg aria-hidden="true" class="octicon octicon-check select-menu-item-icon" height="16" version="1.1" viewBox="0 0 12 16" width="12"><path fill-rule="evenodd" d="M12 5l-8 8-4-4 1.5-1.5L4 10l6.5-6.5z"/></svg>
              <span class="select-menu-item-text css-truncate-target js-select-menu-filter-text">
                236-html-in-popovers
              </span>
            </a>
            <a class="select-menu-item js-navigation-item js-navigation-open "
               href="/ckan/ckan/blob/237-activity-stream-wrapping/ckan/config/routing.py"
               data-name="237-activity-stream-wrapping"
               data-skip-pjax="true"
               rel="nofollow">
              <svg aria-hidden="true" class="octicon octicon-check select-menu-item-icon" height="16" version="1.1" viewBox="0 0 12 16" width="12"><path fill-rule="evenodd" d="M12 5l-8 8-4-4 1.5-1.5L4 10l6.5-6.5z"/></svg>
              <span class="select-menu-item-text css-truncate-target js-select-menu-filter-text">
                237-activity-stream-wrapping
              </span>
            </a>
            <a class="select-menu-item js-navigation-item js-navigation-open "
               href="/ckan/ckan/blob/238-dont-commit-on-package_owner_org_update/ckan/config/routing.py"
               data-name="238-dont-commit-on-package_owner_org_update"
               data-skip-pjax="true"
               rel="nofollow">
              <svg aria-hidden="true" class="octicon octicon-check select-menu-item-icon" height="16" version="1.1" viewBox="0 0 12 16" width="12"><path fill-rule="evenodd" d="M12 5l-8 8-4-4 1.5-1.5L4 10l6.5-6.5z"/></svg>
              <span class="select-menu-item-text css-truncate-target js-select-menu-filter-text">
                238-dont-commit-on-package_owner_org_update
              </span>
            </a>
            <a class="select-menu-item js-navigation-item js-navigation-open "
               href="/ckan/ckan/blob/240-improve-activities-efficiency/ckan/config/routing.py"
               data-name="240-improve-activities-efficiency"
               data-skip-pjax="true"
               rel="nofollow">
              <svg aria-hidden="true" class="octicon octicon-check select-menu-item-icon" height="16" version="1.1" viewBox="0 0 12 16" width="12"><path fill-rule="evenodd" d="M12 5l-8 8-4-4 1.5-1.5L4 10l6.5-6.5z"/></svg>
              <span class="select-menu-item-text css-truncate-target js-select-menu-filter-text">
                240-improve-activities-efficiency
              </span>
            </a>
            <a class="select-menu-item js-navigation-item js-navigation-open "
               href="/ckan/ckan/blob/246-fix-datastorer-tests/ckan/config/routing.py"
               data-name="246-fix-datastorer-tests"
               data-skip-pjax="true"
               rel="nofollow">
              <svg aria-hidden="true" class="octicon octicon-check select-menu-item-icon" height="16" version="1.1" viewBox="0 0 12 16" width="12"><path fill-rule="evenodd" d="M12 5l-8 8-4-4 1.5-1.5L4 10l6.5-6.5z"/></svg>
              <span class="select-menu-item-text css-truncate-target js-select-menu-filter-text">
                246-fix-datastorer-tests
              </span>
            </a>
            <a class="select-menu-item js-navigation-item js-navigation-open "
               href="/ckan/ckan/blob/247-auth-action-update/ckan/config/routing.py"
               data-name="247-auth-action-update"
               data-skip-pjax="true"
               rel="nofollow">
              <svg aria-hidden="true" class="octicon octicon-check select-menu-item-icon" height="16" version="1.1" viewBox="0 0 12 16" width="12"><path fill-rule="evenodd" d="M12 5l-8 8-4-4 1.5-1.5L4 10l6.5-6.5z"/></svg>
              <span class="select-menu-item-text css-truncate-target js-select-menu-filter-text">
                247-auth-action-update
              </span>
            </a>
            <a class="select-menu-item js-navigation-item js-navigation-open "
               href="/ckan/ckan/blob/253-remove-dashboard-notifications-count-reset/ckan/config/routing.py"
               data-name="253-remove-dashboard-notifications-count-reset"
               data-skip-pjax="true"
               rel="nofollow">
              <svg aria-hidden="true" class="octicon octicon-check select-menu-item-icon" height="16" version="1.1" viewBox="0 0 12 16" width="12"><path fill-rule="evenodd" d="M12 5l-8 8-4-4 1.5-1.5L4 10l6.5-6.5z"/></svg>
              <span class="select-menu-item-text css-truncate-target js-select-menu-filter-text">
                253-remove-dashboard-notifications-count-reset
              </span>
            </a>
            <a class="select-menu-item js-navigation-item js-navigation-open "
               href="/ckan/ckan/blob/256-dashboard_activity_list_error/ckan/config/routing.py"
               data-name="256-dashboard_activity_list_error"
               data-skip-pjax="true"
               rel="nofollow">
              <svg aria-hidden="true" class="octicon octicon-check select-menu-item-icon" height="16" version="1.1" viewBox="0 0 12 16" width="12"><path fill-rule="evenodd" d="M12 5l-8 8-4-4 1.5-1.5L4 10l6.5-6.5z"/></svg>
              <span class="select-menu-item-text css-truncate-target js-select-menu-filter-text">
                256-dashboard_activity_list_error
              </span>
            </a>
            <a class="select-menu-item js-navigation-item js-navigation-open "
               href="/ckan/ckan/blob/257-increase-recline-dataproxy-timeout/ckan/config/routing.py"
               data-name="257-increase-recline-dataproxy-timeout"
               data-skip-pjax="true"
               rel="nofollow">
              <svg aria-hidden="true" class="octicon octicon-check select-menu-item-icon" height="16" version="1.1" viewBox="0 0 12 16" width="12"><path fill-rule="evenodd" d="M12 5l-8 8-4-4 1.5-1.5L4 10l6.5-6.5z"/></svg>
              <span class="select-menu-item-text css-truncate-target js-select-menu-filter-text">
                257-increase-recline-dataproxy-timeout
              </span>
            </a>
            <a class="select-menu-item js-navigation-item js-navigation-open "
               href="/ckan/ckan/blob/267-date-indexing-fix/ckan/config/routing.py"
               data-name="267-date-indexing-fix"
               data-skip-pjax="true"
               rel="nofollow">
              <svg aria-hidden="true" class="octicon octicon-check select-menu-item-icon" height="16" version="1.1" viewBox="0 0 12 16" width="12"><path fill-rule="evenodd" d="M12 5l-8 8-4-4 1.5-1.5L4 10l6.5-6.5z"/></svg>
              <span class="select-menu-item-text css-truncate-target js-select-menu-filter-text">
                267-date-indexing-fix
              </span>
            </a>
            <a class="select-menu-item js-navigation-item js-navigation-open "
               href="/ckan/ckan/blob/270-sysadmins-full-orgs-list/ckan/config/routing.py"
               data-name="270-sysadmins-full-orgs-list"
               data-skip-pjax="true"
               rel="nofollow">
              <svg aria-hidden="true" class="octicon octicon-check select-menu-item-icon" height="16" version="1.1" viewBox="0 0 12 16" width="12"><path fill-rule="evenodd" d="M12 5l-8 8-4-4 1.5-1.5L4 10l6.5-6.5z"/></svg>
              <span class="select-menu-item-text css-truncate-target js-select-menu-filter-text">
                270-sysadmins-full-orgs-list
              </span>
            </a>
            <a class="select-menu-item js-navigation-item js-navigation-open "
               href="/ckan/ckan/blob/281-resource-listing-buttons/ckan/config/routing.py"
               data-name="281-resource-listing-buttons"
               data-skip-pjax="true"
               rel="nofollow">
              <svg aria-hidden="true" class="octicon octicon-check select-menu-item-icon" height="16" version="1.1" viewBox="0 0 12 16" width="12"><path fill-rule="evenodd" d="M12 5l-8 8-4-4 1.5-1.5L4 10l6.5-6.5z"/></svg>
              <span class="select-menu-item-text css-truncate-target js-select-menu-filter-text">
                281-resource-listing-buttons
              </span>
            </a>
            <a class="select-menu-item js-navigation-item js-navigation-open "
               href="/ckan/ckan/blob/286-no-orgs-in-group-autocomplete/ckan/config/routing.py"
               data-name="286-no-orgs-in-group-autocomplete"
               data-skip-pjax="true"
               rel="nofollow">
              <svg aria-hidden="true" class="octicon octicon-check select-menu-item-icon" height="16" version="1.1" viewBox="0 0 12 16" width="12"><path fill-rule="evenodd" d="M12 5l-8 8-4-4 1.5-1.5L4 10l6.5-6.5z"/></svg>
              <span class="select-menu-item-text css-truncate-target js-select-menu-filter-text">
                286-no-orgs-in-group-autocomplete
              </span>
            </a>
            <a class="select-menu-item js-navigation-item js-navigation-open "
               href="/ckan/ckan/blob/287-datastore-tests-only-on-pg/ckan/config/routing.py"
               data-name="287-datastore-tests-only-on-pg"
               data-skip-pjax="true"
               rel="nofollow">
              <svg aria-hidden="true" class="octicon octicon-check select-menu-item-icon" height="16" version="1.1" viewBox="0 0 12 16" width="12"><path fill-rule="evenodd" d="M12 5l-8 8-4-4 1.5-1.5L4 10l6.5-6.5z"/></svg>
              <span class="select-menu-item-text css-truncate-target js-select-menu-filter-text">
                287-datastore-tests-only-on-pg
              </span>
            </a>
            <a class="select-menu-item js-navigation-item js-navigation-open "
               href="/ckan/ckan/blob/288-unicode-title-support/ckan/config/routing.py"
               data-name="288-unicode-title-support"
               data-skip-pjax="true"
               rel="nofollow">
              <svg aria-hidden="true" class="octicon octicon-check select-menu-item-icon" height="16" version="1.1" viewBox="0 0 12 16" width="12"><path fill-rule="evenodd" d="M12 5l-8 8-4-4 1.5-1.5L4 10l6.5-6.5z"/></svg>
              <span class="select-menu-item-text css-truncate-target js-select-menu-filter-text">
                288-unicode-title-support
              </span>
            </a>
            <a class="select-menu-item js-navigation-item js-navigation-open "
               href="/ckan/ckan/blob/290-run-all-core-extension-tests/ckan/config/routing.py"
               data-name="290-run-all-core-extension-tests"
               data-skip-pjax="true"
               rel="nofollow">
              <svg aria-hidden="true" class="octicon octicon-check select-menu-item-icon" height="16" version="1.1" viewBox="0 0 12 16" width="12"><path fill-rule="evenodd" d="M12 5l-8 8-4-4 1.5-1.5L4 10l6.5-6.5z"/></svg>
              <span class="select-menu-item-text css-truncate-target js-select-menu-filter-text">
                290-run-all-core-extension-tests
              </span>
            </a>
            <a class="select-menu-item js-navigation-item js-navigation-open "
               href="/ckan/ckan/blob/296-delete-related/ckan/config/routing.py"
               data-name="296-delete-related"
               data-skip-pjax="true"
               rel="nofollow">
              <svg aria-hidden="true" class="octicon octicon-check select-menu-item-icon" height="16" version="1.1" viewBox="0 0 12 16" width="12"><path fill-rule="evenodd" d="M12 5l-8 8-4-4 1.5-1.5L4 10l6.5-6.5z"/></svg>
              <span class="select-menu-item-text css-truncate-target js-select-menu-filter-text">
                296-delete-related
              </span>
            </a>
            <a class="select-menu-item js-navigation-item js-navigation-open "
               href="/ckan/ckan/blob/300-frontend-dependancies/ckan/config/routing.py"
               data-name="300-frontend-dependancies"
               data-skip-pjax="true"
               rel="nofollow">
              <svg aria-hidden="true" class="octicon octicon-check select-menu-item-icon" height="16" version="1.1" viewBox="0 0 12 16" width="12"><path fill-rule="evenodd" d="M12 5l-8 8-4-4 1.5-1.5L4 10l6.5-6.5z"/></svg>
              <span class="select-menu-item-text css-truncate-target js-select-menu-filter-text">
                300-frontend-dependancies
              </span>
            </a>
            <a class="select-menu-item js-navigation-item js-navigation-open "
               href="/ckan/ckan/blob/302-release-textual-tweaks/ckan/config/routing.py"
               data-name="302-release-textual-tweaks"
               data-skip-pjax="true"
               rel="nofollow">
              <svg aria-hidden="true" class="octicon octicon-check select-menu-item-icon" height="16" version="1.1" viewBox="0 0 12 16" width="12"><path fill-rule="evenodd" d="M12 5l-8 8-4-4 1.5-1.5L4 10l6.5-6.5z"/></svg>
              <span class="select-menu-item-text css-truncate-target js-select-menu-filter-text">
                302-release-textual-tweaks
              </span>
            </a>
            <a class="select-menu-item js-navigation-item js-navigation-open "
               href="/ckan/ckan/blob/307-translation-review/ckan/config/routing.py"
               data-name="307-translation-review"
               data-skip-pjax="true"
               rel="nofollow">
              <svg aria-hidden="true" class="octicon octicon-check select-menu-item-icon" height="16" version="1.1" viewBox="0 0 12 16" width="12"><path fill-rule="evenodd" d="M12 5l-8 8-4-4 1.5-1.5L4 10l6.5-6.5z"/></svg>
              <span class="select-menu-item-text css-truncate-target js-select-menu-filter-text">
                307-translation-review
              </span>
            </a>
            <a class="select-menu-item js-navigation-item js-navigation-open "
               href="/ckan/ckan/blob/309-package-private-everywhere/ckan/config/routing.py"
               data-name="309-package-private-everywhere"
               data-skip-pjax="true"
               rel="nofollow">
              <svg aria-hidden="true" class="octicon octicon-check select-menu-item-icon" height="16" version="1.1" viewBox="0 0 12 16" width="12"><path fill-rule="evenodd" d="M12 5l-8 8-4-4 1.5-1.5L4 10l6.5-6.5z"/></svg>
              <span class="select-menu-item-text css-truncate-target js-select-menu-filter-text">
                309-package-private-everywhere
              </span>
            </a>
            <a class="select-menu-item js-navigation-item js-navigation-open "
               href="/ckan/ckan/blob/316-disable-follower-lists/ckan/config/routing.py"
               data-name="316-disable-follower-lists"
               data-skip-pjax="true"
               rel="nofollow">
              <svg aria-hidden="true" class="octicon octicon-check select-menu-item-icon" height="16" version="1.1" viewBox="0 0 12 16" width="12"><path fill-rule="evenodd" d="M12 5l-8 8-4-4 1.5-1.5L4 10l6.5-6.5z"/></svg>
              <span class="select-menu-item-text css-truncate-target js-select-menu-filter-text">
                316-disable-follower-lists
              </span>
            </a>
            <a class="select-menu-item js-navigation-item js-navigation-open "
               href="/ckan/ckan/blob/318-remove-popovers/ckan/config/routing.py"
               data-name="318-remove-popovers"
               data-skip-pjax="true"
               rel="nofollow">
              <svg aria-hidden="true" class="octicon octicon-check select-menu-item-icon" height="16" version="1.1" viewBox="0 0 12 16" width="12"><path fill-rule="evenodd" d="M12 5l-8 8-4-4 1.5-1.5L4 10l6.5-6.5z"/></svg>
              <span class="select-menu-item-text css-truncate-target js-select-menu-filter-text">
                318-remove-popovers
              </span>
            </a>
            <a class="select-menu-item js-navigation-item js-navigation-open "
               href="/ckan/ckan/blob/319-taggable-input-error-state/ckan/config/routing.py"
               data-name="319-taggable-input-error-state"
               data-skip-pjax="true"
               rel="nofollow">
              <svg aria-hidden="true" class="octicon octicon-check select-menu-item-icon" height="16" version="1.1" viewBox="0 0 12 16" width="12"><path fill-rule="evenodd" d="M12 5l-8 8-4-4 1.5-1.5L4 10l6.5-6.5z"/></svg>
              <span class="select-menu-item-text css-truncate-target js-select-menu-filter-text">
                319-taggable-input-error-state
              </span>
            </a>
            <a class="select-menu-item js-navigation-item js-navigation-open "
               href="/ckan/ckan/blob/322-show-organizations-on-dataset/ckan/config/routing.py"
               data-name="322-show-organizations-on-dataset"
               data-skip-pjax="true"
               rel="nofollow">
              <svg aria-hidden="true" class="octicon octicon-check select-menu-item-icon" height="16" version="1.1" viewBox="0 0 12 16" width="12"><path fill-rule="evenodd" d="M12 5l-8 8-4-4 1.5-1.5L4 10l6.5-6.5z"/></svg>
              <span class="select-menu-item-text css-truncate-target js-select-menu-filter-text">
                322-show-organizations-on-dataset
              </span>
            </a>
            <a class="select-menu-item js-navigation-item js-navigation-open "
               href="/ckan/ckan/blob/328-remove-administrators-from-group/ckan/config/routing.py"
               data-name="328-remove-administrators-from-group"
               data-skip-pjax="true"
               rel="nofollow">
              <svg aria-hidden="true" class="octicon octicon-check select-menu-item-icon" height="16" version="1.1" viewBox="0 0 12 16" width="12"><path fill-rule="evenodd" d="M12 5l-8 8-4-4 1.5-1.5L4 10l6.5-6.5z"/></svg>
              <span class="select-menu-item-text css-truncate-target js-select-menu-filter-text">
                328-remove-administrators-from-group
              </span>
            </a>
            <a class="select-menu-item js-navigation-item js-navigation-open "
               href="/ckan/ckan/blob/330-fix-gitignore/ckan/config/routing.py"
               data-name="330-fix-gitignore"
               data-skip-pjax="true"
               rel="nofollow">
              <svg aria-hidden="true" class="octicon octicon-check select-menu-item-icon" height="16" version="1.1" viewBox="0 0 12 16" width="12"><path fill-rule="evenodd" d="M12 5l-8 8-4-4 1.5-1.5L4 10l6.5-6.5z"/></svg>
              <span class="select-menu-item-text css-truncate-target js-select-menu-filter-text">
                330-fix-gitignore
              </span>
            </a>
            <a class="select-menu-item js-navigation-item js-navigation-open "
               href="/ckan/ckan/blob/336-337-organizations-template-tweaks/ckan/config/routing.py"
               data-name="336-337-organizations-template-tweaks"
               data-skip-pjax="true"
               rel="nofollow">
              <svg aria-hidden="true" class="octicon octicon-check select-menu-item-icon" height="16" version="1.1" viewBox="0 0 12 16" width="12"><path fill-rule="evenodd" d="M12 5l-8 8-4-4 1.5-1.5L4 10l6.5-6.5z"/></svg>
              <span class="select-menu-item-text css-truncate-target js-select-menu-filter-text">
                336-337-organizations-template-tweaks
              </span>
            </a>
            <a class="select-menu-item js-navigation-item js-navigation-open "
               href="/ckan/ckan/blob/344-page-param-positive-check/ckan/config/routing.py"
               data-name="344-page-param-positive-check"
               data-skip-pjax="true"
               rel="nofollow">
              <svg aria-hidden="true" class="octicon octicon-check select-menu-item-icon" height="16" version="1.1" viewBox="0 0 12 16" width="12"><path fill-rule="evenodd" d="M12 5l-8 8-4-4 1.5-1.5L4 10l6.5-6.5z"/></svg>
              <span class="select-menu-item-text css-truncate-target js-select-menu-filter-text">
                344-page-param-positive-check
              </span>
            </a>
            <a class="select-menu-item js-navigation-item js-navigation-open "
               href="/ckan/ckan/blob/345-fix-pg-detection/ckan/config/routing.py"
               data-name="345-fix-pg-detection"
               data-skip-pjax="true"
               rel="nofollow">
              <svg aria-hidden="true" class="octicon octicon-check select-menu-item-icon" height="16" version="1.1" viewBox="0 0 12 16" width="12"><path fill-rule="evenodd" d="M12 5l-8 8-4-4 1.5-1.5L4 10l6.5-6.5z"/></svg>
              <span class="select-menu-item-text css-truncate-target js-select-menu-filter-text">
                345-fix-pg-detection
              </span>
            </a>
            <a class="select-menu-item js-navigation-item js-navigation-open "
               href="/ckan/ckan/blob/349-old-auth-cleanups/ckan/config/routing.py"
               data-name="349-old-auth-cleanups"
               data-skip-pjax="true"
               rel="nofollow">
              <svg aria-hidden="true" class="octicon octicon-check select-menu-item-icon" height="16" version="1.1" viewBox="0 0 12 16" width="12"><path fill-rule="evenodd" d="M12 5l-8 8-4-4 1.5-1.5L4 10l6.5-6.5z"/></svg>
              <span class="select-menu-item-text css-truncate-target js-select-menu-filter-text">
                349-old-auth-cleanups
              </span>
            </a>
            <a class="select-menu-item js-navigation-item js-navigation-open "
               href="/ckan/ckan/blob/352/ckan/config/routing.py"
               data-name="352"
               data-skip-pjax="true"
               rel="nofollow">
              <svg aria-hidden="true" class="octicon octicon-check select-menu-item-icon" height="16" version="1.1" viewBox="0 0 12 16" width="12"><path fill-rule="evenodd" d="M12 5l-8 8-4-4 1.5-1.5L4 10l6.5-6.5z"/></svg>
              <span class="select-menu-item-text css-truncate-target js-select-menu-filter-text">
                352
              </span>
            </a>
            <a class="select-menu-item js-navigation-item js-navigation-open "
               href="/ckan/ckan/blob/354-ia-review/ckan/config/routing.py"
               data-name="354-ia-review"
               data-skip-pjax="true"
               rel="nofollow">
              <svg aria-hidden="true" class="octicon octicon-check select-menu-item-icon" height="16" version="1.1" viewBox="0 0 12 16" width="12"><path fill-rule="evenodd" d="M12 5l-8 8-4-4 1.5-1.5L4 10l6.5-6.5z"/></svg>
              <span class="select-menu-item-text css-truncate-target js-select-menu-filter-text">
                354-ia-review
              </span>
            </a>
            <a class="select-menu-item js-navigation-item js-navigation-open "
               href="/ckan/ckan/blob/362-remove-old-datastore/ckan/config/routing.py"
               data-name="362-remove-old-datastore"
               data-skip-pjax="true"
               rel="nofollow">
              <svg aria-hidden="true" class="octicon octicon-check select-menu-item-icon" height="16" version="1.1" viewBox="0 0 12 16" width="12"><path fill-rule="evenodd" d="M12 5l-8 8-4-4 1.5-1.5L4 10l6.5-6.5z"/></svg>
              <span class="select-menu-item-text css-truncate-target js-select-menu-filter-text">
                362-remove-old-datastore
              </span>
            </a>
            <a class="select-menu-item js-navigation-item js-navigation-open "
               href="/ckan/ckan/blob/364-private-datasets/ckan/config/routing.py"
               data-name="364-private-datasets"
               data-skip-pjax="true"
               rel="nofollow">
              <svg aria-hidden="true" class="octicon octicon-check select-menu-item-icon" height="16" version="1.1" viewBox="0 0 12 16" width="12"><path fill-rule="evenodd" d="M12 5l-8 8-4-4 1.5-1.5L4 10l6.5-6.5z"/></svg>
              <span class="select-menu-item-text css-truncate-target js-select-menu-filter-text">
                364-private-datasets
              </span>
            </a>
            <a class="select-menu-item js-navigation-item js-navigation-open "
               href="/ckan/ckan/blob/368-new-history-page-2/ckan/config/routing.py"
               data-name="368-new-history-page-2"
               data-skip-pjax="true"
               rel="nofollow">
              <svg aria-hidden="true" class="octicon octicon-check select-menu-item-icon" height="16" version="1.1" viewBox="0 0 12 16" width="12"><path fill-rule="evenodd" d="M12 5l-8 8-4-4 1.5-1.5L4 10l6.5-6.5z"/></svg>
              <span class="select-menu-item-text css-truncate-target js-select-menu-filter-text">
                368-new-history-page-2
              </span>
            </a>
            <a class="select-menu-item js-navigation-item js-navigation-open "
               href="/ckan/ckan/blob/368-new-history-page/ckan/config/routing.py"
               data-name="368-new-history-page"
               data-skip-pjax="true"
               rel="nofollow">
              <svg aria-hidden="true" class="octicon octicon-check select-menu-item-icon" height="16" version="1.1" viewBox="0 0 12 16" width="12"><path fill-rule="evenodd" d="M12 5l-8 8-4-4 1.5-1.5L4 10l6.5-6.5z"/></svg>
              <span class="select-menu-item-text css-truncate-target js-select-menu-filter-text">
                368-new-history-page
              </span>
            </a>
            <a class="select-menu-item js-navigation-item js-navigation-open "
               href="/ckan/ckan/blob/369-update-package-read-issue/ckan/config/routing.py"
               data-name="369-update-package-read-issue"
               data-skip-pjax="true"
               rel="nofollow">
              <svg aria-hidden="true" class="octicon octicon-check select-menu-item-icon" height="16" version="1.1" viewBox="0 0 12 16" width="12"><path fill-rule="evenodd" d="M12 5l-8 8-4-4 1.5-1.5L4 10l6.5-6.5z"/></svg>
              <span class="select-menu-item-text css-truncate-target js-select-menu-filter-text">
                369-update-package-read-issue
              </span>
            </a>
            <a class="select-menu-item js-navigation-item js-navigation-open "
               href="/ckan/ckan/blob/373_do_not_strip_tracking_summary/ckan/config/routing.py"
               data-name="373_do_not_strip_tracking_summary"
               data-skip-pjax="true"
               rel="nofollow">
              <svg aria-hidden="true" class="octicon octicon-check select-menu-item-icon" height="16" version="1.1" viewBox="0 0 12 16" width="12"><path fill-rule="evenodd" d="M12 5l-8 8-4-4 1.5-1.5L4 10l6.5-6.5z"/></svg>
              <span class="select-menu-item-text css-truncate-target js-select-menu-filter-text">
                373_do_not_strip_tracking_summary
              </span>
            </a>
            <a class="select-menu-item js-navigation-item js-navigation-open "
               href="/ckan/ckan/blob/374-update-recline/ckan/config/routing.py"
               data-name="374-update-recline"
               data-skip-pjax="true"
               rel="nofollow">
              <svg aria-hidden="true" class="octicon octicon-check select-menu-item-icon" height="16" version="1.1" viewBox="0 0 12 16" width="12"><path fill-rule="evenodd" d="M12 5l-8 8-4-4 1.5-1.5L4 10l6.5-6.5z"/></svg>
              <span class="select-menu-item-text css-truncate-target js-select-menu-filter-text">
                374-update-recline
              </span>
            </a>
            <a class="select-menu-item js-navigation-item js-navigation-open "
               href="/ckan/ckan/blob/379-g.plugins-empty/ckan/config/routing.py"
               data-name="379-g.plugins-empty"
               data-skip-pjax="true"
               rel="nofollow">
              <svg aria-hidden="true" class="octicon octicon-check select-menu-item-icon" height="16" version="1.1" viewBox="0 0 12 16" width="12"><path fill-rule="evenodd" d="M12 5l-8 8-4-4 1.5-1.5L4 10l6.5-6.5z"/></svg>
              <span class="select-menu-item-text css-truncate-target js-select-menu-filter-text">
                379-g.plugins-empty
              </span>
            </a>
            <a class="select-menu-item js-navigation-item js-navigation-open "
               href="/ckan/ckan/blob/381-convert-from-extras-quoting/ckan/config/routing.py"
               data-name="381-convert-from-extras-quoting"
               data-skip-pjax="true"
               rel="nofollow">
              <svg aria-hidden="true" class="octicon octicon-check select-menu-item-icon" height="16" version="1.1" viewBox="0 0 12 16" width="12"><path fill-rule="evenodd" d="M12 5l-8 8-4-4 1.5-1.5L4 10l6.5-6.5z"/></svg>
              <span class="select-menu-item-text css-truncate-target js-select-menu-filter-text">
                381-convert-from-extras-quoting
              </span>
            </a>
            <a class="select-menu-item js-navigation-item js-navigation-open "
               href="/ckan/ckan/blob/385-dont-minify-vendor-directories/ckan/config/routing.py"
               data-name="385-dont-minify-vendor-directories"
               data-skip-pjax="true"
               rel="nofollow">
              <svg aria-hidden="true" class="octicon octicon-check select-menu-item-icon" height="16" version="1.1" viewBox="0 0 12 16" width="12"><path fill-rule="evenodd" d="M12 5l-8 8-4-4 1.5-1.5L4 10l6.5-6.5z"/></svg>
              <span class="select-menu-item-text css-truncate-target js-select-menu-filter-text">
                385-dont-minify-vendor-directories
              </span>
            </a>
            <a class="select-menu-item js-navigation-item js-navigation-open "
               href="/ckan/ckan/blob/387-wrong-redirect-after-edit-dataset-slug/ckan/config/routing.py"
               data-name="387-wrong-redirect-after-edit-dataset-slug"
               data-skip-pjax="true"
               rel="nofollow">
              <svg aria-hidden="true" class="octicon octicon-check select-menu-item-icon" height="16" version="1.1" viewBox="0 0 12 16" width="12"><path fill-rule="evenodd" d="M12 5l-8 8-4-4 1.5-1.5L4 10l6.5-6.5z"/></svg>
              <span class="select-menu-item-text css-truncate-target js-select-menu-filter-text">
                387-wrong-redirect-after-edit-dataset-slug
              </span>
            </a>
            <a class="select-menu-item js-navigation-item js-navigation-open "
               href="/ckan/ckan/blob/397-cleanup-public-dir/ckan/config/routing.py"
               data-name="397-cleanup-public-dir"
               data-skip-pjax="true"
               rel="nofollow">
              <svg aria-hidden="true" class="octicon octicon-check select-menu-item-icon" height="16" version="1.1" viewBox="0 0 12 16" width="12"><path fill-rule="evenodd" d="M12 5l-8 8-4-4 1.5-1.5L4 10l6.5-6.5z"/></svg>
              <span class="select-menu-item-text css-truncate-target js-select-menu-filter-text">
                397-cleanup-public-dir
              </span>
            </a>
            <a class="select-menu-item js-navigation-item js-navigation-open "
               href="/ckan/ckan/blob/398-delete-org-fix/ckan/config/routing.py"
               data-name="398-delete-org-fix"
               data-skip-pjax="true"
               rel="nofollow">
              <svg aria-hidden="true" class="octicon octicon-check select-menu-item-icon" height="16" version="1.1" viewBox="0 0 12 16" width="12"><path fill-rule="evenodd" d="M12 5l-8 8-4-4 1.5-1.5L4 10l6.5-6.5z"/></svg>
              <span class="select-menu-item-text css-truncate-target js-select-menu-filter-text">
                398-delete-org-fix
              </span>
            </a>
            <a class="select-menu-item js-navigation-item js-navigation-open "
               href="/ckan/ckan/blob/408-remove-legacy-org-code/ckan/config/routing.py"
               data-name="408-remove-legacy-org-code"
               data-skip-pjax="true"
               rel="nofollow">
              <svg aria-hidden="true" class="octicon octicon-check select-menu-item-icon" height="16" version="1.1" viewBox="0 0 12 16" width="12"><path fill-rule="evenodd" d="M12 5l-8 8-4-4 1.5-1.5L4 10l6.5-6.5z"/></svg>
              <span class="select-menu-item-text css-truncate-target js-select-menu-filter-text">
                408-remove-legacy-org-code
              </span>
            </a>
            <a class="select-menu-item js-navigation-item js-navigation-open "
               href="/ckan/ckan/blob/409-kill-old-admin/ckan/config/routing.py"
               data-name="409-kill-old-admin"
               data-skip-pjax="true"
               rel="nofollow">
              <svg aria-hidden="true" class="octicon octicon-check select-menu-item-icon" height="16" version="1.1" viewBox="0 0 12 16" width="12"><path fill-rule="evenodd" d="M12 5l-8 8-4-4 1.5-1.5L4 10l6.5-6.5z"/></svg>
              <span class="select-menu-item-text css-truncate-target js-select-menu-filter-text">
                409-kill-old-admin
              </span>
            </a>
            <a class="select-menu-item js-navigation-item js-navigation-open "
               href="/ckan/ckan/blob/411-sql-only-search-no-solr/ckan/config/routing.py"
               data-name="411-sql-only-search-no-solr"
               data-skip-pjax="true"
               rel="nofollow">
              <svg aria-hidden="true" class="octicon octicon-check select-menu-item-icon" height="16" version="1.1" viewBox="0 0 12 16" width="12"><path fill-rule="evenodd" d="M12 5l-8 8-4-4 1.5-1.5L4 10l6.5-6.5z"/></svg>
              <span class="select-menu-item-text css-truncate-target js-select-menu-filter-text">
                411-sql-only-search-no-solr
              </span>
            </a>
            <a class="select-menu-item js-navigation-item js-navigation-open "
               href="/ckan/ckan/blob/421-tag-pages/ckan/config/routing.py"
               data-name="421-tag-pages"
               data-skip-pjax="true"
               rel="nofollow">
              <svg aria-hidden="true" class="octicon octicon-check select-menu-item-icon" height="16" version="1.1" viewBox="0 0 12 16" width="12"><path fill-rule="evenodd" d="M12 5l-8 8-4-4 1.5-1.5L4 10l6.5-6.5z"/></svg>
              <span class="select-menu-item-text css-truncate-target js-select-menu-filter-text">
                421-tag-pages
              </span>
            </a>
            <a class="select-menu-item js-navigation-item js-navigation-open "
               href="/ckan/ckan/blob/422-fanstatic-windows-compat/ckan/config/routing.py"
               data-name="422-fanstatic-windows-compat"
               data-skip-pjax="true"
               rel="nofollow">
              <svg aria-hidden="true" class="octicon octicon-check select-menu-item-icon" height="16" version="1.1" viewBox="0 0 12 16" width="12"><path fill-rule="evenodd" d="M12 5l-8 8-4-4 1.5-1.5L4 10l6.5-6.5z"/></svg>
              <span class="select-menu-item-text css-truncate-target js-select-menu-filter-text">
                422-fanstatic-windows-compat
              </span>
            </a>
            <a class="select-menu-item js-navigation-item js-navigation-open "
               href="/ckan/ckan/blob/426-recline-graph-fixes/ckan/config/routing.py"
               data-name="426-recline-graph-fixes"
               data-skip-pjax="true"
               rel="nofollow">
              <svg aria-hidden="true" class="octicon octicon-check select-menu-item-icon" height="16" version="1.1" viewBox="0 0 12 16" width="12"><path fill-rule="evenodd" d="M12 5l-8 8-4-4 1.5-1.5L4 10l6.5-6.5z"/></svg>
              <span class="select-menu-item-text css-truncate-target js-select-menu-filter-text">
                426-recline-graph-fixes
              </span>
            </a>
            <a class="select-menu-item js-navigation-item js-navigation-open "
               href="/ckan/ckan/blob/428-template-corruption-help/ckan/config/routing.py"
               data-name="428-template-corruption-help"
               data-skip-pjax="true"
               rel="nofollow">
              <svg aria-hidden="true" class="octicon octicon-check select-menu-item-icon" height="16" version="1.1" viewBox="0 0 12 16" width="12"><path fill-rule="evenodd" d="M12 5l-8 8-4-4 1.5-1.5L4 10l6.5-6.5z"/></svg>
              <span class="select-menu-item-text css-truncate-target js-select-menu-filter-text">
                428-template-corruption-help
              </span>
            </a>
            <a class="select-menu-item js-navigation-item js-navigation-open "
               href="/ckan/ckan/blob/430-packages-missing-vocabulary-show/ckan/config/routing.py"
               data-name="430-packages-missing-vocabulary-show"
               data-skip-pjax="true"
               rel="nofollow">
              <svg aria-hidden="true" class="octicon octicon-check select-menu-item-icon" height="16" version="1.1" viewBox="0 0 12 16" width="12"><path fill-rule="evenodd" d="M12 5l-8 8-4-4 1.5-1.5L4 10l6.5-6.5z"/></svg>
              <span class="select-menu-item-text css-truncate-target js-select-menu-filter-text">
                430-packages-missing-vocabulary-show
              </span>
            </a>
            <a class="select-menu-item js-navigation-item js-navigation-open "
               href="/ckan/ckan/blob/431-use-db-to-form-package-schema-by-default/ckan/config/routing.py"
               data-name="431-use-db-to-form-package-schema-by-default"
               data-skip-pjax="true"
               rel="nofollow">
              <svg aria-hidden="true" class="octicon octicon-check select-menu-item-icon" height="16" version="1.1" viewBox="0 0 12 16" width="12"><path fill-rule="evenodd" d="M12 5l-8 8-4-4 1.5-1.5L4 10l6.5-6.5z"/></svg>
              <span class="select-menu-item-text css-truncate-target js-select-menu-filter-text">
                431-use-db-to-form-package-schema-by-default
              </span>
            </a>
            <a class="select-menu-item js-navigation-item js-navigation-open "
               href="/ckan/ckan/blob/435-python-support-ordereddict/ckan/config/routing.py"
               data-name="435-python-support-ordereddict"
               data-skip-pjax="true"
               rel="nofollow">
              <svg aria-hidden="true" class="octicon octicon-check select-menu-item-icon" height="16" version="1.1" viewBox="0 0 12 16" width="12"><path fill-rule="evenodd" d="M12 5l-8 8-4-4 1.5-1.5L4 10l6.5-6.5z"/></svg>
              <span class="select-menu-item-text css-truncate-target js-select-menu-filter-text">
                435-python-support-ordereddict
              </span>
            </a>
            <a class="select-menu-item js-navigation-item js-navigation-open "
               href="/ckan/ckan/blob/436-unicode-filetype-fix-for-2.0/ckan/config/routing.py"
               data-name="436-unicode-filetype-fix-for-2.0"
               data-skip-pjax="true"
               rel="nofollow">
              <svg aria-hidden="true" class="octicon octicon-check select-menu-item-icon" height="16" version="1.1" viewBox="0 0 12 16" width="12"><path fill-rule="evenodd" d="M12 5l-8 8-4-4 1.5-1.5L4 10l6.5-6.5z"/></svg>
              <span class="select-menu-item-text css-truncate-target js-select-menu-filter-text">
                436-unicode-filetype-fix-for-2.0
              </span>
            </a>
            <a class="select-menu-item js-navigation-item js-navigation-open "
               href="/ckan/ckan/blob/438-less-issue/ckan/config/routing.py"
               data-name="438-less-issue"
               data-skip-pjax="true"
               rel="nofollow">
              <svg aria-hidden="true" class="octicon octicon-check select-menu-item-icon" height="16" version="1.1" viewBox="0 0 12 16" width="12"><path fill-rule="evenodd" d="M12 5l-8 8-4-4 1.5-1.5L4 10l6.5-6.5z"/></svg>
              <span class="select-menu-item-text css-truncate-target js-select-menu-filter-text">
                438-less-issue
              </span>
            </a>
            <a class="select-menu-item js-navigation-item js-navigation-open "
               href="/ckan/ckan/blob/439-travis-clean/ckan/config/routing.py"
               data-name="439-travis-clean"
               data-skip-pjax="true"
               rel="nofollow">
              <svg aria-hidden="true" class="octicon octicon-check select-menu-item-icon" height="16" version="1.1" viewBox="0 0 12 16" width="12"><path fill-rule="evenodd" d="M12 5l-8 8-4-4 1.5-1.5L4 10l6.5-6.5z"/></svg>
              <span class="select-menu-item-text css-truncate-target js-select-menu-filter-text">
                439-travis-clean
              </span>
            </a>
            <a class="select-menu-item js-navigation-item js-navigation-open "
               href="/ckan/ckan/blob/441-add-dataset/ckan/config/routing.py"
               data-name="441-add-dataset"
               data-skip-pjax="true"
               rel="nofollow">
              <svg aria-hidden="true" class="octicon octicon-check select-menu-item-icon" height="16" version="1.1" viewBox="0 0 12 16" width="12"><path fill-rule="evenodd" d="M12 5l-8 8-4-4 1.5-1.5L4 10l6.5-6.5z"/></svg>
              <span class="select-menu-item-text css-truncate-target js-select-menu-filter-text">
                441-add-dataset
              </span>
            </a>
            <a class="select-menu-item js-navigation-item js-navigation-open "
               href="/ckan/ckan/blob/445-bug-multilingual-tests-failing/ckan/config/routing.py"
               data-name="445-bug-multilingual-tests-failing"
               data-skip-pjax="true"
               rel="nofollow">
              <svg aria-hidden="true" class="octicon octicon-check select-menu-item-icon" height="16" version="1.1" viewBox="0 0 12 16" width="12"><path fill-rule="evenodd" d="M12 5l-8 8-4-4 1.5-1.5L4 10l6.5-6.5z"/></svg>
              <span class="select-menu-item-text css-truncate-target js-select-menu-filter-text">
                445-bug-multilingual-tests-failing
              </span>
            </a>
            <a class="select-menu-item js-navigation-item js-navigation-open "
               href="/ckan/ckan/blob/448-ia-tweaks/ckan/config/routing.py"
               data-name="448-ia-tweaks"
               data-skip-pjax="true"
               rel="nofollow">
              <svg aria-hidden="true" class="octicon octicon-check select-menu-item-icon" height="16" version="1.1" viewBox="0 0 12 16" width="12"><path fill-rule="evenodd" d="M12 5l-8 8-4-4 1.5-1.5L4 10l6.5-6.5z"/></svg>
              <span class="select-menu-item-text css-truncate-target js-select-menu-filter-text">
                448-ia-tweaks
              </span>
            </a>
            <a class="select-menu-item js-navigation-item js-navigation-open "
               href="/ckan/ckan/blob/451-form-labels/ckan/config/routing.py"
               data-name="451-form-labels"
               data-skip-pjax="true"
               rel="nofollow">
              <svg aria-hidden="true" class="octicon octicon-check select-menu-item-icon" height="16" version="1.1" viewBox="0 0 12 16" width="12"><path fill-rule="evenodd" d="M12 5l-8 8-4-4 1.5-1.5L4 10l6.5-6.5z"/></svg>
              <span class="select-menu-item-text css-truncate-target js-select-menu-filter-text">
                451-form-labels
              </span>
            </a>
            <a class="select-menu-item js-navigation-item js-navigation-open "
               href="/ckan/ckan/blob/460-named-routes-helper-function/ckan/config/routing.py"
               data-name="460-named-routes-helper-function"
               data-skip-pjax="true"
               rel="nofollow">
              <svg aria-hidden="true" class="octicon octicon-check select-menu-item-icon" height="16" version="1.1" viewBox="0 0 12 16" width="12"><path fill-rule="evenodd" d="M12 5l-8 8-4-4 1.5-1.5L4 10l6.5-6.5z"/></svg>
              <span class="select-menu-item-text css-truncate-target js-select-menu-filter-text">
                460-named-routes-helper-function
              </span>
            </a>
            <a class="select-menu-item js-navigation-item js-navigation-open "
               href="/ckan/ckan/blob/471-helper-clean-link-functions/ckan/config/routing.py"
               data-name="471-helper-clean-link-functions"
               data-skip-pjax="true"
               rel="nofollow">
              <svg aria-hidden="true" class="octicon octicon-check select-menu-item-icon" height="16" version="1.1" viewBox="0 0 12 16" width="12"><path fill-rule="evenodd" d="M12 5l-8 8-4-4 1.5-1.5L4 10l6.5-6.5z"/></svg>
              <span class="select-menu-item-text css-truncate-target js-select-menu-filter-text">
                471-helper-clean-link-functions
              </span>
            </a>
            <a class="select-menu-item js-navigation-item js-navigation-open "
               href="/ckan/ckan/blob/477-group-org-additional-info/ckan/config/routing.py"
               data-name="477-group-org-additional-info"
               data-skip-pjax="true"
               rel="nofollow">
              <svg aria-hidden="true" class="octicon octicon-check select-menu-item-icon" height="16" version="1.1" viewBox="0 0 12 16" width="12"><path fill-rule="evenodd" d="M12 5l-8 8-4-4 1.5-1.5L4 10l6.5-6.5z"/></svg>
              <span class="select-menu-item-text css-truncate-target js-select-menu-filter-text">
                477-group-org-additional-info
              </span>
            </a>
            <a class="select-menu-item js-navigation-item js-navigation-open "
               href="/ckan/ckan/blob/479-tests-for-example-idatasetform/ckan/config/routing.py"
               data-name="479-tests-for-example-idatasetform"
               data-skip-pjax="true"
               rel="nofollow">
              <svg aria-hidden="true" class="octicon octicon-check select-menu-item-icon" height="16" version="1.1" viewBox="0 0 12 16" width="12"><path fill-rule="evenodd" d="M12 5l-8 8-4-4 1.5-1.5L4 10l6.5-6.5z"/></svg>
              <span class="select-menu-item-text css-truncate-target js-select-menu-filter-text">
                479-tests-for-example-idatasetform
              </span>
            </a>
            <a class="select-menu-item js-navigation-item js-navigation-open "
               href="/ckan/ckan/blob/480-admins-dataset-private/ckan/config/routing.py"
               data-name="480-admins-dataset-private"
               data-skip-pjax="true"
               rel="nofollow">
              <svg aria-hidden="true" class="octicon octicon-check select-menu-item-icon" height="16" version="1.1" viewBox="0 0 12 16" width="12"><path fill-rule="evenodd" d="M12 5l-8 8-4-4 1.5-1.5L4 10l6.5-6.5z"/></svg>
              <span class="select-menu-item-text css-truncate-target js-select-menu-filter-text">
                480-admins-dataset-private
              </span>
            </a>
            <a class="select-menu-item js-navigation-item js-navigation-open "
               href="/ckan/ckan/blob/482-plugin-validator-converter-access/ckan/config/routing.py"
               data-name="482-plugin-validator-converter-access"
               data-skip-pjax="true"
               rel="nofollow">
              <svg aria-hidden="true" class="octicon octicon-check select-menu-item-icon" height="16" version="1.1" viewBox="0 0 12 16" width="12"><path fill-rule="evenodd" d="M12 5l-8 8-4-4 1.5-1.5L4 10l6.5-6.5z"/></svg>
              <span class="select-menu-item-text css-truncate-target js-select-menu-filter-text">
                482-plugin-validator-converter-access
              </span>
            </a>
            <a class="select-menu-item js-navigation-item js-navigation-open "
               href="/ckan/ckan/blob/484-upgrade-requests/ckan/config/routing.py"
               data-name="484-upgrade-requests"
               data-skip-pjax="true"
               rel="nofollow">
              <svg aria-hidden="true" class="octicon octicon-check select-menu-item-icon" height="16" version="1.1" viewBox="0 0 12 16" width="12"><path fill-rule="evenodd" d="M12 5l-8 8-4-4 1.5-1.5L4 10l6.5-6.5z"/></svg>
              <span class="select-menu-item-text css-truncate-target js-select-menu-filter-text">
                484-upgrade-requests
              </span>
            </a>
            <a class="select-menu-item js-navigation-item js-navigation-open "
               href="/ckan/ckan/blob/485-monochrome-icons/ckan/config/routing.py"
               data-name="485-monochrome-icons"
               data-skip-pjax="true"
               rel="nofollow">
              <svg aria-hidden="true" class="octicon octicon-check select-menu-item-icon" height="16" version="1.1" viewBox="0 0 12 16" width="12"><path fill-rule="evenodd" d="M12 5l-8 8-4-4 1.5-1.5L4 10l6.5-6.5z"/></svg>
              <span class="select-menu-item-text css-truncate-target js-select-menu-filter-text">
                485-monochrome-icons
              </span>
            </a>
            <a class="select-menu-item js-navigation-item js-navigation-open "
               href="/ckan/ckan/blob/486-footer-template/ckan/config/routing.py"
               data-name="486-footer-template"
               data-skip-pjax="true"
               rel="nofollow">
              <svg aria-hidden="true" class="octicon octicon-check select-menu-item-icon" height="16" version="1.1" viewBox="0 0 12 16" width="12"><path fill-rule="evenodd" d="M12 5l-8 8-4-4 1.5-1.5L4 10l6.5-6.5z"/></svg>
              <span class="select-menu-item-text css-truncate-target js-select-menu-filter-text">
                486-footer-template
              </span>
            </a>
            <a class="select-menu-item js-navigation-item js-navigation-open "
               href="/ckan/ckan/blob/487-search-no-results/ckan/config/routing.py"
               data-name="487-search-no-results"
               data-skip-pjax="true"
               rel="nofollow">
              <svg aria-hidden="true" class="octicon octicon-check select-menu-item-icon" height="16" version="1.1" viewBox="0 0 12 16" width="12"><path fill-rule="evenodd" d="M12 5l-8 8-4-4 1.5-1.5L4 10l6.5-6.5z"/></svg>
              <span class="select-menu-item-text css-truncate-target js-select-menu-filter-text">
                487-search-no-results
              </span>
            </a>
            <a class="select-menu-item js-navigation-item js-navigation-open "
               href="/ckan/ckan/blob/491-resolve-pip-requirements/ckan/config/routing.py"
               data-name="491-resolve-pip-requirements"
               data-skip-pjax="true"
               rel="nofollow">
              <svg aria-hidden="true" class="octicon octicon-check select-menu-item-icon" height="16" version="1.1" viewBox="0 0 12 16" width="12"><path fill-rule="evenodd" d="M12 5l-8 8-4-4 1.5-1.5L4 10l6.5-6.5z"/></svg>
              <span class="select-menu-item-text css-truncate-target js-select-menu-filter-text">
                491-resolve-pip-requirements
              </span>
            </a>
            <a class="select-menu-item js-navigation-item js-navigation-open "
               href="/ckan/ckan/blob/494-org-500-take2/ckan/config/routing.py"
               data-name="494-org-500-take2"
               data-skip-pjax="true"
               rel="nofollow">
              <svg aria-hidden="true" class="octicon octicon-check select-menu-item-icon" height="16" version="1.1" viewBox="0 0 12 16" width="12"><path fill-rule="evenodd" d="M12 5l-8 8-4-4 1.5-1.5L4 10l6.5-6.5z"/></svg>
              <span class="select-menu-item-text css-truncate-target js-select-menu-filter-text">
                494-org-500-take2
              </span>
            </a>
            <a class="select-menu-item js-navigation-item js-navigation-open "
               href="/ckan/ckan/blob/494-org-500/ckan/config/routing.py"
               data-name="494-org-500"
               data-skip-pjax="true"
               rel="nofollow">
              <svg aria-hidden="true" class="octicon octicon-check select-menu-item-icon" height="16" version="1.1" viewBox="0 0 12 16" width="12"><path fill-rule="evenodd" d="M12 5l-8 8-4-4 1.5-1.5L4 10l6.5-6.5z"/></svg>
              <span class="select-menu-item-text css-truncate-target js-select-menu-filter-text">
                494-org-500
              </span>
            </a>
            <a class="select-menu-item js-navigation-item js-navigation-open "
               href="/ckan/ckan/blob/500-featured-image-custom/ckan/config/routing.py"
               data-name="500-featured-image-custom"
               data-skip-pjax="true"
               rel="nofollow">
              <svg aria-hidden="true" class="octicon octicon-check select-menu-item-icon" height="16" version="1.1" viewBox="0 0 12 16" width="12"><path fill-rule="evenodd" d="M12 5l-8 8-4-4 1.5-1.5L4 10l6.5-6.5z"/></svg>
              <span class="select-menu-item-text css-truncate-target js-select-menu-filter-text">
                500-featured-image-custom
              </span>
            </a>
            <a class="select-menu-item js-navigation-item js-navigation-open "
               href="/ckan/ckan/blob/505-organizations-activity-streams/ckan/config/routing.py"
               data-name="505-organizations-activity-streams"
               data-skip-pjax="true"
               rel="nofollow">
              <svg aria-hidden="true" class="octicon octicon-check select-menu-item-icon" height="16" version="1.1" viewBox="0 0 12 16" width="12"><path fill-rule="evenodd" d="M12 5l-8 8-4-4 1.5-1.5L4 10l6.5-6.5z"/></svg>
              <span class="select-menu-item-text css-truncate-target js-select-menu-filter-text">
                505-organizations-activity-streams
              </span>
            </a>
            <a class="select-menu-item js-navigation-item js-navigation-open "
               href="/ckan/ckan/blob/507-template-cache-reset/ckan/config/routing.py"
               data-name="507-template-cache-reset"
               data-skip-pjax="true"
               rel="nofollow">
              <svg aria-hidden="true" class="octicon octicon-check select-menu-item-icon" height="16" version="1.1" viewBox="0 0 12 16" width="12"><path fill-rule="evenodd" d="M12 5l-8 8-4-4 1.5-1.5L4 10l6.5-6.5z"/></svg>
              <span class="select-menu-item-text css-truncate-target js-select-menu-filter-text">
                507-template-cache-reset
              </span>
            </a>
            <a class="select-menu-item js-navigation-item js-navigation-open "
               href="/ckan/ckan/blob/509-group-add-remove/ckan/config/routing.py"
               data-name="509-group-add-remove"
               data-skip-pjax="true"
               rel="nofollow">
              <svg aria-hidden="true" class="octicon octicon-check select-menu-item-icon" height="16" version="1.1" viewBox="0 0 12 16" width="12"><path fill-rule="evenodd" d="M12 5l-8 8-4-4 1.5-1.5L4 10l6.5-6.5z"/></svg>
              <span class="select-menu-item-text css-truncate-target js-select-menu-filter-text">
                509-group-add-remove
              </span>
            </a>
            <a class="select-menu-item js-navigation-item js-navigation-open "
               href="/ckan/ckan/blob/511-resource-url-on-resource-page/ckan/config/routing.py"
               data-name="511-resource-url-on-resource-page"
               data-skip-pjax="true"
               rel="nofollow">
              <svg aria-hidden="true" class="octicon octicon-check select-menu-item-icon" height="16" version="1.1" viewBox="0 0 12 16" width="12"><path fill-rule="evenodd" d="M12 5l-8 8-4-4 1.5-1.5L4 10l6.5-6.5z"/></svg>
              <span class="select-menu-item-text css-truncate-target js-select-menu-filter-text">
                511-resource-url-on-resource-page
              </span>
            </a>
            <a class="select-menu-item js-navigation-item js-navigation-open "
               href="/ckan/ckan/blob/515-org-group-search-issue/ckan/config/routing.py"
               data-name="515-org-group-search-issue"
               data-skip-pjax="true"
               rel="nofollow">
              <svg aria-hidden="true" class="octicon octicon-check select-menu-item-icon" height="16" version="1.1" viewBox="0 0 12 16" width="12"><path fill-rule="evenodd" d="M12 5l-8 8-4-4 1.5-1.5L4 10l6.5-6.5z"/></svg>
              <span class="select-menu-item-text css-truncate-target js-select-menu-filter-text">
                515-org-group-search-issue
              </span>
            </a>
            <a class="select-menu-item js-navigation-item js-navigation-open "
               href="/ckan/ckan/blob/517-test-db/ckan/config/routing.py"
               data-name="517-test-db"
               data-skip-pjax="true"
               rel="nofollow">
              <svg aria-hidden="true" class="octicon octicon-check select-menu-item-icon" height="16" version="1.1" viewBox="0 0 12 16" width="12"><path fill-rule="evenodd" d="M12 5l-8 8-4-4 1.5-1.5L4 10l6.5-6.5z"/></svg>
              <span class="select-menu-item-text css-truncate-target js-select-menu-filter-text">
                517-test-db
              </span>
            </a>
            <a class="select-menu-item js-navigation-item js-navigation-open "
               href="/ckan/ckan/blob/518-date-time-within-activity-streams/ckan/config/routing.py"
               data-name="518-date-time-within-activity-streams"
               data-skip-pjax="true"
               rel="nofollow">
              <svg aria-hidden="true" class="octicon octicon-check select-menu-item-icon" height="16" version="1.1" viewBox="0 0 12 16" width="12"><path fill-rule="evenodd" d="M12 5l-8 8-4-4 1.5-1.5L4 10l6.5-6.5z"/></svg>
              <span class="select-menu-item-text css-truncate-target js-select-menu-filter-text">
                518-date-time-within-activity-streams
              </span>
            </a>
            <a class="select-menu-item js-navigation-item js-navigation-open "
               href="/ckan/ckan/blob/519-update-deployment-docs/ckan/config/routing.py"
               data-name="519-update-deployment-docs"
               data-skip-pjax="true"
               rel="nofollow">
              <svg aria-hidden="true" class="octicon octicon-check select-menu-item-icon" height="16" version="1.1" viewBox="0 0 12 16" width="12"><path fill-rule="evenodd" d="M12 5l-8 8-4-4 1.5-1.5L4 10l6.5-6.5z"/></svg>
              <span class="select-menu-item-text css-truncate-target js-select-menu-filter-text">
                519-update-deployment-docs
              </span>
            </a>
            <a class="select-menu-item js-navigation-item js-navigation-open "
               href="/ckan/ckan/blob/520-templating-docs-with-imports/ckan/config/routing.py"
               data-name="520-templating-docs-with-imports"
               data-skip-pjax="true"
               rel="nofollow">
              <svg aria-hidden="true" class="octicon octicon-check select-menu-item-icon" height="16" version="1.1" viewBox="0 0 12 16" width="12"><path fill-rule="evenodd" d="M12 5l-8 8-4-4 1.5-1.5L4 10l6.5-6.5z"/></svg>
              <span class="select-menu-item-text css-truncate-target js-select-menu-filter-text">
                520-templating-docs-with-imports
              </span>
            </a>
            <a class="select-menu-item js-navigation-item js-navigation-open "
               href="/ckan/ckan/blob/528-docs-publishing-datasets/ckan/config/routing.py"
               data-name="528-docs-publishing-datasets"
               data-skip-pjax="true"
               rel="nofollow">
              <svg aria-hidden="true" class="octicon octicon-check select-menu-item-icon" height="16" version="1.1" viewBox="0 0 12 16" width="12"><path fill-rule="evenodd" d="M12 5l-8 8-4-4 1.5-1.5L4 10l6.5-6.5z"/></svg>
              <span class="select-menu-item-text css-truncate-target js-select-menu-filter-text">
                528-docs-publishing-datasets
              </span>
            </a>
            <a class="select-menu-item js-navigation-item js-navigation-open "
               href="/ckan/ckan/blob/529-docs-import-datasets/ckan/config/routing.py"
               data-name="529-docs-import-datasets"
               data-skip-pjax="true"
               rel="nofollow">
              <svg aria-hidden="true" class="octicon octicon-check select-menu-item-icon" height="16" version="1.1" viewBox="0 0 12 16" width="12"><path fill-rule="evenodd" d="M12 5l-8 8-4-4 1.5-1.5L4 10l6.5-6.5z"/></svg>
              <span class="select-menu-item-text css-truncate-target js-select-menu-filter-text">
                529-docs-import-datasets
              </span>
            </a>
            <a class="select-menu-item js-navigation-item js-navigation-open "
               href="/ckan/ckan/blob/532-update-ckan-admin-dashboard-doc/ckan/config/routing.py"
               data-name="532-update-ckan-admin-dashboard-doc"
               data-skip-pjax="true"
               rel="nofollow">
              <svg aria-hidden="true" class="octicon octicon-check select-menu-item-icon" height="16" version="1.1" viewBox="0 0 12 16" width="12"><path fill-rule="evenodd" d="M12 5l-8 8-4-4 1.5-1.5L4 10l6.5-6.5z"/></svg>
              <span class="select-menu-item-text css-truncate-target js-select-menu-filter-text">
                532-update-ckan-admin-dashboard-doc
              </span>
            </a>
            <a class="select-menu-item js-navigation-item js-navigation-open "
               href="/ckan/ckan/blob/538-package-install-docs/ckan/config/routing.py"
               data-name="538-package-install-docs"
               data-skip-pjax="true"
               rel="nofollow">
              <svg aria-hidden="true" class="octicon octicon-check select-menu-item-icon" height="16" version="1.1" viewBox="0 0 12 16" width="12"><path fill-rule="evenodd" d="M12 5l-8 8-4-4 1.5-1.5L4 10l6.5-6.5z"/></svg>
              <span class="select-menu-item-text css-truncate-target js-select-menu-filter-text">
                538-package-install-docs
              </span>
            </a>
            <a class="select-menu-item js-navigation-item js-navigation-open "
               href="/ckan/ckan/blob/546-get-actions-no-params/ckan/config/routing.py"
               data-name="546-get-actions-no-params"
               data-skip-pjax="true"
               rel="nofollow">
              <svg aria-hidden="true" class="octicon octicon-check select-menu-item-icon" height="16" version="1.1" viewBox="0 0 12 16" width="12"><path fill-rule="evenodd" d="M12 5l-8 8-4-4 1.5-1.5L4 10l6.5-6.5z"/></svg>
              <span class="select-menu-item-text css-truncate-target js-select-menu-filter-text">
                546-get-actions-no-params
              </span>
            </a>
            <a class="select-menu-item js-navigation-item js-navigation-open "
               href="/ckan/ckan/blob/548-password-reset-fix/ckan/config/routing.py"
               data-name="548-password-reset-fix"
               data-skip-pjax="true"
               rel="nofollow">
              <svg aria-hidden="true" class="octicon octicon-check select-menu-item-icon" height="16" version="1.1" viewBox="0 0 12 16" width="12"><path fill-rule="evenodd" d="M12 5l-8 8-4-4 1.5-1.5L4 10l6.5-6.5z"/></svg>
              <span class="select-menu-item-text css-truncate-target js-select-menu-filter-text">
                548-password-reset-fix
              </span>
            </a>
            <a class="select-menu-item js-navigation-item js-navigation-open "
               href="/ckan/ckan/blob/550-fix-paster-front-end-build/ckan/config/routing.py"
               data-name="550-fix-paster-front-end-build"
               data-skip-pjax="true"
               rel="nofollow">
              <svg aria-hidden="true" class="octicon octicon-check select-menu-item-icon" height="16" version="1.1" viewBox="0 0 12 16" width="12"><path fill-rule="evenodd" d="M12 5l-8 8-4-4 1.5-1.5L4 10l6.5-6.5z"/></svg>
              <span class="select-menu-item-text css-truncate-target js-select-menu-filter-text">
                550-fix-paster-front-end-build
              </span>
            </a>
            <a class="select-menu-item js-navigation-item js-navigation-open "
               href="/ckan/ckan/blob/552-page-header-tabs/ckan/config/routing.py"
               data-name="552-page-header-tabs"
               data-skip-pjax="true"
               rel="nofollow">
              <svg aria-hidden="true" class="octicon octicon-check select-menu-item-icon" height="16" version="1.1" viewBox="0 0 12 16" width="12"><path fill-rule="evenodd" d="M12 5l-8 8-4-4 1.5-1.5L4 10l6.5-6.5z"/></svg>
              <span class="select-menu-item-text css-truncate-target js-select-menu-filter-text">
                552-page-header-tabs
              </span>
            </a>
            <a class="select-menu-item js-navigation-item js-navigation-open "
               href="/ckan/ckan/blob/553-compare_domains-wrong-url/ckan/config/routing.py"
               data-name="553-compare_domains-wrong-url"
               data-skip-pjax="true"
               rel="nofollow">
              <svg aria-hidden="true" class="octicon octicon-check select-menu-item-icon" height="16" version="1.1" viewBox="0 0 12 16" width="12"><path fill-rule="evenodd" d="M12 5l-8 8-4-4 1.5-1.5L4 10l6.5-6.5z"/></svg>
              <span class="select-menu-item-text css-truncate-target js-select-menu-filter-text">
                553-compare_domains-wrong-url
              </span>
            </a>
            <a class="select-menu-item js-navigation-item js-navigation-open "
               href="/ckan/ckan/blob/558-no-nav-wrapper-class/ckan/config/routing.py"
               data-name="558-no-nav-wrapper-class"
               data-skip-pjax="true"
               rel="nofollow">
              <svg aria-hidden="true" class="octicon octicon-check select-menu-item-icon" height="16" version="1.1" viewBox="0 0 12 16" width="12"><path fill-rule="evenodd" d="M12 5l-8 8-4-4 1.5-1.5L4 10l6.5-6.5z"/></svg>
              <span class="select-menu-item-text css-truncate-target js-select-menu-filter-text">
                558-no-nav-wrapper-class
              </span>
            </a>
            <a class="select-menu-item js-navigation-item js-navigation-open "
               href="/ckan/ckan/blob/564-storage-controller-clean/ckan/config/routing.py"
               data-name="564-storage-controller-clean"
               data-skip-pjax="true"
               rel="nofollow">
              <svg aria-hidden="true" class="octicon octicon-check select-menu-item-icon" height="16" version="1.1" viewBox="0 0 12 16" width="12"><path fill-rule="evenodd" d="M12 5l-8 8-4-4 1.5-1.5L4 10l6.5-6.5z"/></svg>
              <span class="select-menu-item-text css-truncate-target js-select-menu-filter-text">
                564-storage-controller-clean
              </span>
            </a>
            <a class="select-menu-item js-navigation-item js-navigation-open "
               href="/ckan/ckan/blob/568-fix-trans-extract/ckan/config/routing.py"
               data-name="568-fix-trans-extract"
               data-skip-pjax="true"
               rel="nofollow">
              <svg aria-hidden="true" class="octicon octicon-check select-menu-item-icon" height="16" version="1.1" viewBox="0 0 12 16" width="12"><path fill-rule="evenodd" d="M12 5l-8 8-4-4 1.5-1.5L4 10l6.5-6.5z"/></svg>
              <span class="select-menu-item-text css-truncate-target js-select-menu-filter-text">
                568-fix-trans-extract
              </span>
            </a>
            <a class="select-menu-item js-navigation-item js-navigation-open "
               href="/ckan/ckan/blob/577-bug-navl-test-fail-if-computer-not-english/ckan/config/routing.py"
               data-name="577-bug-navl-test-fail-if-computer-not-english"
               data-skip-pjax="true"
               rel="nofollow">
              <svg aria-hidden="true" class="octicon octicon-check select-menu-item-icon" height="16" version="1.1" viewBox="0 0 12 16" width="12"><path fill-rule="evenodd" d="M12 5l-8 8-4-4 1.5-1.5L4 10l6.5-6.5z"/></svg>
              <span class="select-menu-item-text css-truncate-target js-select-menu-filter-text">
                577-bug-navl-test-fail-if-computer-not-english
              </span>
            </a>
            <a class="select-menu-item js-navigation-item js-navigation-open "
               href="/ckan/ckan/blob/581-validationerror-crashes-stage3/ckan/config/routing.py"
               data-name="581-validationerror-crashes-stage3"
               data-skip-pjax="true"
               rel="nofollow">
              <svg aria-hidden="true" class="octicon octicon-check select-menu-item-icon" height="16" version="1.1" viewBox="0 0 12 16" width="12"><path fill-rule="evenodd" d="M12 5l-8 8-4-4 1.5-1.5L4 10l6.5-6.5z"/></svg>
              <span class="select-menu-item-text css-truncate-target js-select-menu-filter-text">
                581-validationerror-crashes-stage3
              </span>
            </a>
            <a class="select-menu-item js-navigation-item js-navigation-open "
               href="/ckan/ckan/blob/583-improved-search-messages/ckan/config/routing.py"
               data-name="583-improved-search-messages"
               data-skip-pjax="true"
               rel="nofollow">
              <svg aria-hidden="true" class="octicon octicon-check select-menu-item-icon" height="16" version="1.1" viewBox="0 0 12 16" width="12"><path fill-rule="evenodd" d="M12 5l-8 8-4-4 1.5-1.5L4 10l6.5-6.5z"/></svg>
              <span class="select-menu-item-text css-truncate-target js-select-menu-filter-text">
                583-improved-search-messages
              </span>
            </a>
            <a class="select-menu-item js-navigation-item js-navigation-open "
               href="/ckan/ckan/blob/584-rename-featured-groups/ckan/config/routing.py"
               data-name="584-rename-featured-groups"
               data-skip-pjax="true"
               rel="nofollow">
              <svg aria-hidden="true" class="octicon octicon-check select-menu-item-icon" height="16" version="1.1" viewBox="0 0 12 16" width="12"><path fill-rule="evenodd" d="M12 5l-8 8-4-4 1.5-1.5L4 10l6.5-6.5z"/></svg>
              <span class="select-menu-item-text css-truncate-target js-select-menu-filter-text">
                584-rename-featured-groups
              </span>
            </a>
            <a class="select-menu-item js-navigation-item js-navigation-open "
               href="/ckan/ckan/blob/585-quick-org-template-fix/ckan/config/routing.py"
               data-name="585-quick-org-template-fix"
               data-skip-pjax="true"
               rel="nofollow">
              <svg aria-hidden="true" class="octicon octicon-check select-menu-item-icon" height="16" version="1.1" viewBox="0 0 12 16" width="12"><path fill-rule="evenodd" d="M12 5l-8 8-4-4 1.5-1.5L4 10l6.5-6.5z"/></svg>
              <span class="select-menu-item-text css-truncate-target js-select-menu-filter-text">
                585-quick-org-template-fix
              </span>
            </a>
            <a class="select-menu-item js-navigation-item js-navigation-open "
               href="/ckan/ckan/blob/586-dataset-validation-errors/ckan/config/routing.py"
               data-name="586-dataset-validation-errors"
               data-skip-pjax="true"
               rel="nofollow">
              <svg aria-hidden="true" class="octicon octicon-check select-menu-item-icon" height="16" version="1.1" viewBox="0 0 12 16" width="12"><path fill-rule="evenodd" d="M12 5l-8 8-4-4 1.5-1.5L4 10l6.5-6.5z"/></svg>
              <span class="select-menu-item-text css-truncate-target js-select-menu-filter-text">
                586-dataset-validation-errors
              </span>
            </a>
            <a class="select-menu-item js-navigation-item js-navigation-open "
               href="/ckan/ckan/blob/590-edit-admin-button/ckan/config/routing.py"
               data-name="590-edit-admin-button"
               data-skip-pjax="true"
               rel="nofollow">
              <svg aria-hidden="true" class="octicon octicon-check select-menu-item-icon" height="16" version="1.1" viewBox="0 0 12 16" width="12"><path fill-rule="evenodd" d="M12 5l-8 8-4-4 1.5-1.5L4 10l6.5-6.5z"/></svg>
              <span class="select-menu-item-text css-truncate-target js-select-menu-filter-text">
                590-edit-admin-button
              </span>
            </a>
            <a class="select-menu-item js-navigation-item js-navigation-open "
               href="/ckan/ckan/blob/592-org-create-header/ckan/config/routing.py"
               data-name="592-org-create-header"
               data-skip-pjax="true"
               rel="nofollow">
              <svg aria-hidden="true" class="octicon octicon-check select-menu-item-icon" height="16" version="1.1" viewBox="0 0 12 16" width="12"><path fill-rule="evenodd" d="M12 5l-8 8-4-4 1.5-1.5L4 10l6.5-6.5z"/></svg>
              <span class="select-menu-item-text css-truncate-target js-select-menu-filter-text">
                592-org-create-header
              </span>
            </a>
            <a class="select-menu-item js-navigation-item js-navigation-open "
               href="/ckan/ckan/blob/594-case-insensitive-group-org-search/ckan/config/routing.py"
               data-name="594-case-insensitive-group-org-search"
               data-skip-pjax="true"
               rel="nofollow">
              <svg aria-hidden="true" class="octicon octicon-check select-menu-item-icon" height="16" version="1.1" viewBox="0 0 12 16" width="12"><path fill-rule="evenodd" d="M12 5l-8 8-4-4 1.5-1.5L4 10l6.5-6.5z"/></svg>
              <span class="select-menu-item-text css-truncate-target js-select-menu-filter-text">
                594-case-insensitive-group-org-search
              </span>
            </a>
            <a class="select-menu-item js-navigation-item js-navigation-open "
               href="/ckan/ckan/blob/597-fix-logout-first-template/ckan/config/routing.py"
               data-name="597-fix-logout-first-template"
               data-skip-pjax="true"
               rel="nofollow">
              <svg aria-hidden="true" class="octicon octicon-check select-menu-item-icon" height="16" version="1.1" viewBox="0 0 12 16" width="12"><path fill-rule="evenodd" d="M12 5l-8 8-4-4 1.5-1.5L4 10l6.5-6.5z"/></svg>
              <span class="select-menu-item-text css-truncate-target js-select-menu-filter-text">
                597-fix-logout-first-template
              </span>
            </a>
            <a class="select-menu-item js-navigation-item js-navigation-open "
               href="/ckan/ckan/blob/605-data-api-template/ckan/config/routing.py"
               data-name="605-data-api-template"
               data-skip-pjax="true"
               rel="nofollow">
              <svg aria-hidden="true" class="octicon octicon-check select-menu-item-icon" height="16" version="1.1" viewBox="0 0 12 16" width="12"><path fill-rule="evenodd" d="M12 5l-8 8-4-4 1.5-1.5L4 10l6.5-6.5z"/></svg>
              <span class="select-menu-item-text css-truncate-target js-select-menu-filter-text">
                605-data-api-template
              </span>
            </a>
            <a class="select-menu-item js-navigation-item js-navigation-open "
               href="/ckan/ckan/blob/606-nice-error-on-no-resource/ckan/config/routing.py"
               data-name="606-nice-error-on-no-resource"
               data-skip-pjax="true"
               rel="nofollow">
              <svg aria-hidden="true" class="octicon octicon-check select-menu-item-icon" height="16" version="1.1" viewBox="0 0 12 16" width="12"><path fill-rule="evenodd" d="M12 5l-8 8-4-4 1.5-1.5L4 10l6.5-6.5z"/></svg>
              <span class="select-menu-item-text css-truncate-target js-select-menu-filter-text">
                606-nice-error-on-no-resource
              </span>
            </a>
            <a class="select-menu-item js-navigation-item js-navigation-open "
               href="/ckan/ckan/blob/621-bug-crash-on-extras-validation/ckan/config/routing.py"
               data-name="621-bug-crash-on-extras-validation"
               data-skip-pjax="true"
               rel="nofollow">
              <svg aria-hidden="true" class="octicon octicon-check select-menu-item-icon" height="16" version="1.1" viewBox="0 0 12 16" width="12"><path fill-rule="evenodd" d="M12 5l-8 8-4-4 1.5-1.5L4 10l6.5-6.5z"/></svg>
              <span class="select-menu-item-text css-truncate-target js-select-menu-filter-text">
                621-bug-crash-on-extras-validation
              </span>
            </a>
            <a class="select-menu-item js-navigation-item js-navigation-open "
               href="/ckan/ckan/blob/621-bug-move-extras_validation_into___before/ckan/config/routing.py"
               data-name="621-bug-move-extras_validation_into___before"
               data-skip-pjax="true"
               rel="nofollow">
              <svg aria-hidden="true" class="octicon octicon-check select-menu-item-icon" height="16" version="1.1" viewBox="0 0 12 16" width="12"><path fill-rule="evenodd" d="M12 5l-8 8-4-4 1.5-1.5L4 10l6.5-6.5z"/></svg>
              <span class="select-menu-item-text css-truncate-target js-select-menu-filter-text">
                621-bug-move-extras_validation_into___before
              </span>
            </a>
            <a class="select-menu-item js-navigation-item js-navigation-open "
               href="/ckan/ckan/blob/626-dashboard-update/ckan/config/routing.py"
               data-name="626-dashboard-update"
               data-skip-pjax="true"
               rel="nofollow">
              <svg aria-hidden="true" class="octicon octicon-check select-menu-item-icon" height="16" version="1.1" viewBox="0 0 12 16" width="12"><path fill-rule="evenodd" d="M12 5l-8 8-4-4 1.5-1.5L4 10l6.5-6.5z"/></svg>
              <span class="select-menu-item-text css-truncate-target js-select-menu-filter-text">
                626-dashboard-update
              </span>
            </a>
            <a class="select-menu-item js-navigation-item js-navigation-open "
               href="/ckan/ckan/blob/629-clear-all-facet/ckan/config/routing.py"
               data-name="629-clear-all-facet"
               data-skip-pjax="true"
               rel="nofollow">
              <svg aria-hidden="true" class="octicon octicon-check select-menu-item-icon" height="16" version="1.1" viewBox="0 0 12 16" width="12"><path fill-rule="evenodd" d="M12 5l-8 8-4-4 1.5-1.5L4 10l6.5-6.5z"/></svg>
              <span class="select-menu-item-text css-truncate-target js-select-menu-filter-text">
                629-clear-all-facet
              </span>
            </a>
            <a class="select-menu-item js-navigation-item js-navigation-open "
               href="/ckan/ckan/blob/630-org-template-tidy-up/ckan/config/routing.py"
               data-name="630-org-template-tidy-up"
               data-skip-pjax="true"
               rel="nofollow">
              <svg aria-hidden="true" class="octicon octicon-check select-menu-item-icon" height="16" version="1.1" viewBox="0 0 12 16" width="12"><path fill-rule="evenodd" d="M12 5l-8 8-4-4 1.5-1.5L4 10l6.5-6.5z"/></svg>
              <span class="select-menu-item-text css-truncate-target js-select-menu-filter-text">
                630-org-template-tidy-up
              </span>
            </a>
            <a class="select-menu-item js-navigation-item js-navigation-open "
               href="/ckan/ckan/blob/637-solr-updates/ckan/config/routing.py"
               data-name="637-solr-updates"
               data-skip-pjax="true"
               rel="nofollow">
              <svg aria-hidden="true" class="octicon octicon-check select-menu-item-icon" height="16" version="1.1" viewBox="0 0 12 16" width="12"><path fill-rule="evenodd" d="M12 5l-8 8-4-4 1.5-1.5L4 10l6.5-6.5z"/></svg>
              <span class="select-menu-item-text css-truncate-target js-select-menu-filter-text">
                637-solr-updates
              </span>
            </a>
            <a class="select-menu-item js-navigation-item js-navigation-open "
               href="/ckan/ckan/blob/646-undocumented-action-functions/ckan/config/routing.py"
               data-name="646-undocumented-action-functions"
               data-skip-pjax="true"
               rel="nofollow">
              <svg aria-hidden="true" class="octicon octicon-check select-menu-item-icon" height="16" version="1.1" viewBox="0 0 12 16" width="12"><path fill-rule="evenodd" d="M12 5l-8 8-4-4 1.5-1.5L4 10l6.5-6.5z"/></svg>
              <span class="select-menu-item-text css-truncate-target js-select-menu-filter-text">
                646-undocumented-action-functions
              </span>
            </a>
            <a class="select-menu-item js-navigation-item js-navigation-open "
               href="/ckan/ckan/blob/652-secure-datastore/ckan/config/routing.py"
               data-name="652-secure-datastore"
               data-skip-pjax="true"
               rel="nofollow">
              <svg aria-hidden="true" class="octicon octicon-check select-menu-item-icon" height="16" version="1.1" viewBox="0 0 12 16" width="12"><path fill-rule="evenodd" d="M12 5l-8 8-4-4 1.5-1.5L4 10l6.5-6.5z"/></svg>
              <span class="select-menu-item-text css-truncate-target js-select-menu-filter-text">
                652-secure-datastore
              </span>
            </a>
            <a class="select-menu-item js-navigation-item js-navigation-open "
               href="/ckan/ckan/blob/654-disable-activity-streams-via-config/ckan/config/routing.py"
               data-name="654-disable-activity-streams-via-config"
               data-skip-pjax="true"
               rel="nofollow">
              <svg aria-hidden="true" class="octicon octicon-check select-menu-item-icon" height="16" version="1.1" viewBox="0 0 12 16" width="12"><path fill-rule="evenodd" d="M12 5l-8 8-4-4 1.5-1.5L4 10l6.5-6.5z"/></svg>
              <span class="select-menu-item-text css-truncate-target js-select-menu-filter-text">
                654-disable-activity-streams-via-config
              </span>
            </a>
            <a class="select-menu-item js-navigation-item js-navigation-open "
               href="/ckan/ckan/blob/658-bulk-action-post/ckan/config/routing.py"
               data-name="658-bulk-action-post"
               data-skip-pjax="true"
               rel="nofollow">
              <svg aria-hidden="true" class="octicon octicon-check select-menu-item-icon" height="16" version="1.1" viewBox="0 0 12 16" width="12"><path fill-rule="evenodd" d="M12 5l-8 8-4-4 1.5-1.5L4 10l6.5-6.5z"/></svg>
              <span class="select-menu-item-text css-truncate-target js-select-menu-filter-text">
                658-bulk-action-post
              </span>
            </a>
            <a class="select-menu-item js-navigation-item js-navigation-open "
               href="/ckan/ckan/blob/664-group-form-issues/ckan/config/routing.py"
               data-name="664-group-form-issues"
               data-skip-pjax="true"
               rel="nofollow">
              <svg aria-hidden="true" class="octicon octicon-check select-menu-item-icon" height="16" version="1.1" viewBox="0 0 12 16" width="12"><path fill-rule="evenodd" d="M12 5l-8 8-4-4 1.5-1.5L4 10l6.5-6.5z"/></svg>
              <span class="select-menu-item-text css-truncate-target js-select-menu-filter-text">
                664-group-form-issues
              </span>
            </a>
            <a class="select-menu-item js-navigation-item js-navigation-open "
               href="/ckan/ckan/blob/669-member-list-broken/ckan/config/routing.py"
               data-name="669-member-list-broken"
               data-skip-pjax="true"
               rel="nofollow">
              <svg aria-hidden="true" class="octicon octicon-check select-menu-item-icon" height="16" version="1.1" viewBox="0 0 12 16" width="12"><path fill-rule="evenodd" d="M12 5l-8 8-4-4 1.5-1.5L4 10l6.5-6.5z"/></svg>
              <span class="select-menu-item-text css-truncate-target js-select-menu-filter-text">
                669-member-list-broken
              </span>
            </a>
            <a class="select-menu-item js-navigation-item js-navigation-open "
               href="/ckan/ckan/blob/671-bug-custom-about-page-text-gets-truncated/ckan/config/routing.py"
               data-name="671-bug-custom-about-page-text-gets-truncated"
               data-skip-pjax="true"
               rel="nofollow">
              <svg aria-hidden="true" class="octicon octicon-check select-menu-item-icon" height="16" version="1.1" viewBox="0 0 12 16" width="12"><path fill-rule="evenodd" d="M12 5l-8 8-4-4 1.5-1.5L4 10l6.5-6.5z"/></svg>
              <span class="select-menu-item-text css-truncate-target js-select-menu-filter-text">
                671-bug-custom-about-page-text-gets-truncated
              </span>
            </a>
            <a class="select-menu-item js-navigation-item js-navigation-open "
               href="/ckan/ckan/blob/674-better-solr-exceptions/ckan/config/routing.py"
               data-name="674-better-solr-exceptions"
               data-skip-pjax="true"
               rel="nofollow">
              <svg aria-hidden="true" class="octicon octicon-check select-menu-item-icon" height="16" version="1.1" viewBox="0 0 12 16" width="12"><path fill-rule="evenodd" d="M12 5l-8 8-4-4 1.5-1.5L4 10l6.5-6.5z"/></svg>
              <span class="select-menu-item-text css-truncate-target js-select-menu-filter-text">
                674-better-solr-exceptions
              </span>
            </a>
            <a class="select-menu-item js-navigation-item js-navigation-open "
               href="/ckan/ckan/blob/678-modal-position/ckan/config/routing.py"
               data-name="678-modal-position"
               data-skip-pjax="true"
               rel="nofollow">
              <svg aria-hidden="true" class="octicon octicon-check select-menu-item-icon" height="16" version="1.1" viewBox="0 0 12 16" width="12"><path fill-rule="evenodd" d="M12 5l-8 8-4-4 1.5-1.5L4 10l6.5-6.5z"/></svg>
              <span class="select-menu-item-text css-truncate-target js-select-menu-filter-text">
                678-modal-position
              </span>
            </a>
            <a class="select-menu-item js-navigation-item js-navigation-open "
               href="/ckan/ckan/blob/680-no-default-package-roles/ckan/config/routing.py"
               data-name="680-no-default-package-roles"
               data-skip-pjax="true"
               rel="nofollow">
              <svg aria-hidden="true" class="octicon octicon-check select-menu-item-icon" height="16" version="1.1" viewBox="0 0 12 16" width="12"><path fill-rule="evenodd" d="M12 5l-8 8-4-4 1.5-1.5L4 10l6.5-6.5z"/></svg>
              <span class="select-menu-item-text css-truncate-target js-select-menu-filter-text">
                680-no-default-package-roles
              </span>
            </a>
            <a class="select-menu-item js-navigation-item js-navigation-open "
               href="/ckan/ckan/blob/683-remove-author-resource/ckan/config/routing.py"
               data-name="683-remove-author-resource"
               data-skip-pjax="true"
               rel="nofollow">
              <svg aria-hidden="true" class="octicon octicon-check select-menu-item-icon" height="16" version="1.1" viewBox="0 0 12 16" width="12"><path fill-rule="evenodd" d="M12 5l-8 8-4-4 1.5-1.5L4 10l6.5-6.5z"/></svg>
              <span class="select-menu-item-text css-truncate-target js-select-menu-filter-text">
                683-remove-author-resource
              </span>
            </a>
            <a class="select-menu-item js-navigation-item js-navigation-open "
               href="/ckan/ckan/blob/688-template-blocks/ckan/config/routing.py"
               data-name="688-template-blocks"
               data-skip-pjax="true"
               rel="nofollow">
              <svg aria-hidden="true" class="octicon octicon-check select-menu-item-icon" height="16" version="1.1" viewBox="0 0 12 16" width="12"><path fill-rule="evenodd" d="M12 5l-8 8-4-4 1.5-1.5L4 10l6.5-6.5z"/></svg>
              <span class="select-menu-item-text css-truncate-target js-select-menu-filter-text">
                688-template-blocks
              </span>
            </a>
            <a class="select-menu-item js-navigation-item js-navigation-open "
               href="/ckan/ckan/blob/700-speed-up-search-index/ckan/config/routing.py"
               data-name="700-speed-up-search-index"
               data-skip-pjax="true"
               rel="nofollow">
              <svg aria-hidden="true" class="octicon octicon-check select-menu-item-icon" height="16" version="1.1" viewBox="0 0 12 16" width="12"><path fill-rule="evenodd" d="M12 5l-8 8-4-4 1.5-1.5L4 10l6.5-6.5z"/></svg>
              <span class="select-menu-item-text css-truncate-target js-select-menu-filter-text">
                700-speed-up-search-index
              </span>
            </a>
            <a class="select-menu-item js-navigation-item js-navigation-open "
               href="/ckan/ckan/blob/703-html-attribs/ckan/config/routing.py"
               data-name="703-html-attribs"
               data-skip-pjax="true"
               rel="nofollow">
              <svg aria-hidden="true" class="octicon octicon-check select-menu-item-icon" height="16" version="1.1" viewBox="0 0 12 16" width="12"><path fill-rule="evenodd" d="M12 5l-8 8-4-4 1.5-1.5L4 10l6.5-6.5z"/></svg>
              <span class="select-menu-item-text css-truncate-target js-select-menu-filter-text">
                703-html-attribs
              </span>
            </a>
            <a class="select-menu-item js-navigation-item js-navigation-open "
               href="/ckan/ckan/blob/705-remove_url_param-multiple-params/ckan/config/routing.py"
               data-name="705-remove_url_param-multiple-params"
               data-skip-pjax="true"
               rel="nofollow">
              <svg aria-hidden="true" class="octicon octicon-check select-menu-item-icon" height="16" version="1.1" viewBox="0 0 12 16" width="12"><path fill-rule="evenodd" d="M12 5l-8 8-4-4 1.5-1.5L4 10l6.5-6.5z"/></svg>
              <span class="select-menu-item-text css-truncate-target js-select-menu-filter-text">
                705-remove_url_param-multiple-params
              </span>
            </a>
            <a class="select-menu-item js-navigation-item js-navigation-open "
               href="/ckan/ckan/blob/706-fix-data-migration/ckan/config/routing.py"
               data-name="706-fix-data-migration"
               data-skip-pjax="true"
               rel="nofollow">
              <svg aria-hidden="true" class="octicon octicon-check select-menu-item-icon" height="16" version="1.1" viewBox="0 0 12 16" width="12"><path fill-rule="evenodd" d="M12 5l-8 8-4-4 1.5-1.5L4 10l6.5-6.5z"/></svg>
              <span class="select-menu-item-text css-truncate-target js-select-menu-filter-text">
                706-fix-data-migration
              </span>
            </a>
            <a class="select-menu-item js-navigation-item js-navigation-open "
               href="/ckan/ckan/blob/708-markdown-fixes/ckan/config/routing.py"
               data-name="708-markdown-fixes"
               data-skip-pjax="true"
               rel="nofollow">
              <svg aria-hidden="true" class="octicon octicon-check select-menu-item-icon" height="16" version="1.1" viewBox="0 0 12 16" width="12"><path fill-rule="evenodd" d="M12 5l-8 8-4-4 1.5-1.5L4 10l6.5-6.5z"/></svg>
              <span class="select-menu-item-text css-truncate-target js-select-menu-filter-text">
                708-markdown-fixes
              </span>
            </a>
            <a class="select-menu-item js-navigation-item js-navigation-open "
               href="/ckan/ckan/blob/716-pass-schema-in-context/ckan/config/routing.py"
               data-name="716-pass-schema-in-context"
               data-skip-pjax="true"
               rel="nofollow">
              <svg aria-hidden="true" class="octicon octicon-check select-menu-item-icon" height="16" version="1.1" viewBox="0 0 12 16" width="12"><path fill-rule="evenodd" d="M12 5l-8 8-4-4 1.5-1.5L4 10l6.5-6.5z"/></svg>
              <span class="select-menu-item-text css-truncate-target js-select-menu-filter-text">
                716-pass-schema-in-context
              </span>
            </a>
            <a class="select-menu-item js-navigation-item js-navigation-open "
               href="/ckan/ckan/blob/718-datastore-depends-on-localisation-for-2.0/ckan/config/routing.py"
               data-name="718-datastore-depends-on-localisation-for-2.0"
               data-skip-pjax="true"
               rel="nofollow">
              <svg aria-hidden="true" class="octicon octicon-check select-menu-item-icon" height="16" version="1.1" viewBox="0 0 12 16" width="12"><path fill-rule="evenodd" d="M12 5l-8 8-4-4 1.5-1.5L4 10l6.5-6.5z"/></svg>
              <span class="select-menu-item-text css-truncate-target js-select-menu-filter-text">
                718-datastore-depends-on-localisation-for-2.0
              </span>
            </a>
            <a class="select-menu-item js-navigation-item js-navigation-open "
               href="/ckan/ckan/blob/732-double-tag-fun-times/ckan/config/routing.py"
               data-name="732-double-tag-fun-times"
               data-skip-pjax="true"
               rel="nofollow">
              <svg aria-hidden="true" class="octicon octicon-check select-menu-item-icon" height="16" version="1.1" viewBox="0 0 12 16" width="12"><path fill-rule="evenodd" d="M12 5l-8 8-4-4 1.5-1.5L4 10l6.5-6.5z"/></svg>
              <span class="select-menu-item-text css-truncate-target js-select-menu-filter-text">
                732-double-tag-fun-times
              </span>
            </a>
            <a class="select-menu-item js-navigation-item js-navigation-open "
               href="/ckan/ckan/blob/738-fix-search-relevency/ckan/config/routing.py"
               data-name="738-fix-search-relevency"
               data-skip-pjax="true"
               rel="nofollow">
              <svg aria-hidden="true" class="octicon octicon-check select-menu-item-icon" height="16" version="1.1" viewBox="0 0 12 16" width="12"><path fill-rule="evenodd" d="M12 5l-8 8-4-4 1.5-1.5L4 10l6.5-6.5z"/></svg>
              <span class="select-menu-item-text css-truncate-target js-select-menu-filter-text">
                738-fix-search-relevency
              </span>
            </a>
            <a class="select-menu-item js-navigation-item js-navigation-open "
               href="/ckan/ckan/blob/740-resource-url/ckan/config/routing.py"
               data-name="740-resource-url"
               data-skip-pjax="true"
               rel="nofollow">
              <svg aria-hidden="true" class="octicon octicon-check select-menu-item-icon" height="16" version="1.1" viewBox="0 0 12 16" width="12"><path fill-rule="evenodd" d="M12 5l-8 8-4-4 1.5-1.5L4 10l6.5-6.5z"/></svg>
              <span class="select-menu-item-text css-truncate-target js-select-menu-filter-text">
                740-resource-url
              </span>
            </a>
            <a class="select-menu-item js-navigation-item js-navigation-open "
               href="/ckan/ckan/blob/744-tests-for-page-view-tracking/ckan/config/routing.py"
               data-name="744-tests-for-page-view-tracking"
               data-skip-pjax="true"
               rel="nofollow">
              <svg aria-hidden="true" class="octicon octicon-check select-menu-item-icon" height="16" version="1.1" viewBox="0 0 12 16" width="12"><path fill-rule="evenodd" d="M12 5l-8 8-4-4 1.5-1.5L4 10l6.5-6.5z"/></svg>
              <span class="select-menu-item-text css-truncate-target js-select-menu-filter-text">
                744-tests-for-page-view-tracking
              </span>
            </a>
            <a class="select-menu-item js-navigation-item js-navigation-open "
               href="/ckan/ckan/blob/749-org-index-title/ckan/config/routing.py"
               data-name="749-org-index-title"
               data-skip-pjax="true"
               rel="nofollow">
              <svg aria-hidden="true" class="octicon octicon-check select-menu-item-icon" height="16" version="1.1" viewBox="0 0 12 16" width="12"><path fill-rule="evenodd" d="M12 5l-8 8-4-4 1.5-1.5L4 10l6.5-6.5z"/></svg>
              <span class="select-menu-item-text css-truncate-target js-select-menu-filter-text">
                749-org-index-title
              </span>
            </a>
            <a class="select-menu-item js-navigation-item js-navigation-open "
               href="/ckan/ckan/blob/751-release-docs/ckan/config/routing.py"
               data-name="751-release-docs"
               data-skip-pjax="true"
               rel="nofollow">
              <svg aria-hidden="true" class="octicon octicon-check select-menu-item-icon" height="16" version="1.1" viewBox="0 0 12 16" width="12"><path fill-rule="evenodd" d="M12 5l-8 8-4-4 1.5-1.5L4 10l6.5-6.5z"/></svg>
              <span class="select-menu-item-text css-truncate-target js-select-menu-filter-text">
                751-release-docs
              </span>
            </a>
            <a class="select-menu-item js-navigation-item js-navigation-open "
               href="/ckan/ckan/blob/752-data-api-button/ckan/config/routing.py"
               data-name="752-data-api-button"
               data-skip-pjax="true"
               rel="nofollow">
              <svg aria-hidden="true" class="octicon octicon-check select-menu-item-icon" height="16" version="1.1" viewBox="0 0 12 16" width="12"><path fill-rule="evenodd" d="M12 5l-8 8-4-4 1.5-1.5L4 10l6.5-6.5z"/></svg>
              <span class="select-menu-item-text css-truncate-target js-select-menu-filter-text">
                752-data-api-button
              </span>
            </a>
            <a class="select-menu-item js-navigation-item js-navigation-open "
               href="/ckan/ckan/blob/769-docs-reorg/ckan/config/routing.py"
               data-name="769-docs-reorg"
               data-skip-pjax="true"
               rel="nofollow">
              <svg aria-hidden="true" class="octicon octicon-check select-menu-item-icon" height="16" version="1.1" viewBox="0 0 12 16" width="12"><path fill-rule="evenodd" d="M12 5l-8 8-4-4 1.5-1.5L4 10l6.5-6.5z"/></svg>
              <span class="select-menu-item-text css-truncate-target js-select-menu-filter-text">
                769-docs-reorg
              </span>
            </a>
            <a class="select-menu-item js-navigation-item js-navigation-open "
               href="/ckan/ckan/blob/772-document-plugin-load-order/ckan/config/routing.py"
               data-name="772-document-plugin-load-order"
               data-skip-pjax="true"
               rel="nofollow">
              <svg aria-hidden="true" class="octicon octicon-check select-menu-item-icon" height="16" version="1.1" viewBox="0 0 12 16" width="12"><path fill-rule="evenodd" d="M12 5l-8 8-4-4 1.5-1.5L4 10l6.5-6.5z"/></svg>
              <span class="select-menu-item-text css-truncate-target js-select-menu-filter-text">
                772-document-plugin-load-order
              </span>
            </a>
            <a class="select-menu-item js-navigation-item js-navigation-open "
               href="/ckan/ckan/blob/776-show-organizaton-facets/ckan/config/routing.py"
               data-name="776-show-organizaton-facets"
               data-skip-pjax="true"
               rel="nofollow">
              <svg aria-hidden="true" class="octicon octicon-check select-menu-item-icon" height="16" version="1.1" viewBox="0 0 12 16" width="12"><path fill-rule="evenodd" d="M12 5l-8 8-4-4 1.5-1.5L4 10l6.5-6.5z"/></svg>
              <span class="select-menu-item-text css-truncate-target js-select-menu-filter-text">
                776-show-organizaton-facets
              </span>
            </a>
            <a class="select-menu-item js-navigation-item js-navigation-open "
               href="/ckan/ckan/blob/787-ie10-media-item-image-height/ckan/config/routing.py"
               data-name="787-ie10-media-item-image-height"
               data-skip-pjax="true"
               rel="nofollow">
              <svg aria-hidden="true" class="octicon octicon-check select-menu-item-icon" height="16" version="1.1" viewBox="0 0 12 16" width="12"><path fill-rule="evenodd" d="M12 5l-8 8-4-4 1.5-1.5L4 10l6.5-6.5z"/></svg>
              <span class="select-menu-item-text css-truncate-target js-select-menu-filter-text">
                787-ie10-media-item-image-height
              </span>
            </a>
            <a class="select-menu-item js-navigation-item js-navigation-open "
               href="/ckan/ckan/blob/788-facet-num-fixes/ckan/config/routing.py"
               data-name="788-facet-num-fixes"
               data-skip-pjax="true"
               rel="nofollow">
              <svg aria-hidden="true" class="octicon octicon-check select-menu-item-icon" height="16" version="1.1" viewBox="0 0 12 16" width="12"><path fill-rule="evenodd" d="M12 5l-8 8-4-4 1.5-1.5L4 10l6.5-6.5z"/></svg>
              <span class="select-menu-item-text css-truncate-target js-select-menu-filter-text">
                788-facet-num-fixes
              </span>
            </a>
            <a class="select-menu-item js-navigation-item js-navigation-open "
               href="/ckan/ckan/blob/790-custom-fields-tutorial/ckan/config/routing.py"
               data-name="790-custom-fields-tutorial"
               data-skip-pjax="true"
               rel="nofollow">
              <svg aria-hidden="true" class="octicon octicon-check select-menu-item-icon" height="16" version="1.1" viewBox="0 0 12 16" width="12"><path fill-rule="evenodd" d="M12 5l-8 8-4-4 1.5-1.5L4 10l6.5-6.5z"/></svg>
              <span class="select-menu-item-text css-truncate-target js-select-menu-filter-text">
                790-custom-fields-tutorial
              </span>
            </a>
            <a class="select-menu-item js-navigation-item js-navigation-open "
               href="/ckan/ckan/blob/797-ie7-footer/ckan/config/routing.py"
               data-name="797-ie7-footer"
               data-skip-pjax="true"
               rel="nofollow">
              <svg aria-hidden="true" class="octicon octicon-check select-menu-item-icon" height="16" version="1.1" viewBox="0 0 12 16" width="12"><path fill-rule="evenodd" d="M12 5l-8 8-4-4 1.5-1.5L4 10l6.5-6.5z"/></svg>
              <span class="select-menu-item-text css-truncate-target js-select-menu-filter-text">
                797-ie7-footer
              </span>
            </a>
            <a class="select-menu-item js-navigation-item js-navigation-open "
               href="/ckan/ckan/blob/801-travis/ckan/config/routing.py"
               data-name="801-travis"
               data-skip-pjax="true"
               rel="nofollow">
              <svg aria-hidden="true" class="octicon octicon-check select-menu-item-icon" height="16" version="1.1" viewBox="0 0 12 16" width="12"><path fill-rule="evenodd" d="M12 5l-8 8-4-4 1.5-1.5L4 10l6.5-6.5z"/></svg>
              <span class="select-menu-item-text css-truncate-target js-select-menu-filter-text">
                801-travis
              </span>
            </a>
            <a class="select-menu-item js-navigation-item js-navigation-open "
               href="/ckan/ckan/blob/803-warn-before-deleting-org/ckan/config/routing.py"
               data-name="803-warn-before-deleting-org"
               data-skip-pjax="true"
               rel="nofollow">
              <svg aria-hidden="true" class="octicon octicon-check select-menu-item-icon" height="16" version="1.1" viewBox="0 0 12 16" width="12"><path fill-rule="evenodd" d="M12 5l-8 8-4-4 1.5-1.5L4 10l6.5-6.5z"/></svg>
              <span class="select-menu-item-text css-truncate-target js-select-menu-filter-text">
                803-warn-before-deleting-org
              </span>
            </a>
            <a class="select-menu-item js-navigation-item js-navigation-open "
               href="/ckan/ckan/blob/807-datastore-docs/ckan/config/routing.py"
               data-name="807-datastore-docs"
               data-skip-pjax="true"
               rel="nofollow">
              <svg aria-hidden="true" class="octicon octicon-check select-menu-item-icon" height="16" version="1.1" viewBox="0 0 12 16" width="12"><path fill-rule="evenodd" d="M12 5l-8 8-4-4 1.5-1.5L4 10l6.5-6.5z"/></svg>
              <span class="select-menu-item-text css-truncate-target js-select-menu-filter-text">
                807-datastore-docs
              </span>
            </a>
            <a class="select-menu-item js-navigation-item js-navigation-open "
               href="/ckan/ckan/blob/808-unicode-url-error/ckan/config/routing.py"
               data-name="808-unicode-url-error"
               data-skip-pjax="true"
               rel="nofollow">
              <svg aria-hidden="true" class="octicon octicon-check select-menu-item-icon" height="16" version="1.1" viewBox="0 0 12 16" width="12"><path fill-rule="evenodd" d="M12 5l-8 8-4-4 1.5-1.5L4 10l6.5-6.5z"/></svg>
              <span class="select-menu-item-text css-truncate-target js-select-menu-filter-text">
                808-unicode-url-error
              </span>
            </a>
            <a class="select-menu-item js-navigation-item js-navigation-open "
               href="/ckan/ckan/blob/811-remove-auth-profile-config-for-2.0/ckan/config/routing.py"
               data-name="811-remove-auth-profile-config-for-2.0"
               data-skip-pjax="true"
               rel="nofollow">
              <svg aria-hidden="true" class="octicon octicon-check select-menu-item-icon" height="16" version="1.1" viewBox="0 0 12 16" width="12"><path fill-rule="evenodd" d="M12 5l-8 8-4-4 1.5-1.5L4 10l6.5-6.5z"/></svg>
              <span class="select-menu-item-text css-truncate-target js-select-menu-filter-text">
                811-remove-auth-profile-config-for-2.0
              </span>
            </a>
            <a class="select-menu-item js-navigation-item js-navigation-open "
               href="/ckan/ckan/blob/813-flags/ckan/config/routing.py"
               data-name="813-flags"
               data-skip-pjax="true"
               rel="nofollow">
              <svg aria-hidden="true" class="octicon octicon-check select-menu-item-icon" height="16" version="1.1" viewBox="0 0 12 16" width="12"><path fill-rule="evenodd" d="M12 5l-8 8-4-4 1.5-1.5L4 10l6.5-6.5z"/></svg>
              <span class="select-menu-item-text css-truncate-target js-select-menu-filter-text">
                813-flags
              </span>
            </a>
            <a class="select-menu-item js-navigation-item js-navigation-open "
               href="/ckan/ckan/blob/814-tweak-solr-docs/ckan/config/routing.py"
               data-name="814-tweak-solr-docs"
               data-skip-pjax="true"
               rel="nofollow">
              <svg aria-hidden="true" class="octicon octicon-check select-menu-item-icon" height="16" version="1.1" viewBox="0 0 12 16" width="12"><path fill-rule="evenodd" d="M12 5l-8 8-4-4 1.5-1.5L4 10l6.5-6.5z"/></svg>
              <span class="select-menu-item-text css-truncate-target js-select-menu-filter-text">
                814-tweak-solr-docs
              </span>
            </a>
            <a class="select-menu-item js-navigation-item js-navigation-open "
               href="/ckan/ckan/blob/824-flags/ckan/config/routing.py"
               data-name="824-flags"
               data-skip-pjax="true"
               rel="nofollow">
              <svg aria-hidden="true" class="octicon octicon-check select-menu-item-icon" height="16" version="1.1" viewBox="0 0 12 16" width="12"><path fill-rule="evenodd" d="M12 5l-8 8-4-4 1.5-1.5L4 10l6.5-6.5z"/></svg>
              <span class="select-menu-item-text css-truncate-target js-select-menu-filter-text">
                824-flags
              </span>
            </a>
            <a class="select-menu-item js-navigation-item js-navigation-open "
               href="/ckan/ckan/blob/827-ga-fix/ckan/config/routing.py"
               data-name="827-ga-fix"
               data-skip-pjax="true"
               rel="nofollow">
              <svg aria-hidden="true" class="octicon octicon-check select-menu-item-icon" height="16" version="1.1" viewBox="0 0 12 16" width="12"><path fill-rule="evenodd" d="M12 5l-8 8-4-4 1.5-1.5L4 10l6.5-6.5z"/></svg>
              <span class="select-menu-item-text css-truncate-target js-select-menu-filter-text">
                827-ga-fix
              </span>
            </a>
            <a class="select-menu-item js-navigation-item js-navigation-open "
               href="/ckan/ckan/blob/830-dashboard-fix/ckan/config/routing.py"
               data-name="830-dashboard-fix"
               data-skip-pjax="true"
               rel="nofollow">
              <svg aria-hidden="true" class="octicon octicon-check select-menu-item-icon" height="16" version="1.1" viewBox="0 0 12 16" width="12"><path fill-rule="evenodd" d="M12 5l-8 8-4-4 1.5-1.5L4 10l6.5-6.5z"/></svg>
              <span class="select-menu-item-text css-truncate-target js-select-menu-filter-text">
                830-dashboard-fix
              </span>
            </a>
            <a class="select-menu-item js-navigation-item js-navigation-open "
               href="/ckan/ckan/blob/838-pgcode-string/ckan/config/routing.py"
               data-name="838-pgcode-string"
               data-skip-pjax="true"
               rel="nofollow">
              <svg aria-hidden="true" class="octicon octicon-check select-menu-item-icon" height="16" version="1.1" viewBox="0 0 12 16" width="12"><path fill-rule="evenodd" d="M12 5l-8 8-4-4 1.5-1.5L4 10l6.5-6.5z"/></svg>
              <span class="select-menu-item-text css-truncate-target js-select-menu-filter-text">
                838-pgcode-string
              </span>
            </a>
            <a class="select-menu-item js-navigation-item js-navigation-open "
               href="/ckan/ckan/blob/839-stats-doc/ckan/config/routing.py"
               data-name="839-stats-doc"
               data-skip-pjax="true"
               rel="nofollow">
              <svg aria-hidden="true" class="octicon octicon-check select-menu-item-icon" height="16" version="1.1" viewBox="0 0 12 16" width="12"><path fill-rule="evenodd" d="M12 5l-8 8-4-4 1.5-1.5L4 10l6.5-6.5z"/></svg>
              <span class="select-menu-item-text css-truncate-target js-select-menu-filter-text">
                839-stats-doc
              </span>
            </a>
            <a class="select-menu-item js-navigation-item js-navigation-open "
               href="/ckan/ckan/blob/846-unicode-api-json/ckan/config/routing.py"
               data-name="846-unicode-api-json"
               data-skip-pjax="true"
               rel="nofollow">
              <svg aria-hidden="true" class="octicon octicon-check select-menu-item-icon" height="16" version="1.1" viewBox="0 0 12 16" width="12"><path fill-rule="evenodd" d="M12 5l-8 8-4-4 1.5-1.5L4 10l6.5-6.5z"/></svg>
              <span class="select-menu-item-text css-truncate-target js-select-menu-filter-text">
                846-unicode-api-json
              </span>
            </a>
            <a class="select-menu-item js-navigation-item js-navigation-open "
               href="/ckan/ckan/blob/848-finishing-configuration-docs/ckan/config/routing.py"
               data-name="848-finishing-configuration-docs"
               data-skip-pjax="true"
               rel="nofollow">
              <svg aria-hidden="true" class="octicon octicon-check select-menu-item-icon" height="16" version="1.1" viewBox="0 0 12 16" width="12"><path fill-rule="evenodd" d="M12 5l-8 8-4-4 1.5-1.5L4 10l6.5-6.5z"/></svg>
              <span class="select-menu-item-text css-truncate-target js-select-menu-filter-text">
                848-finishing-configuration-docs
              </span>
            </a>
            <a class="select-menu-item js-navigation-item js-navigation-open "
               href="/ckan/ckan/blob/853-license-facet/ckan/config/routing.py"
               data-name="853-license-facet"
               data-skip-pjax="true"
               rel="nofollow">
              <svg aria-hidden="true" class="octicon octicon-check select-menu-item-icon" height="16" version="1.1" viewBox="0 0 12 16" width="12"><path fill-rule="evenodd" d="M12 5l-8 8-4-4 1.5-1.5L4 10l6.5-6.5z"/></svg>
              <span class="select-menu-item-text css-truncate-target js-select-menu-filter-text">
                853-license-facet
              </span>
            </a>
            <a class="select-menu-item js-navigation-item js-navigation-open "
               href="/ckan/ckan/blob/859-fix-default-sort-ordering/ckan/config/routing.py"
               data-name="859-fix-default-sort-ordering"
               data-skip-pjax="true"
               rel="nofollow">
              <svg aria-hidden="true" class="octicon octicon-check select-menu-item-icon" height="16" version="1.1" viewBox="0 0 12 16" width="12"><path fill-rule="evenodd" d="M12 5l-8 8-4-4 1.5-1.5L4 10l6.5-6.5z"/></svg>
              <span class="select-menu-item-text css-truncate-target js-select-menu-filter-text">
                859-fix-default-sort-ordering
              </span>
            </a>
            <a class="select-menu-item js-navigation-item js-navigation-open "
               href="/ckan/ckan/blob/865-add-resource-breadcrumbs/ckan/config/routing.py"
               data-name="865-add-resource-breadcrumbs"
               data-skip-pjax="true"
               rel="nofollow">
              <svg aria-hidden="true" class="octicon octicon-check select-menu-item-icon" height="16" version="1.1" viewBox="0 0 12 16" width="12"><path fill-rule="evenodd" d="M12 5l-8 8-4-4 1.5-1.5L4 10l6.5-6.5z"/></svg>
              <span class="select-menu-item-text css-truncate-target js-select-menu-filter-text">
                865-add-resource-breadcrumbs
              </span>
            </a>
            <a class="select-menu-item js-navigation-item js-navigation-open "
               href="/ckan/ckan/blob/867-heading-sizes/ckan/config/routing.py"
               data-name="867-heading-sizes"
               data-skip-pjax="true"
               rel="nofollow">
              <svg aria-hidden="true" class="octicon octicon-check select-menu-item-icon" height="16" version="1.1" viewBox="0 0 12 16" width="12"><path fill-rule="evenodd" d="M12 5l-8 8-4-4 1.5-1.5L4 10l6.5-6.5z"/></svg>
              <span class="select-menu-item-text css-truncate-target js-select-menu-filter-text">
                867-heading-sizes
              </span>
            </a>
            <a class="select-menu-item js-navigation-item js-navigation-open "
               href="/ckan/ckan/blob/869-validate-username-in-new-member/ckan/config/routing.py"
               data-name="869-validate-username-in-new-member"
               data-skip-pjax="true"
               rel="nofollow">
              <svg aria-hidden="true" class="octicon octicon-check select-menu-item-icon" height="16" version="1.1" viewBox="0 0 12 16" width="12"><path fill-rule="evenodd" d="M12 5l-8 8-4-4 1.5-1.5L4 10l6.5-6.5z"/></svg>
              <span class="select-menu-item-text css-truncate-target js-select-menu-filter-text">
                869-validate-username-in-new-member
              </span>
            </a>
            <a class="select-menu-item js-navigation-item js-navigation-open "
               href="/ckan/ckan/blob/879-config-cleanup/ckan/config/routing.py"
               data-name="879-config-cleanup"
               data-skip-pjax="true"
               rel="nofollow">
              <svg aria-hidden="true" class="octicon octicon-check select-menu-item-icon" height="16" version="1.1" viewBox="0 0 12 16" width="12"><path fill-rule="evenodd" d="M12 5l-8 8-4-4 1.5-1.5L4 10l6.5-6.5z"/></svg>
              <span class="select-menu-item-text css-truncate-target js-select-menu-filter-text">
                879-config-cleanup
              </span>
            </a>
            <a class="select-menu-item js-navigation-item js-navigation-open "
               href="/ckan/ckan/blob/881-form-ie7/ckan/config/routing.py"
               data-name="881-form-ie7"
               data-skip-pjax="true"
               rel="nofollow">
              <svg aria-hidden="true" class="octicon octicon-check select-menu-item-icon" height="16" version="1.1" viewBox="0 0 12 16" width="12"><path fill-rule="evenodd" d="M12 5l-8 8-4-4 1.5-1.5L4 10l6.5-6.5z"/></svg>
              <span class="select-menu-item-text css-truncate-target js-select-menu-filter-text">
                881-form-ie7
              </span>
            </a>
            <a class="select-menu-item js-navigation-item js-navigation-open "
               href="/ckan/ckan/blob/888-cache_dir-path-deployment.ini_tmpl/ckan/config/routing.py"
               data-name="888-cache_dir-path-deployment.ini_tmpl"
               data-skip-pjax="true"
               rel="nofollow">
              <svg aria-hidden="true" class="octicon octicon-check select-menu-item-icon" height="16" version="1.1" viewBox="0 0 12 16" width="12"><path fill-rule="evenodd" d="M12 5l-8 8-4-4 1.5-1.5L4 10l6.5-6.5z"/></svg>
              <span class="select-menu-item-text css-truncate-target js-select-menu-filter-text">
                888-cache_dir-path-deployment.ini_tmpl
              </span>
            </a>
            <a class="select-menu-item js-navigation-item js-navigation-open "
               href="/ckan/ckan/blob/893-datastore-postgres-checks-fail-if-different-dbs/ckan/config/routing.py"
               data-name="893-datastore-postgres-checks-fail-if-different-dbs"
               data-skip-pjax="true"
               rel="nofollow">
              <svg aria-hidden="true" class="octicon octicon-check select-menu-item-icon" height="16" version="1.1" viewBox="0 0 12 16" width="12"><path fill-rule="evenodd" d="M12 5l-8 8-4-4 1.5-1.5L4 10l6.5-6.5z"/></svg>
              <span class="select-menu-item-text css-truncate-target js-select-menu-filter-text">
                893-datastore-postgres-checks-fail-if-different-dbs
              </span>
            </a>
            <a class="select-menu-item js-navigation-item js-navigation-open "
               href="/ckan/ckan/blob/896-resource-proxy-fixes-for-2.0/ckan/config/routing.py"
               data-name="896-resource-proxy-fixes-for-2.0"
               data-skip-pjax="true"
               rel="nofollow">
              <svg aria-hidden="true" class="octicon octicon-check select-menu-item-icon" height="16" version="1.1" viewBox="0 0 12 16" width="12"><path fill-rule="evenodd" d="M12 5l-8 8-4-4 1.5-1.5L4 10l6.5-6.5z"/></svg>
              <span class="select-menu-item-text css-truncate-target js-select-menu-filter-text">
                896-resource-proxy-fixes-for-2.0
              </span>
            </a>
            <a class="select-menu-item js-navigation-item js-navigation-open "
               href="/ckan/ckan/blob/901-bug-save-and-add-another/ckan/config/routing.py"
               data-name="901-bug-save-and-add-another"
               data-skip-pjax="true"
               rel="nofollow">
              <svg aria-hidden="true" class="octicon octicon-check select-menu-item-icon" height="16" version="1.1" viewBox="0 0 12 16" width="12"><path fill-rule="evenodd" d="M12 5l-8 8-4-4 1.5-1.5L4 10l6.5-6.5z"/></svg>
              <span class="select-menu-item-text css-truncate-target js-select-menu-filter-text">
                901-bug-save-and-add-another
              </span>
            </a>
            <a class="select-menu-item js-navigation-item js-navigation-open "
               href="/ckan/ckan/blob/902-uploader-stop-navigate/ckan/config/routing.py"
               data-name="902-uploader-stop-navigate"
               data-skip-pjax="true"
               rel="nofollow">
              <svg aria-hidden="true" class="octicon octicon-check select-menu-item-icon" height="16" version="1.1" viewBox="0 0 12 16" width="12"><path fill-rule="evenodd" d="M12 5l-8 8-4-4 1.5-1.5L4 10l6.5-6.5z"/></svg>
              <span class="select-menu-item-text css-truncate-target js-select-menu-filter-text">
                902-uploader-stop-navigate
              </span>
            </a>
            <a class="select-menu-item js-navigation-item js-navigation-open "
               href="/ckan/ckan/blob/907-for-2.0/ckan/config/routing.py"
               data-name="907-for-2.0"
               data-skip-pjax="true"
               rel="nofollow">
              <svg aria-hidden="true" class="octicon octicon-check select-menu-item-icon" height="16" version="1.1" viewBox="0 0 12 16" width="12"><path fill-rule="evenodd" d="M12 5l-8 8-4-4 1.5-1.5L4 10l6.5-6.5z"/></svg>
              <span class="select-menu-item-text css-truncate-target js-select-menu-filter-text">
                907-for-2.0
              </span>
            </a>
            <a class="select-menu-item js-navigation-item js-navigation-open "
               href="/ckan/ckan/blob/912-org-title-dataset-form/ckan/config/routing.py"
               data-name="912-org-title-dataset-form"
               data-skip-pjax="true"
               rel="nofollow">
              <svg aria-hidden="true" class="octicon octicon-check select-menu-item-icon" height="16" version="1.1" viewBox="0 0 12 16" width="12"><path fill-rule="evenodd" d="M12 5l-8 8-4-4 1.5-1.5L4 10l6.5-6.5z"/></svg>
              <span class="select-menu-item-text css-truncate-target js-select-menu-filter-text">
                912-org-title-dataset-form
              </span>
            </a>
            <a class="select-menu-item js-navigation-item js-navigation-open "
               href="/ckan/ckan/blob/914-pill-spacing/ckan/config/routing.py"
               data-name="914-pill-spacing"
               data-skip-pjax="true"
               rel="nofollow">
              <svg aria-hidden="true" class="octicon octicon-check select-menu-item-icon" height="16" version="1.1" viewBox="0 0 12 16" width="12"><path fill-rule="evenodd" d="M12 5l-8 8-4-4 1.5-1.5L4 10l6.5-6.5z"/></svg>
              <span class="select-menu-item-text css-truncate-target js-select-menu-filter-text">
                914-pill-spacing
              </span>
            </a>
            <a class="select-menu-item js-navigation-item js-navigation-open "
               href="/ckan/ckan/blob/915-explore-button/ckan/config/routing.py"
               data-name="915-explore-button"
               data-skip-pjax="true"
               rel="nofollow">
              <svg aria-hidden="true" class="octicon octicon-check select-menu-item-icon" height="16" version="1.1" viewBox="0 0 12 16" width="12"><path fill-rule="evenodd" d="M12 5l-8 8-4-4 1.5-1.5L4 10l6.5-6.5z"/></svg>
              <span class="select-menu-item-text css-truncate-target js-select-menu-filter-text">
                915-explore-button
              </span>
            </a>
            <a class="select-menu-item js-navigation-item js-navigation-open "
               href="/ckan/ckan/blob/917-datastore_search-filters-get/ckan/config/routing.py"
               data-name="917-datastore_search-filters-get"
               data-skip-pjax="true"
               rel="nofollow">
              <svg aria-hidden="true" class="octicon octicon-check select-menu-item-icon" height="16" version="1.1" viewBox="0 0 12 16" width="12"><path fill-rule="evenodd" d="M12 5l-8 8-4-4 1.5-1.5L4 10l6.5-6.5z"/></svg>
              <span class="select-menu-item-text css-truncate-target js-select-menu-filter-text">
                917-datastore_search-filters-get
              </span>
            </a>
            <a class="select-menu-item js-navigation-item js-navigation-open "
               href="/ckan/ckan/blob/921-resourceproxy-docs/ckan/config/routing.py"
               data-name="921-resourceproxy-docs"
               data-skip-pjax="true"
               rel="nofollow">
              <svg aria-hidden="true" class="octicon octicon-check select-menu-item-icon" height="16" version="1.1" viewBox="0 0 12 16" width="12"><path fill-rule="evenodd" d="M12 5l-8 8-4-4 1.5-1.5L4 10l6.5-6.5z"/></svg>
              <span class="select-menu-item-text css-truncate-target js-select-menu-filter-text">
                921-resourceproxy-docs
              </span>
            </a>
            <a class="select-menu-item js-navigation-item js-navigation-open "
               href="/ckan/ckan/blob/924-better-validation-errors/ckan/config/routing.py"
               data-name="924-better-validation-errors"
               data-skip-pjax="true"
               rel="nofollow">
              <svg aria-hidden="true" class="octicon octicon-check select-menu-item-icon" height="16" version="1.1" viewBox="0 0 12 16" width="12"><path fill-rule="evenodd" d="M12 5l-8 8-4-4 1.5-1.5L4 10l6.5-6.5z"/></svg>
              <span class="select-menu-item-text css-truncate-target js-select-menu-filter-text">
                924-better-validation-errors
              </span>
            </a>
            <a class="select-menu-item js-navigation-item js-navigation-open "
               href="/ckan/ckan/blob/929/ckan/config/routing.py"
               data-name="929"
               data-skip-pjax="true"
               rel="nofollow">
              <svg aria-hidden="true" class="octicon octicon-check select-menu-item-icon" height="16" version="1.1" viewBox="0 0 12 16" width="12"><path fill-rule="evenodd" d="M12 5l-8 8-4-4 1.5-1.5L4 10l6.5-6.5z"/></svg>
              <span class="select-menu-item-text css-truncate-target js-select-menu-filter-text">
                929
              </span>
            </a>
            <a class="select-menu-item js-navigation-item js-navigation-open "
               href="/ckan/ckan/blob/938-datapusher/ckan/config/routing.py"
               data-name="938-datapusher"
               data-skip-pjax="true"
               rel="nofollow">
              <svg aria-hidden="true" class="octicon octicon-check select-menu-item-icon" height="16" version="1.1" viewBox="0 0 12 16" width="12"><path fill-rule="evenodd" d="M12 5l-8 8-4-4 1.5-1.5L4 10l6.5-6.5z"/></svg>
              <span class="select-menu-item-text css-truncate-target js-select-menu-filter-text">
                938-datapusher
              </span>
            </a>
            <a class="select-menu-item js-navigation-item js-navigation-open "
               href="/ckan/ckan/blob/942-documentation-guidelines-resubmit/ckan/config/routing.py"
               data-name="942-documentation-guidelines-resubmit"
               data-skip-pjax="true"
               rel="nofollow">
              <svg aria-hidden="true" class="octicon octicon-check select-menu-item-icon" height="16" version="1.1" viewBox="0 0 12 16" width="12"><path fill-rule="evenodd" d="M12 5l-8 8-4-4 1.5-1.5L4 10l6.5-6.5z"/></svg>
              <span class="select-menu-item-text css-truncate-target js-select-menu-filter-text">
                942-documentation-guidelines-resubmit
              </span>
            </a>
            <a class="select-menu-item js-navigation-item js-navigation-open "
               href="/ckan/ckan/blob/942-documentation-guidelines/ckan/config/routing.py"
               data-name="942-documentation-guidelines"
               data-skip-pjax="true"
               rel="nofollow">
              <svg aria-hidden="true" class="octicon octicon-check select-menu-item-icon" height="16" version="1.1" viewBox="0 0 12 16" width="12"><path fill-rule="evenodd" d="M12 5l-8 8-4-4 1.5-1.5L4 10l6.5-6.5z"/></svg>
              <span class="select-menu-item-text css-truncate-target js-select-menu-filter-text">
                942-documentation-guidelines
              </span>
            </a>
            <a class="select-menu-item js-navigation-item js-navigation-open "
               href="/ckan/ckan/blob/945-merge-upgrading-docs/ckan/config/routing.py"
               data-name="945-merge-upgrading-docs"
               data-skip-pjax="true"
               rel="nofollow">
              <svg aria-hidden="true" class="octicon octicon-check select-menu-item-icon" height="16" version="1.1" viewBox="0 0 12 16" width="12"><path fill-rule="evenodd" d="M12 5l-8 8-4-4 1.5-1.5L4 10l6.5-6.5z"/></svg>
              <span class="select-menu-item-text css-truncate-target js-select-menu-filter-text">
                945-merge-upgrading-docs
              </span>
            </a>
            <a class="select-menu-item js-navigation-item js-navigation-open "
               href="/ckan/ckan/blob/948-helper-function-img/ckan/config/routing.py"
               data-name="948-helper-function-img"
               data-skip-pjax="true"
               rel="nofollow">
              <svg aria-hidden="true" class="octicon octicon-check select-menu-item-icon" height="16" version="1.1" viewBox="0 0 12 16" width="12"><path fill-rule="evenodd" d="M12 5l-8 8-4-4 1.5-1.5L4 10l6.5-6.5z"/></svg>
              <span class="select-menu-item-text css-truncate-target js-select-menu-filter-text">
                948-helper-function-img
              </span>
            </a>
            <a class="select-menu-item js-navigation-item js-navigation-open "
               href="/ckan/ckan/blob/952-create-site-user-at-startup/ckan/config/routing.py"
               data-name="952-create-site-user-at-startup"
               data-skip-pjax="true"
               rel="nofollow">
              <svg aria-hidden="true" class="octicon octicon-check select-menu-item-icon" height="16" version="1.1" viewBox="0 0 12 16" width="12"><path fill-rule="evenodd" d="M12 5l-8 8-4-4 1.5-1.5L4 10l6.5-6.5z"/></svg>
              <span class="select-menu-item-text css-truncate-target js-select-menu-filter-text">
                952-create-site-user-at-startup
              </span>
            </a>
            <a class="select-menu-item js-navigation-item js-navigation-open "
               href="/ckan/ckan/blob/953-bug-creating-a-private-dataset-emits-an-activity/ckan/config/routing.py"
               data-name="953-bug-creating-a-private-dataset-emits-an-activity"
               data-skip-pjax="true"
               rel="nofollow">
              <svg aria-hidden="true" class="octicon octicon-check select-menu-item-icon" height="16" version="1.1" viewBox="0 0 12 16" width="12"><path fill-rule="evenodd" d="M12 5l-8 8-4-4 1.5-1.5L4 10l6.5-6.5z"/></svg>
              <span class="select-menu-item-text css-truncate-target js-select-menu-filter-text">
                953-bug-creating-a-private-dataset-emits-an-activity
              </span>
            </a>
            <a class="select-menu-item js-navigation-item js-navigation-open "
               href="/ckan/ckan/blob/956-solr-trigrams/ckan/config/routing.py"
               data-name="956-solr-trigrams"
               data-skip-pjax="true"
               rel="nofollow">
              <svg aria-hidden="true" class="octicon octicon-check select-menu-item-icon" height="16" version="1.1" viewBox="0 0 12 16" width="12"><path fill-rule="evenodd" d="M12 5l-8 8-4-4 1.5-1.5L4 10l6.5-6.5z"/></svg>
              <span class="select-menu-item-text css-truncate-target js-select-menu-filter-text">
                956-solr-trigrams
              </span>
            </a>
            <a class="select-menu-item js-navigation-item js-navigation-open "
               href="/ckan/ckan/blob/964-500-Server-Error-on-non-string-extra-value/ckan/config/routing.py"
               data-name="964-500-Server-Error-on-non-string-extra-value"
               data-skip-pjax="true"
               rel="nofollow">
              <svg aria-hidden="true" class="octicon octicon-check select-menu-item-icon" height="16" version="1.1" viewBox="0 0 12 16" width="12"><path fill-rule="evenodd" d="M12 5l-8 8-4-4 1.5-1.5L4 10l6.5-6.5z"/></svg>
              <span class="select-menu-item-text css-truncate-target js-select-menu-filter-text">
                964-500-Server-Error-on-non-string-extra-value
              </span>
            </a>
            <a class="select-menu-item js-navigation-item js-navigation-open "
               href="/ckan/ckan/blob/973-datastore-docs-improvements/ckan/config/routing.py"
               data-name="973-datastore-docs-improvements"
               data-skip-pjax="true"
               rel="nofollow">
              <svg aria-hidden="true" class="octicon octicon-check select-menu-item-icon" height="16" version="1.1" viewBox="0 0 12 16" width="12"><path fill-rule="evenodd" d="M12 5l-8 8-4-4 1.5-1.5L4 10l6.5-6.5z"/></svg>
              <span class="select-menu-item-text css-truncate-target js-select-menu-filter-text">
                973-datastore-docs-improvements
              </span>
            </a>
            <a class="select-menu-item js-navigation-item js-navigation-open "
               href="/ckan/ckan/blob/974-disable-email-notifications/ckan/config/routing.py"
               data-name="974-disable-email-notifications"
               data-skip-pjax="true"
               rel="nofollow">
              <svg aria-hidden="true" class="octicon octicon-check select-menu-item-icon" height="16" version="1.1" viewBox="0 0 12 16" width="12"><path fill-rule="evenodd" d="M12 5l-8 8-4-4 1.5-1.5L4 10l6.5-6.5z"/></svg>
              <span class="select-menu-item-text css-truncate-target js-select-menu-filter-text">
                974-disable-email-notifications
              </span>
            </a>
            <a class="select-menu-item js-navigation-item js-navigation-open "
               href="/ckan/ckan/blob/1002-enable-resource-proxy/ckan/config/routing.py"
               data-name="1002-enable-resource-proxy"
               data-skip-pjax="true"
               rel="nofollow">
              <svg aria-hidden="true" class="octicon octicon-check select-menu-item-icon" height="16" version="1.1" viewBox="0 0 12 16" width="12"><path fill-rule="evenodd" d="M12 5l-8 8-4-4 1.5-1.5L4 10l6.5-6.5z"/></svg>
              <span class="select-menu-item-text css-truncate-target js-select-menu-filter-text">
                1002-enable-resource-proxy
              </span>
            </a>
            <a class="select-menu-item js-navigation-item js-navigation-open "
               href="/ckan/ckan/blob/1004-featured-groups-updates/ckan/config/routing.py"
               data-name="1004-featured-groups-updates"
               data-skip-pjax="true"
               rel="nofollow">
              <svg aria-hidden="true" class="octicon octicon-check select-menu-item-icon" height="16" version="1.1" viewBox="0 0 12 16" width="12"><path fill-rule="evenodd" d="M12 5l-8 8-4-4 1.5-1.5L4 10l6.5-6.5z"/></svg>
              <span class="select-menu-item-text css-truncate-target js-select-menu-filter-text">
                1004-featured-groups-updates
              </span>
            </a>
            <a class="select-menu-item js-navigation-item js-navigation-open "
               href="/ckan/ckan/blob/1009-ValueError-when-resource-size-is-not-an-int/ckan/config/routing.py"
               data-name="1009-ValueError-when-resource-size-is-not-an-int"
               data-skip-pjax="true"
               rel="nofollow">
              <svg aria-hidden="true" class="octicon octicon-check select-menu-item-icon" height="16" version="1.1" viewBox="0 0 12 16" width="12"><path fill-rule="evenodd" d="M12 5l-8 8-4-4 1.5-1.5L4 10l6.5-6.5z"/></svg>
              <span class="select-menu-item-text css-truncate-target js-select-menu-filter-text">
                1009-ValueError-when-resource-size-is-not-an-int
              </span>
            </a>
            <a class="select-menu-item js-navigation-item js-navigation-open "
               href="/ckan/ckan/blob/1010-server-error-on-new-resource-if-package-does-not-exist/ckan/config/routing.py"
               data-name="1010-server-error-on-new-resource-if-package-does-not-exist"
               data-skip-pjax="true"
               rel="nofollow">
              <svg aria-hidden="true" class="octicon octicon-check select-menu-item-icon" height="16" version="1.1" viewBox="0 0 12 16" width="12"><path fill-rule="evenodd" d="M12 5l-8 8-4-4 1.5-1.5L4 10l6.5-6.5z"/></svg>
              <span class="select-menu-item-text css-truncate-target js-select-menu-filter-text">
                1010-server-error-on-new-resource-if-package-does-not-exist
              </span>
            </a>
            <a class="select-menu-item js-navigation-item js-navigation-open "
               href="/ckan/ckan/blob/1011-template-not-found/ckan/config/routing.py"
               data-name="1011-template-not-found"
               data-skip-pjax="true"
               rel="nofollow">
              <svg aria-hidden="true" class="octicon octicon-check select-menu-item-icon" height="16" version="1.1" viewBox="0 0 12 16" width="12"><path fill-rule="evenodd" d="M12 5l-8 8-4-4 1.5-1.5L4 10l6.5-6.5z"/></svg>
              <span class="select-menu-item-text css-truncate-target js-select-menu-filter-text">
                1011-template-not-found
              </span>
            </a>
            <a class="select-menu-item js-navigation-item js-navigation-open "
               href="/ckan/ckan/blob/1014-sphinx-theme-git-url/ckan/config/routing.py"
               data-name="1014-sphinx-theme-git-url"
               data-skip-pjax="true"
               rel="nofollow">
              <svg aria-hidden="true" class="octicon octicon-check select-menu-item-icon" height="16" version="1.1" viewBox="0 0 12 16" width="12"><path fill-rule="evenodd" d="M12 5l-8 8-4-4 1.5-1.5L4 10l6.5-6.5z"/></svg>
              <span class="select-menu-item-text css-truncate-target js-select-menu-filter-text">
                1014-sphinx-theme-git-url
              </span>
            </a>
            <a class="select-menu-item js-navigation-item js-navigation-open "
               href="/ckan/ckan/blob/1019-task-status-update-docstring/ckan/config/routing.py"
               data-name="1019-task-status-update-docstring"
               data-skip-pjax="true"
               rel="nofollow">
              <svg aria-hidden="true" class="octicon octicon-check select-menu-item-icon" height="16" version="1.1" viewBox="0 0 12 16" width="12"><path fill-rule="evenodd" d="M12 5l-8 8-4-4 1.5-1.5L4 10l6.5-6.5z"/></svg>
              <span class="select-menu-item-text css-truncate-target js-select-menu-filter-text">
                1019-task-status-update-docstring
              </span>
            </a>
            <a class="select-menu-item js-navigation-item js-navigation-open "
               href="/ckan/ckan/blob/1022-api-docs-improvements/ckan/config/routing.py"
               data-name="1022-api-docs-improvements"
               data-skip-pjax="true"
               rel="nofollow">
              <svg aria-hidden="true" class="octicon octicon-check select-menu-item-icon" height="16" version="1.1" viewBox="0 0 12 16" width="12"><path fill-rule="evenodd" d="M12 5l-8 8-4-4 1.5-1.5L4 10l6.5-6.5z"/></svg>
              <span class="select-menu-item-text css-truncate-target js-select-menu-filter-text">
                1022-api-docs-improvements
              </span>
            </a>
            <a class="select-menu-item js-navigation-item js-navigation-open "
               href="/ckan/ckan/blob/1027-celery-configuration/ckan/config/routing.py"
               data-name="1027-celery-configuration"
               data-skip-pjax="true"
               rel="nofollow">
              <svg aria-hidden="true" class="octicon octicon-check select-menu-item-icon" height="16" version="1.1" viewBox="0 0 12 16" width="12"><path fill-rule="evenodd" d="M12 5l-8 8-4-4 1.5-1.5L4 10l6.5-6.5z"/></svg>
              <span class="select-menu-item-text css-truncate-target js-select-menu-filter-text">
                1027-celery-configuration
              </span>
            </a>
            <a class="select-menu-item js-navigation-item js-navigation-open "
               href="/ckan/ckan/blob/1030-ui-update/ckan/config/routing.py"
               data-name="1030-ui-update"
               data-skip-pjax="true"
               rel="nofollow">
              <svg aria-hidden="true" class="octicon octicon-check select-menu-item-icon" height="16" version="1.1" viewBox="0 0 12 16" width="12"><path fill-rule="evenodd" d="M12 5l-8 8-4-4 1.5-1.5L4 10l6.5-6.5z"/></svg>
              <span class="select-menu-item-text css-truncate-target js-select-menu-filter-text">
                1030-ui-update
              </span>
            </a>
            <a class="select-menu-item js-navigation-item js-navigation-open "
               href="/ckan/ckan/blob/1033-term-translation-validation/ckan/config/routing.py"
               data-name="1033-term-translation-validation"
               data-skip-pjax="true"
               rel="nofollow">
              <svg aria-hidden="true" class="octicon octicon-check select-menu-item-icon" height="16" version="1.1" viewBox="0 0 12 16" width="12"><path fill-rule="evenodd" d="M12 5l-8 8-4-4 1.5-1.5L4 10l6.5-6.5z"/></svg>
              <span class="select-menu-item-text css-truncate-target js-select-menu-filter-text">
                1033-term-translation-validation
              </span>
            </a>
            <a class="select-menu-item js-navigation-item js-navigation-open "
               href="/ckan/ckan/blob/1038-organization-hierarchy/ckan/config/routing.py"
               data-name="1038-organization-hierarchy"
               data-skip-pjax="true"
               rel="nofollow">
              <svg aria-hidden="true" class="octicon octicon-check select-menu-item-icon" height="16" version="1.1" viewBox="0 0 12 16" width="12"><path fill-rule="evenodd" d="M12 5l-8 8-4-4 1.5-1.5L4 10l6.5-6.5z"/></svg>
              <span class="select-menu-item-text css-truncate-target js-select-menu-filter-text">
                1038-organization-hierarchy
              </span>
            </a>
            <a class="select-menu-item js-navigation-item js-navigation-open "
               href="/ckan/ckan/blob/1045-deprecate-groups-available-and-organizations-available/ckan/config/routing.py"
               data-name="1045-deprecate-groups-available-and-organizations-available"
               data-skip-pjax="true"
               rel="nofollow">
              <svg aria-hidden="true" class="octicon octicon-check select-menu-item-icon" height="16" version="1.1" viewBox="0 0 12 16" width="12"><path fill-rule="evenodd" d="M12 5l-8 8-4-4 1.5-1.5L4 10l6.5-6.5z"/></svg>
              <span class="select-menu-item-text css-truncate-target js-select-menu-filter-text">
                1045-deprecate-groups-available-and-organizations-available
              </span>
            </a>
            <a class="select-menu-item js-navigation-item js-navigation-open "
               href="/ckan/ckan/blob/1049-group-templates/ckan/config/routing.py"
               data-name="1049-group-templates"
               data-skip-pjax="true"
               rel="nofollow">
              <svg aria-hidden="true" class="octicon octicon-check select-menu-item-icon" height="16" version="1.1" viewBox="0 0 12 16" width="12"><path fill-rule="evenodd" d="M12 5l-8 8-4-4 1.5-1.5L4 10l6.5-6.5z"/></svg>
              <span class="select-menu-item-text css-truncate-target js-select-menu-filter-text">
                1049-group-templates
              </span>
            </a>
            <a class="select-menu-item js-navigation-item js-navigation-open "
               href="/ckan/ckan/blob/1056-group-template-fixes/ckan/config/routing.py"
               data-name="1056-group-template-fixes"
               data-skip-pjax="true"
               rel="nofollow">
              <svg aria-hidden="true" class="octicon octicon-check select-menu-item-icon" height="16" version="1.1" viewBox="0 0 12 16" width="12"><path fill-rule="evenodd" d="M12 5l-8 8-4-4 1.5-1.5L4 10l6.5-6.5z"/></svg>
              <span class="select-menu-item-text css-truncate-target js-select-menu-filter-text">
                1056-group-template-fixes
              </span>
            </a>
            <a class="select-menu-item js-navigation-item js-navigation-open "
               href="/ckan/ckan/blob/1060-action-auth-audit/ckan/config/routing.py"
               data-name="1060-action-auth-audit"
               data-skip-pjax="true"
               rel="nofollow">
              <svg aria-hidden="true" class="octicon octicon-check select-menu-item-icon" height="16" version="1.1" viewBox="0 0 12 16" width="12"><path fill-rule="evenodd" d="M12 5l-8 8-4-4 1.5-1.5L4 10l6.5-6.5z"/></svg>
              <span class="select-menu-item-text css-truncate-target js-select-menu-filter-text">
                1060-action-auth-audit
              </span>
            </a>
            <a class="select-menu-item js-navigation-item js-navigation-open "
               href="/ckan/ckan/blob/1063-org-template-tweak/ckan/config/routing.py"
               data-name="1063-org-template-tweak"
               data-skip-pjax="true"
               rel="nofollow">
              <svg aria-hidden="true" class="octicon octicon-check select-menu-item-icon" height="16" version="1.1" viewBox="0 0 12 16" width="12"><path fill-rule="evenodd" d="M12 5l-8 8-4-4 1.5-1.5L4 10l6.5-6.5z"/></svg>
              <span class="select-menu-item-text css-truncate-target js-select-menu-filter-text">
                1063-org-template-tweak
              </span>
            </a>
            <a class="select-menu-item js-navigation-item js-navigation-open "
               href="/ckan/ckan/blob/1064-dont-translate-empty-string/ckan/config/routing.py"
               data-name="1064-dont-translate-empty-string"
               data-skip-pjax="true"
               rel="nofollow">
              <svg aria-hidden="true" class="octicon octicon-check select-menu-item-icon" height="16" version="1.1" viewBox="0 0 12 16" width="12"><path fill-rule="evenodd" d="M12 5l-8 8-4-4 1.5-1.5L4 10l6.5-6.5z"/></svg>
              <span class="select-menu-item-text css-truncate-target js-select-menu-filter-text">
                1064-dont-translate-empty-string
              </span>
            </a>
            <a class="select-menu-item js-navigation-item js-navigation-open "
               href="/ckan/ckan/blob/1067-datastore-percent-issues/ckan/config/routing.py"
               data-name="1067-datastore-percent-issues"
               data-skip-pjax="true"
               rel="nofollow">
              <svg aria-hidden="true" class="octicon octicon-check select-menu-item-icon" height="16" version="1.1" viewBox="0 0 12 16" width="12"><path fill-rule="evenodd" d="M12 5l-8 8-4-4 1.5-1.5L4 10l6.5-6.5z"/></svg>
              <span class="select-menu-item-text css-truncate-target js-select-menu-filter-text">
                1067-datastore-percent-issues
              </span>
            </a>
            <a class="select-menu-item js-navigation-item js-navigation-open "
               href="/ckan/ckan/blob/1069-style-guide/ckan/config/routing.py"
               data-name="1069-style-guide"
               data-skip-pjax="true"
               rel="nofollow">
              <svg aria-hidden="true" class="octicon octicon-check select-menu-item-icon" height="16" version="1.1" viewBox="0 0 12 16" width="12"><path fill-rule="evenodd" d="M12 5l-8 8-4-4 1.5-1.5L4 10l6.5-6.5z"/></svg>
              <span class="select-menu-item-text css-truncate-target js-select-menu-filter-text">
                1069-style-guide
              </span>
            </a>
            <a class="select-menu-item js-navigation-item js-navigation-open "
               href="/ckan/ckan/blob/1071-close-div/ckan/config/routing.py"
               data-name="1071-close-div"
               data-skip-pjax="true"
               rel="nofollow">
              <svg aria-hidden="true" class="octicon octicon-check select-menu-item-icon" height="16" version="1.1" viewBox="0 0 12 16" width="12"><path fill-rule="evenodd" d="M12 5l-8 8-4-4 1.5-1.5L4 10l6.5-6.5z"/></svg>
              <span class="select-menu-item-text css-truncate-target js-select-menu-filter-text">
                1071-close-div
              </span>
            </a>
            <a class="select-menu-item js-navigation-item js-navigation-open "
               href="/ckan/ckan/blob/1078-package_show-performance/ckan/config/routing.py"
               data-name="1078-package_show-performance"
               data-skip-pjax="true"
               rel="nofollow">
              <svg aria-hidden="true" class="octicon octicon-check select-menu-item-icon" height="16" version="1.1" viewBox="0 0 12 16" width="12"><path fill-rule="evenodd" d="M12 5l-8 8-4-4 1.5-1.5L4 10l6.5-6.5z"/></svg>
              <span class="select-menu-item-text css-truncate-target js-select-menu-filter-text">
                1078-package_show-performance
              </span>
            </a>
            <a class="select-menu-item js-navigation-item js-navigation-open "
               href="/ckan/ckan/blob/1083-upgrade-minor-version-instructions/ckan/config/routing.py"
               data-name="1083-upgrade-minor-version-instructions"
               data-skip-pjax="true"
               rel="nofollow">
              <svg aria-hidden="true" class="octicon octicon-check select-menu-item-icon" height="16" version="1.1" viewBox="0 0 12 16" width="12"><path fill-rule="evenodd" d="M12 5l-8 8-4-4 1.5-1.5L4 10l6.5-6.5z"/></svg>
              <span class="select-menu-item-text css-truncate-target js-select-menu-filter-text">
                1083-upgrade-minor-version-instructions
              </span>
            </a>
            <a class="select-menu-item js-navigation-item js-navigation-open "
               href="/ckan/ckan/blob/1089-required-fields/ckan/config/routing.py"
               data-name="1089-required-fields"
               data-skip-pjax="true"
               rel="nofollow">
              <svg aria-hidden="true" class="octicon octicon-check select-menu-item-icon" height="16" version="1.1" viewBox="0 0 12 16" width="12"><path fill-rule="evenodd" d="M12 5l-8 8-4-4 1.5-1.5L4 10l6.5-6.5z"/></svg>
              <span class="select-menu-item-text css-truncate-target js-select-menu-filter-text">
                1089-required-fields
              </span>
            </a>
            <a class="select-menu-item js-navigation-item js-navigation-open "
               href="/ckan/ckan/blob/1092-helper-text/ckan/config/routing.py"
               data-name="1092-helper-text"
               data-skip-pjax="true"
               rel="nofollow">
              <svg aria-hidden="true" class="octicon octicon-check select-menu-item-icon" height="16" version="1.1" viewBox="0 0 12 16" width="12"><path fill-rule="evenodd" d="M12 5l-8 8-4-4 1.5-1.5L4 10l6.5-6.5z"/></svg>
              <span class="select-menu-item-text css-truncate-target js-select-menu-filter-text">
                1092-helper-text
              </span>
            </a>
            <a class="select-menu-item js-navigation-item js-navigation-open "
               href="/ckan/ckan/blob/1094-not-sorry-just-empty/ckan/config/routing.py"
               data-name="1094-not-sorry-just-empty"
               data-skip-pjax="true"
               rel="nofollow">
              <svg aria-hidden="true" class="octicon octicon-check select-menu-item-icon" height="16" version="1.1" viewBox="0 0 12 16" width="12"><path fill-rule="evenodd" d="M12 5l-8 8-4-4 1.5-1.5L4 10l6.5-6.5z"/></svg>
              <span class="select-menu-item-text css-truncate-target js-select-menu-filter-text">
                1094-not-sorry-just-empty
              </span>
            </a>
            <a class="select-menu-item js-navigation-item js-navigation-open "
               href="/ckan/ckan/blob/1096-org-members/ckan/config/routing.py"
               data-name="1096-org-members"
               data-skip-pjax="true"
               rel="nofollow">
              <svg aria-hidden="true" class="octicon octicon-check select-menu-item-icon" height="16" version="1.1" viewBox="0 0 12 16" width="12"><path fill-rule="evenodd" d="M12 5l-8 8-4-4 1.5-1.5L4 10l6.5-6.5z"/></svg>
              <span class="select-menu-item-text css-truncate-target js-select-menu-filter-text">
                1096-org-members
              </span>
            </a>
            <a class="select-menu-item js-navigation-item js-navigation-open "
               href="/ckan/ckan/blob/1102-dataset-group-add/ckan/config/routing.py"
               data-name="1102-dataset-group-add"
               data-skip-pjax="true"
               rel="nofollow">
              <svg aria-hidden="true" class="octicon octicon-check select-menu-item-icon" height="16" version="1.1" viewBox="0 0 12 16" width="12"><path fill-rule="evenodd" d="M12 5l-8 8-4-4 1.5-1.5L4 10l6.5-6.5z"/></svg>
              <span class="select-menu-item-text css-truncate-target js-select-menu-filter-text">
                1102-dataset-group-add
              </span>
            </a>
            <a class="select-menu-item js-navigation-item js-navigation-open "
               href="/ckan/ckan/blob/1110-user-read_base-fixes/ckan/config/routing.py"
               data-name="1110-user-read_base-fixes"
               data-skip-pjax="true"
               rel="nofollow">
              <svg aria-hidden="true" class="octicon octicon-check select-menu-item-icon" height="16" version="1.1" viewBox="0 0 12 16" width="12"><path fill-rule="evenodd" d="M12 5l-8 8-4-4 1.5-1.5L4 10l6.5-6.5z"/></svg>
              <span class="select-menu-item-text css-truncate-target js-select-menu-filter-text">
                1110-user-read_base-fixes
              </span>
            </a>
            <a class="select-menu-item js-navigation-item js-navigation-open "
               href="/ckan/ckan/blob/1115-header-block-recursion/ckan/config/routing.py"
               data-name="1115-header-block-recursion"
               data-skip-pjax="true"
               rel="nofollow">
              <svg aria-hidden="true" class="octicon octicon-check select-menu-item-icon" height="16" version="1.1" viewBox="0 0 12 16" width="12"><path fill-rule="evenodd" d="M12 5l-8 8-4-4 1.5-1.5L4 10l6.5-6.5z"/></svg>
              <span class="select-menu-item-text css-truncate-target js-select-menu-filter-text">
                1115-header-block-recursion
              </span>
            </a>
            <a class="select-menu-item js-navigation-item js-navigation-open "
               href="/ckan/ckan/blob/1118-error-not-caught/ckan/config/routing.py"
               data-name="1118-error-not-caught"
               data-skip-pjax="true"
               rel="nofollow">
              <svg aria-hidden="true" class="octicon octicon-check select-menu-item-icon" height="16" version="1.1" viewBox="0 0 12 16" width="12"><path fill-rule="evenodd" d="M12 5l-8 8-4-4 1.5-1.5L4 10l6.5-6.5z"/></svg>
              <span class="select-menu-item-text css-truncate-target js-select-menu-filter-text">
                1118-error-not-caught
              </span>
            </a>
            <a class="select-menu-item js-navigation-item js-navigation-open "
               href="/ckan/ckan/blob/1119-text-preview-can-preview-xml-and-json/ckan/config/routing.py"
               data-name="1119-text-preview-can-preview-xml-and-json"
               data-skip-pjax="true"
               rel="nofollow">
              <svg aria-hidden="true" class="octicon octicon-check select-menu-item-icon" height="16" version="1.1" viewBox="0 0 12 16" width="12"><path fill-rule="evenodd" d="M12 5l-8 8-4-4 1.5-1.5L4 10l6.5-6.5z"/></svg>
              <span class="select-menu-item-text css-truncate-target js-select-menu-filter-text">
                1119-text-preview-can-preview-xml-and-json
              </span>
            </a>
            <a class="select-menu-item js-navigation-item js-navigation-open "
               href="/ckan/ckan/blob/1120-datastore-make-public/ckan/config/routing.py"
               data-name="1120-datastore-make-public"
               data-skip-pjax="true"
               rel="nofollow">
              <svg aria-hidden="true" class="octicon octicon-check select-menu-item-icon" height="16" version="1.1" viewBox="0 0 12 16" width="12"><path fill-rule="evenodd" d="M12 5l-8 8-4-4 1.5-1.5L4 10l6.5-6.5z"/></svg>
              <span class="select-menu-item-text css-truncate-target js-select-menu-filter-text">
                1120-datastore-make-public
              </span>
            </a>
            <a class="select-menu-item js-navigation-item js-navigation-open "
               href="/ckan/ckan/blob/1122-nose-tests-are-noisy-on-travis/ckan/config/routing.py"
               data-name="1122-nose-tests-are-noisy-on-travis"
               data-skip-pjax="true"
               rel="nofollow">
              <svg aria-hidden="true" class="octicon octicon-check select-menu-item-icon" height="16" version="1.1" viewBox="0 0 12 16" width="12"><path fill-rule="evenodd" d="M12 5l-8 8-4-4 1.5-1.5L4 10l6.5-6.5z"/></svg>
              <span class="select-menu-item-text css-truncate-target js-select-menu-filter-text">
                1122-nose-tests-are-noisy-on-travis
              </span>
            </a>
            <a class="select-menu-item js-navigation-item js-navigation-open "
               href="/ckan/ckan/blob/1139-remove-moderated-from-config-docs/ckan/config/routing.py"
               data-name="1139-remove-moderated-from-config-docs"
               data-skip-pjax="true"
               rel="nofollow">
              <svg aria-hidden="true" class="octicon octicon-check select-menu-item-icon" height="16" version="1.1" viewBox="0 0 12 16" width="12"><path fill-rule="evenodd" d="M12 5l-8 8-4-4 1.5-1.5L4 10l6.5-6.5z"/></svg>
              <span class="select-menu-item-text css-truncate-target js-select-menu-filter-text">
                1139-remove-moderated-from-config-docs
              </span>
            </a>
            <a class="select-menu-item js-navigation-item js-navigation-open "
               href="/ckan/ckan/blob/1140-example/ckan/config/routing.py"
               data-name="1140-example"
               data-skip-pjax="true"
               rel="nofollow">
              <svg aria-hidden="true" class="octicon octicon-check select-menu-item-icon" height="16" version="1.1" viewBox="0 0 12 16" width="12"><path fill-rule="evenodd" d="M12 5l-8 8-4-4 1.5-1.5L4 10l6.5-6.5z"/></svg>
              <span class="select-menu-item-text css-truncate-target js-select-menu-filter-text">
                1140-example
              </span>
            </a>
            <a class="select-menu-item js-navigation-item js-navigation-open "
               href="/ckan/ckan/blob/1143-docs-test-plugins-errors/ckan/config/routing.py"
               data-name="1143-docs-test-plugins-errors"
               data-skip-pjax="true"
               rel="nofollow">
              <svg aria-hidden="true" class="octicon octicon-check select-menu-item-icon" height="16" version="1.1" viewBox="0 0 12 16" width="12"><path fill-rule="evenodd" d="M12 5l-8 8-4-4 1.5-1.5L4 10l6.5-6.5z"/></svg>
              <span class="select-menu-item-text css-truncate-target js-select-menu-filter-text">
                1143-docs-test-plugins-errors
              </span>
            </a>
            <a class="select-menu-item js-navigation-item js-navigation-open "
               href="/ckan/ckan/blob/1148-whitespace-strip-validator/ckan/config/routing.py"
               data-name="1148-whitespace-strip-validator"
               data-skip-pjax="true"
               rel="nofollow">
              <svg aria-hidden="true" class="octicon octicon-check select-menu-item-icon" height="16" version="1.1" viewBox="0 0 12 16" width="12"><path fill-rule="evenodd" d="M12 5l-8 8-4-4 1.5-1.5L4 10l6.5-6.5z"/></svg>
              <span class="select-menu-item-text css-truncate-target js-select-menu-filter-text">
                1148-whitespace-strip-validator
              </span>
            </a>
            <a class="select-menu-item js-navigation-item js-navigation-open "
               href="/ckan/ckan/blob/1149-requirements/ckan/config/routing.py"
               data-name="1149-requirements"
               data-skip-pjax="true"
               rel="nofollow">
              <svg aria-hidden="true" class="octicon octicon-check select-menu-item-icon" height="16" version="1.1" viewBox="0 0 12 16" width="12"><path fill-rule="evenodd" d="M12 5l-8 8-4-4 1.5-1.5L4 10l6.5-6.5z"/></svg>
              <span class="select-menu-item-text css-truncate-target js-select-menu-filter-text">
                1149-requirements
              </span>
            </a>
            <a class="select-menu-item js-navigation-item js-navigation-open "
               href="/ckan/ckan/blob/1151-auth-datastore-fix/ckan/config/routing.py"
               data-name="1151-auth-datastore-fix"
               data-skip-pjax="true"
               rel="nofollow">
              <svg aria-hidden="true" class="octicon octicon-check select-menu-item-icon" height="16" version="1.1" viewBox="0 0 12 16" width="12"><path fill-rule="evenodd" d="M12 5l-8 8-4-4 1.5-1.5L4 10l6.5-6.5z"/></svg>
              <span class="select-menu-item-text css-truncate-target js-select-menu-filter-text">
                1151-auth-datastore-fix
              </span>
            </a>
            <a class="select-menu-item js-navigation-item js-navigation-open "
               href="/ckan/ckan/blob/1157-update-release-policy/ckan/config/routing.py"
               data-name="1157-update-release-policy"
               data-skip-pjax="true"
               rel="nofollow">
              <svg aria-hidden="true" class="octicon octicon-check select-menu-item-icon" height="16" version="1.1" viewBox="0 0 12 16" width="12"><path fill-rule="evenodd" d="M12 5l-8 8-4-4 1.5-1.5L4 10l6.5-6.5z"/></svg>
              <span class="select-menu-item-text css-truncate-target js-select-menu-filter-text">
                1157-update-release-policy
              </span>
            </a>
            <a class="select-menu-item js-navigation-item js-navigation-open "
               href="/ckan/ckan/blob/1159-recently-changed-packages-helper/ckan/config/routing.py"
               data-name="1159-recently-changed-packages-helper"
               data-skip-pjax="true"
               rel="nofollow">
              <svg aria-hidden="true" class="octicon octicon-check select-menu-item-icon" height="16" version="1.1" viewBox="0 0 12 16" width="12"><path fill-rule="evenodd" d="M12 5l-8 8-4-4 1.5-1.5L4 10l6.5-6.5z"/></svg>
              <span class="select-menu-item-text css-truncate-target js-select-menu-filter-text">
                1159-recently-changed-packages-helper
              </span>
            </a>
            <a class="select-menu-item js-navigation-item js-navigation-open "
               href="/ckan/ckan/blob/1172-groups-list-use-dictization/ckan/config/routing.py"
               data-name="1172-groups-list-use-dictization"
               data-skip-pjax="true"
               rel="nofollow">
              <svg aria-hidden="true" class="octicon octicon-check select-menu-item-icon" height="16" version="1.1" viewBox="0 0 12 16" width="12"><path fill-rule="evenodd" d="M12 5l-8 8-4-4 1.5-1.5L4 10l6.5-6.5z"/></svg>
              <span class="select-menu-item-text css-truncate-target js-select-menu-filter-text">
                1172-groups-list-use-dictization
              </span>
            </a>
            <a class="select-menu-item js-navigation-item js-navigation-open "
               href="/ckan/ckan/blob/1183-datapusher-status/ckan/config/routing.py"
               data-name="1183-datapusher-status"
               data-skip-pjax="true"
               rel="nofollow">
              <svg aria-hidden="true" class="octicon octicon-check select-menu-item-icon" height="16" version="1.1" viewBox="0 0 12 16" width="12"><path fill-rule="evenodd" d="M12 5l-8 8-4-4 1.5-1.5L4 10l6.5-6.5z"/></svg>
              <span class="select-menu-item-text css-truncate-target js-select-menu-filter-text">
                1183-datapusher-status
              </span>
            </a>
            <a class="select-menu-item js-navigation-item js-navigation-open "
               href="/ckan/ckan/blob/1184-package_create-auth-fixes/ckan/config/routing.py"
               data-name="1184-package_create-auth-fixes"
               data-skip-pjax="true"
               rel="nofollow">
              <svg aria-hidden="true" class="octicon octicon-check select-menu-item-icon" height="16" version="1.1" viewBox="0 0 12 16" width="12"><path fill-rule="evenodd" d="M12 5l-8 8-4-4 1.5-1.5L4 10l6.5-6.5z"/></svg>
              <span class="select-menu-item-text css-truncate-target js-select-menu-filter-text">
                1184-package_create-auth-fixes
              </span>
            </a>
            <a class="select-menu-item js-navigation-item js-navigation-open "
               href="/ckan/ckan/blob/1188-fix-org-list-dataset-form/ckan/config/routing.py"
               data-name="1188-fix-org-list-dataset-form"
               data-skip-pjax="true"
               rel="nofollow">
              <svg aria-hidden="true" class="octicon octicon-check select-menu-item-icon" height="16" version="1.1" viewBox="0 0 12 16" width="12"><path fill-rule="evenodd" d="M12 5l-8 8-4-4 1.5-1.5L4 10l6.5-6.5z"/></svg>
              <span class="select-menu-item-text css-truncate-target js-select-menu-filter-text">
                1188-fix-org-list-dataset-form
              </span>
            </a>
            <a class="select-menu-item js-navigation-item js-navigation-open "
               href="/ckan/ckan/blob/1191-group-show-no-user-data/ckan/config/routing.py"
               data-name="1191-group-show-no-user-data"
               data-skip-pjax="true"
               rel="nofollow">
              <svg aria-hidden="true" class="octicon octicon-check select-menu-item-icon" height="16" version="1.1" viewBox="0 0 12 16" width="12"><path fill-rule="evenodd" d="M12 5l-8 8-4-4 1.5-1.5L4 10l6.5-6.5z"/></svg>
              <span class="select-menu-item-text css-truncate-target js-select-menu-filter-text">
                1191-group-show-no-user-data
              </span>
            </a>
            <a class="select-menu-item js-navigation-item js-navigation-open "
               href="/ckan/ckan/blob/1196-separate-datapusher/ckan/config/routing.py"
               data-name="1196-separate-datapusher"
               data-skip-pjax="true"
               rel="nofollow">
              <svg aria-hidden="true" class="octicon octicon-check select-menu-item-icon" height="16" version="1.1" viewBox="0 0 12 16" width="12"><path fill-rule="evenodd" d="M12 5l-8 8-4-4 1.5-1.5L4 10l6.5-6.5z"/></svg>
              <span class="select-menu-item-text css-truncate-target js-select-menu-filter-text">
                1196-separate-datapusher
              </span>
            </a>
            <a class="select-menu-item js-navigation-item js-navigation-open "
               href="/ckan/ckan/blob/1197-rtd-fix/ckan/config/routing.py"
               data-name="1197-rtd-fix"
               data-skip-pjax="true"
               rel="nofollow">
              <svg aria-hidden="true" class="octicon octicon-check select-menu-item-icon" height="16" version="1.1" viewBox="0 0 12 16" width="12"><path fill-rule="evenodd" d="M12 5l-8 8-4-4 1.5-1.5L4 10l6.5-6.5z"/></svg>
              <span class="select-menu-item-text css-truncate-target js-select-menu-filter-text">
                1197-rtd-fix
              </span>
            </a>
            <a class="select-menu-item js-navigation-item js-navigation-open "
               href="/ckan/ckan/blob/1204-fix-datastore-auth-audit/ckan/config/routing.py"
               data-name="1204-fix-datastore-auth-audit"
               data-skip-pjax="true"
               rel="nofollow">
              <svg aria-hidden="true" class="octicon octicon-check select-menu-item-icon" height="16" version="1.1" viewBox="0 0 12 16" width="12"><path fill-rule="evenodd" d="M12 5l-8 8-4-4 1.5-1.5L4 10l6.5-6.5z"/></svg>
              <span class="select-menu-item-text css-truncate-target js-select-menu-filter-text">
                1204-fix-datastore-auth-audit
              </span>
            </a>
            <a class="select-menu-item js-navigation-item js-navigation-open "
               href="/ckan/ckan/blob/1217-trash-redirect/ckan/config/routing.py"
               data-name="1217-trash-redirect"
               data-skip-pjax="true"
               rel="nofollow">
              <svg aria-hidden="true" class="octicon octicon-check select-menu-item-icon" height="16" version="1.1" viewBox="0 0 12 16" width="12"><path fill-rule="evenodd" d="M12 5l-8 8-4-4 1.5-1.5L4 10l6.5-6.5z"/></svg>
              <span class="select-menu-item-text css-truncate-target js-select-menu-filter-text">
                1217-trash-redirect
              </span>
            </a>
            <a class="select-menu-item js-navigation-item js-navigation-open "
               href="/ckan/ckan/blob/1218-remove-__extras/ckan/config/routing.py"
               data-name="1218-remove-__extras"
               data-skip-pjax="true"
               rel="nofollow">
              <svg aria-hidden="true" class="octicon octicon-check select-menu-item-icon" height="16" version="1.1" viewBox="0 0 12 16" width="12"><path fill-rule="evenodd" d="M12 5l-8 8-4-4 1.5-1.5L4 10l6.5-6.5z"/></svg>
              <span class="select-menu-item-text css-truncate-target js-select-menu-filter-text">
                1218-remove-__extras
              </span>
            </a>
            <a class="select-menu-item js-navigation-item js-navigation-open "
               href="/ckan/ckan/blob/1221-preview-fails-private-datasets/ckan/config/routing.py"
               data-name="1221-preview-fails-private-datasets"
               data-skip-pjax="true"
               rel="nofollow">
              <svg aria-hidden="true" class="octicon octicon-check select-menu-item-icon" height="16" version="1.1" viewBox="0 0 12 16" width="12"><path fill-rule="evenodd" d="M12 5l-8 8-4-4 1.5-1.5L4 10l6.5-6.5z"/></svg>
              <span class="select-menu-item-text css-truncate-target js-select-menu-filter-text">
                1221-preview-fails-private-datasets
              </span>
            </a>
            <a class="select-menu-item js-navigation-item js-navigation-open "
               href="/ckan/ckan/blob/1228-dictize-whitespace/ckan/config/routing.py"
               data-name="1228-dictize-whitespace"
               data-skip-pjax="true"
               rel="nofollow">
              <svg aria-hidden="true" class="octicon octicon-check select-menu-item-icon" height="16" version="1.1" viewBox="0 0 12 16" width="12"><path fill-rule="evenodd" d="M12 5l-8 8-4-4 1.5-1.5L4 10l6.5-6.5z"/></svg>
              <span class="select-menu-item-text css-truncate-target js-select-menu-filter-text">
                1228-dictize-whitespace
              </span>
            </a>
            <a class="select-menu-item js-navigation-item js-navigation-open "
               href="/ckan/ckan/blob/1231-best-practices-for-writing-extensions-mistake/ckan/config/routing.py"
               data-name="1231-best-practices-for-writing-extensions-mistake"
               data-skip-pjax="true"
               rel="nofollow">
              <svg aria-hidden="true" class="octicon octicon-check select-menu-item-icon" height="16" version="1.1" viewBox="0 0 12 16" width="12"><path fill-rule="evenodd" d="M12 5l-8 8-4-4 1.5-1.5L4 10l6.5-6.5z"/></svg>
              <span class="select-menu-item-text css-truncate-target js-select-menu-filter-text">
                1231-best-practices-for-writing-extensions-mistake
              </span>
            </a>
            <a class="select-menu-item js-navigation-item js-navigation-open "
               href="/ckan/ckan/blob/1232-slug-edit/ckan/config/routing.py"
               data-name="1232-slug-edit"
               data-skip-pjax="true"
               rel="nofollow">
              <svg aria-hidden="true" class="octicon octicon-check select-menu-item-icon" height="16" version="1.1" viewBox="0 0 12 16" width="12"><path fill-rule="evenodd" d="M12 5l-8 8-4-4 1.5-1.5L4 10l6.5-6.5z"/></svg>
              <span class="select-menu-item-text css-truncate-target js-select-menu-filter-text">
                1232-slug-edit
              </span>
            </a>
            <a class="select-menu-item js-navigation-item js-navigation-open "
               href="/ckan/ckan/blob/1238-number_span-span-fix/ckan/config/routing.py"
               data-name="1238-number_span-span-fix"
               data-skip-pjax="true"
               rel="nofollow">
              <svg aria-hidden="true" class="octicon octicon-check select-menu-item-icon" height="16" version="1.1" viewBox="0 0 12 16" width="12"><path fill-rule="evenodd" d="M12 5l-8 8-4-4 1.5-1.5L4 10l6.5-6.5z"/></svg>
              <span class="select-menu-item-text css-truncate-target js-select-menu-filter-text">
                1238-number_span-span-fix
              </span>
            </a>
            <a class="select-menu-item js-navigation-item js-navigation-open "
               href="/ckan/ckan/blob/1242-notifications-youve-been-added-to-group/ckan/config/routing.py"
               data-name="1242-notifications-youve-been-added-to-group"
               data-skip-pjax="true"
               rel="nofollow">
              <svg aria-hidden="true" class="octicon octicon-check select-menu-item-icon" height="16" version="1.1" viewBox="0 0 12 16" width="12"><path fill-rule="evenodd" d="M12 5l-8 8-4-4 1.5-1.5L4 10l6.5-6.5z"/></svg>
              <span class="select-menu-item-text css-truncate-target js-select-menu-filter-text">
                1242-notifications-youve-been-added-to-group
              </span>
            </a>
            <a class="select-menu-item js-navigation-item js-navigation-open "
               href="/ckan/ckan/blob/1244-cli-user-fullname-unicode/ckan/config/routing.py"
               data-name="1244-cli-user-fullname-unicode"
               data-skip-pjax="true"
               rel="nofollow">
              <svg aria-hidden="true" class="octicon octicon-check select-menu-item-icon" height="16" version="1.1" viewBox="0 0 12 16" width="12"><path fill-rule="evenodd" d="M12 5l-8 8-4-4 1.5-1.5L4 10l6.5-6.5z"/></svg>
              <span class="select-menu-item-text css-truncate-target js-select-menu-filter-text">
                1244-cli-user-fullname-unicode
              </span>
            </a>
            <a class="select-menu-item js-navigation-item js-navigation-open "
               href="/ckan/ckan/blob/1251-resource-view/ckan/config/routing.py"
               data-name="1251-resource-view"
               data-skip-pjax="true"
               rel="nofollow">
              <svg aria-hidden="true" class="octicon octicon-check select-menu-item-icon" height="16" version="1.1" viewBox="0 0 12 16" width="12"><path fill-rule="evenodd" d="M12 5l-8 8-4-4 1.5-1.5L4 10l6.5-6.5z"/></svg>
              <span class="select-menu-item-text css-truncate-target js-select-menu-filter-text">
                1251-resource-view
              </span>
            </a>
            <a class="select-menu-item js-navigation-item js-navigation-open "
               href="/ckan/ckan/blob/1258-validator-decorators/ckan/config/routing.py"
               data-name="1258-validator-decorators"
               data-skip-pjax="true"
               rel="nofollow">
              <svg aria-hidden="true" class="octicon octicon-check select-menu-item-icon" height="16" version="1.1" viewBox="0 0 12 16" width="12"><path fill-rule="evenodd" d="M12 5l-8 8-4-4 1.5-1.5L4 10l6.5-6.5z"/></svg>
              <span class="select-menu-item-text css-truncate-target js-select-menu-filter-text">
                1258-validator-decorators
              </span>
            </a>
            <a class="select-menu-item js-navigation-item js-navigation-open "
               href="/ckan/ckan/blob/1264-licenses-not-license-you-dummy/ckan/config/routing.py"
               data-name="1264-licenses-not-license-you-dummy"
               data-skip-pjax="true"
               rel="nofollow">
              <svg aria-hidden="true" class="octicon octicon-check select-menu-item-icon" height="16" version="1.1" viewBox="0 0 12 16" width="12"><path fill-rule="evenodd" d="M12 5l-8 8-4-4 1.5-1.5L4 10l6.5-6.5z"/></svg>
              <span class="select-menu-item-text css-truncate-target js-select-menu-filter-text">
                1264-licenses-not-license-you-dummy
              </span>
            </a>
            <a class="select-menu-item js-navigation-item js-navigation-open "
               href="/ckan/ckan/blob/1267-new-docs-for-contributing-to-the-docs/ckan/config/routing.py"
               data-name="1267-new-docs-for-contributing-to-the-docs"
               data-skip-pjax="true"
               rel="nofollow">
              <svg aria-hidden="true" class="octicon octicon-check select-menu-item-icon" height="16" version="1.1" viewBox="0 0 12 16" width="12"><path fill-rule="evenodd" d="M12 5l-8 8-4-4 1.5-1.5L4 10l6.5-6.5z"/></svg>
              <span class="select-menu-item-text css-truncate-target js-select-menu-filter-text">
                1267-new-docs-for-contributing-to-the-docs
              </span>
            </a>
            <a class="select-menu-item js-navigation-item js-navigation-open "
               href="/ckan/ckan/blob/1268-add-step-upgrade-source/ckan/config/routing.py"
               data-name="1268-add-step-upgrade-source"
               data-skip-pjax="true"
               rel="nofollow">
              <svg aria-hidden="true" class="octicon octicon-check select-menu-item-icon" height="16" version="1.1" viewBox="0 0 12 16" width="12"><path fill-rule="evenodd" d="M12 5l-8 8-4-4 1.5-1.5L4 10l6.5-6.5z"/></svg>
              <span class="select-menu-item-text css-truncate-target js-select-menu-filter-text">
                1268-add-step-upgrade-source
              </span>
            </a>
            <a class="select-menu-item js-navigation-item js-navigation-open "
               href="/ckan/ckan/blob/1269-dataset-and-resource-edit-tweaks/ckan/config/routing.py"
               data-name="1269-dataset-and-resource-edit-tweaks"
               data-skip-pjax="true"
               rel="nofollow">
              <svg aria-hidden="true" class="octicon octicon-check select-menu-item-icon" height="16" version="1.1" viewBox="0 0 12 16" width="12"><path fill-rule="evenodd" d="M12 5l-8 8-4-4 1.5-1.5L4 10l6.5-6.5z"/></svg>
              <span class="select-menu-item-text css-truncate-target js-select-menu-filter-text">
                1269-dataset-and-resource-edit-tweaks
              </span>
            </a>
            <a class="select-menu-item js-navigation-item js-navigation-open "
               href="/ckan/ckan/blob/1272-datastore-key-error/ckan/config/routing.py"
               data-name="1272-datastore-key-error"
               data-skip-pjax="true"
               rel="nofollow">
              <svg aria-hidden="true" class="octicon octicon-check select-menu-item-icon" height="16" version="1.1" viewBox="0 0 12 16" width="12"><path fill-rule="evenodd" d="M12 5l-8 8-4-4 1.5-1.5L4 10l6.5-6.5z"/></svg>
              <span class="select-menu-item-text css-truncate-target js-select-menu-filter-text">
                1272-datastore-key-error
              </span>
            </a>
            <a class="select-menu-item js-navigation-item js-navigation-open "
               href="/ckan/ckan/blob/1277-resource-reordering/ckan/config/routing.py"
               data-name="1277-resource-reordering"
               data-skip-pjax="true"
               rel="nofollow">
              <svg aria-hidden="true" class="octicon octicon-check select-menu-item-icon" height="16" version="1.1" viewBox="0 0 12 16" width="12"><path fill-rule="evenodd" d="M12 5l-8 8-4-4 1.5-1.5L4 10l6.5-6.5z"/></svg>
              <span class="select-menu-item-text css-truncate-target js-select-menu-filter-text">
                1277-resource-reordering
              </span>
            </a>
            <a class="select-menu-item js-navigation-item js-navigation-open "
               href="/ckan/ckan/blob/1290-keep-database-for-tests/ckan/config/routing.py"
               data-name="1290-keep-database-for-tests"
               data-skip-pjax="true"
               rel="nofollow">
              <svg aria-hidden="true" class="octicon octicon-check select-menu-item-icon" height="16" version="1.1" viewBox="0 0 12 16" width="12"><path fill-rule="evenodd" d="M12 5l-8 8-4-4 1.5-1.5L4 10l6.5-6.5z"/></svg>
              <span class="select-menu-item-text css-truncate-target js-select-menu-filter-text">
                1290-keep-database-for-tests
              </span>
            </a>
            <a class="select-menu-item js-navigation-item js-navigation-open "
               href="/ckan/ckan/blob/1294-update-docs-theme/ckan/config/routing.py"
               data-name="1294-update-docs-theme"
               data-skip-pjax="true"
               rel="nofollow">
              <svg aria-hidden="true" class="octicon octicon-check select-menu-item-icon" height="16" version="1.1" viewBox="0 0 12 16" width="12"><path fill-rule="evenodd" d="M12 5l-8 8-4-4 1.5-1.5L4 10l6.5-6.5z"/></svg>
              <span class="select-menu-item-text css-truncate-target js-select-menu-filter-text">
                1294-update-docs-theme
              </span>
            </a>
            <a class="select-menu-item js-navigation-item js-navigation-open "
               href="/ckan/ckan/blob/1295-package_list-private-datasets/ckan/config/routing.py"
               data-name="1295-package_list-private-datasets"
               data-skip-pjax="true"
               rel="nofollow">
              <svg aria-hidden="true" class="octicon octicon-check select-menu-item-icon" height="16" version="1.1" viewBox="0 0 12 16" width="12"><path fill-rule="evenodd" d="M12 5l-8 8-4-4 1.5-1.5L4 10l6.5-6.5z"/></svg>
              <span class="select-menu-item-text css-truncate-target js-select-menu-filter-text">
                1295-package_list-private-datasets
              </span>
            </a>
            <a class="select-menu-item js-navigation-item js-navigation-open "
               href="/ckan/ckan/blob/1298-fix-orgs-activity-about-page/ckan/config/routing.py"
               data-name="1298-fix-orgs-activity-about-page"
               data-skip-pjax="true"
               rel="nofollow">
              <svg aria-hidden="true" class="octicon octicon-check select-menu-item-icon" height="16" version="1.1" viewBox="0 0 12 16" width="12"><path fill-rule="evenodd" d="M12 5l-8 8-4-4 1.5-1.5L4 10l6.5-6.5z"/></svg>
              <span class="select-menu-item-text css-truncate-target js-select-menu-filter-text">
                1298-fix-orgs-activity-about-page
              </span>
            </a>
            <a class="select-menu-item js-navigation-item js-navigation-open "
               href="/ckan/ckan/blob/1301-template-blocks/ckan/config/routing.py"
               data-name="1301-template-blocks"
               data-skip-pjax="true"
               rel="nofollow">
              <svg aria-hidden="true" class="octicon octicon-check select-menu-item-icon" height="16" version="1.1" viewBox="0 0 12 16" width="12"><path fill-rule="evenodd" d="M12 5l-8 8-4-4 1.5-1.5L4 10l6.5-6.5z"/></svg>
              <span class="select-menu-item-text css-truncate-target js-select-menu-filter-text">
                1301-template-blocks
              </span>
            </a>
            <a class="select-menu-item js-navigation-item js-navigation-open "
               href="/ckan/ckan/blob/1302-remove-mentions-of-no-description/ckan/config/routing.py"
               data-name="1302-remove-mentions-of-no-description"
               data-skip-pjax="true"
               rel="nofollow">
              <svg aria-hidden="true" class="octicon octicon-check select-menu-item-icon" height="16" version="1.1" viewBox="0 0 12 16" width="12"><path fill-rule="evenodd" d="M12 5l-8 8-4-4 1.5-1.5L4 10l6.5-6.5z"/></svg>
              <span class="select-menu-item-text css-truncate-target js-select-menu-filter-text">
                1302-remove-mentions-of-no-description
              </span>
            </a>
            <a class="select-menu-item js-navigation-item js-navigation-open "
               href="/ckan/ckan/blob/1305-undefined-popover/ckan/config/routing.py"
               data-name="1305-undefined-popover"
               data-skip-pjax="true"
               rel="nofollow">
              <svg aria-hidden="true" class="octicon octicon-check select-menu-item-icon" height="16" version="1.1" viewBox="0 0 12 16" width="12"><path fill-rule="evenodd" d="M12 5l-8 8-4-4 1.5-1.5L4 10l6.5-6.5z"/></svg>
              <span class="select-menu-item-text css-truncate-target js-select-menu-filter-text">
                1305-undefined-popover
              </span>
            </a>
            <a class="select-menu-item js-navigation-item js-navigation-open "
               href="/ckan/ckan/blob/1307-minor-docs-correction/ckan/config/routing.py"
               data-name="1307-minor-docs-correction"
               data-skip-pjax="true"
               rel="nofollow">
              <svg aria-hidden="true" class="octicon octicon-check select-menu-item-icon" height="16" version="1.1" viewBox="0 0 12 16" width="12"><path fill-rule="evenodd" d="M12 5l-8 8-4-4 1.5-1.5L4 10l6.5-6.5z"/></svg>
              <span class="select-menu-item-text css-truncate-target js-select-menu-filter-text">
                1307-minor-docs-correction
              </span>
            </a>
            <a class="select-menu-item js-navigation-item js-navigation-open "
               href="/ckan/ckan/blob/1314-solr-schema-single-file/ckan/config/routing.py"
               data-name="1314-solr-schema-single-file"
               data-skip-pjax="true"
               rel="nofollow">
              <svg aria-hidden="true" class="octicon octicon-check select-menu-item-icon" height="16" version="1.1" viewBox="0 0 12 16" width="12"><path fill-rule="evenodd" d="M12 5l-8 8-4-4 1.5-1.5L4 10l6.5-6.5z"/></svg>
              <span class="select-menu-item-text css-truncate-target js-select-menu-filter-text">
                1314-solr-schema-single-file
              </span>
            </a>
            <a class="select-menu-item js-navigation-item js-navigation-open "
               href="/ckan/ckan/blob/1318-help_show-action/ckan/config/routing.py"
               data-name="1318-help_show-action"
               data-skip-pjax="true"
               rel="nofollow">
              <svg aria-hidden="true" class="octicon octicon-check select-menu-item-icon" height="16" version="1.1" viewBox="0 0 12 16" width="12"><path fill-rule="evenodd" d="M12 5l-8 8-4-4 1.5-1.5L4 10l6.5-6.5z"/></svg>
              <span class="select-menu-item-text css-truncate-target js-select-menu-filter-text">
                1318-help_show-action
              </span>
            </a>
            <a class="select-menu-item js-navigation-item js-navigation-open "
               href="/ckan/ckan/blob/1326-create-dataset-incorrect-org/ckan/config/routing.py"
               data-name="1326-create-dataset-incorrect-org"
               data-skip-pjax="true"
               rel="nofollow">
              <svg aria-hidden="true" class="octicon octicon-check select-menu-item-icon" height="16" version="1.1" viewBox="0 0 12 16" width="12"><path fill-rule="evenodd" d="M12 5l-8 8-4-4 1.5-1.5L4 10l6.5-6.5z"/></svg>
              <span class="select-menu-item-text css-truncate-target js-select-menu-filter-text">
                1326-create-dataset-incorrect-org
              </span>
            </a>
            <a class="select-menu-item js-navigation-item js-navigation-open "
               href="/ckan/ckan/blob/1333-html-comment/ckan/config/routing.py"
               data-name="1333-html-comment"
               data-skip-pjax="true"
               rel="nofollow">
              <svg aria-hidden="true" class="octicon octicon-check select-menu-item-icon" height="16" version="1.1" viewBox="0 0 12 16" width="12"><path fill-rule="evenodd" d="M12 5l-8 8-4-4 1.5-1.5L4 10l6.5-6.5z"/></svg>
              <span class="select-menu-item-text css-truncate-target js-select-menu-filter-text">
                1333-html-comment
              </span>
            </a>
            <a class="select-menu-item js-navigation-item js-navigation-open "
               href="/ckan/ckan/blob/1337-travis-postgres-8.4-cleaned/ckan/config/routing.py"
               data-name="1337-travis-postgres-8.4-cleaned"
               data-skip-pjax="true"
               rel="nofollow">
              <svg aria-hidden="true" class="octicon octicon-check select-menu-item-icon" height="16" version="1.1" viewBox="0 0 12 16" width="12"><path fill-rule="evenodd" d="M12 5l-8 8-4-4 1.5-1.5L4 10l6.5-6.5z"/></svg>
              <span class="select-menu-item-text css-truncate-target js-select-menu-filter-text">
                1337-travis-postgres-8.4-cleaned
              </span>
            </a>
            <a class="select-menu-item js-navigation-item js-navigation-open "
               href="/ckan/ckan/blob/1346-minor-debug-message-tweaks/ckan/config/routing.py"
               data-name="1346-minor-debug-message-tweaks"
               data-skip-pjax="true"
               rel="nofollow">
              <svg aria-hidden="true" class="octicon octicon-check select-menu-item-icon" height="16" version="1.1" viewBox="0 0 12 16" width="12"><path fill-rule="evenodd" d="M12 5l-8 8-4-4 1.5-1.5L4 10l6.5-6.5z"/></svg>
              <span class="select-menu-item-text css-truncate-target js-select-menu-filter-text">
                1346-minor-debug-message-tweaks
              </span>
            </a>
            <a class="select-menu-item js-navigation-item js-navigation-open "
               href="/ckan/ckan/blob/1348-add-dataset-button-org-page/ckan/config/routing.py"
               data-name="1348-add-dataset-button-org-page"
               data-skip-pjax="true"
               rel="nofollow">
              <svg aria-hidden="true" class="octicon octicon-check select-menu-item-icon" height="16" version="1.1" viewBox="0 0 12 16" width="12"><path fill-rule="evenodd" d="M12 5l-8 8-4-4 1.5-1.5L4 10l6.5-6.5z"/></svg>
              <span class="select-menu-item-text css-truncate-target js-select-menu-filter-text">
                1348-add-dataset-button-org-page
              </span>
            </a>
            <a class="select-menu-item js-navigation-item js-navigation-open "
               href="/ckan/ckan/blob/1349-tests-for-theming-example-plugins/ckan/config/routing.py"
               data-name="1349-tests-for-theming-example-plugins"
               data-skip-pjax="true"
               rel="nofollow">
              <svg aria-hidden="true" class="octicon octicon-check select-menu-item-icon" height="16" version="1.1" viewBox="0 0 12 16" width="12"><path fill-rule="evenodd" d="M12 5l-8 8-4-4 1.5-1.5L4 10l6.5-6.5z"/></svg>
              <span class="select-menu-item-text css-truncate-target js-select-menu-filter-text">
                1349-tests-for-theming-example-plugins
              </span>
            </a>
            <a class="select-menu-item js-navigation-item js-navigation-open "
               href="/ckan/ckan/blob/1350-resource-format-remove-text/ckan/config/routing.py"
               data-name="1350-resource-format-remove-text"
               data-skip-pjax="true"
               rel="nofollow">
              <svg aria-hidden="true" class="octicon octicon-check select-menu-item-icon" height="16" version="1.1" viewBox="0 0 12 16" width="12"><path fill-rule="evenodd" d="M12 5l-8 8-4-4 1.5-1.5L4 10l6.5-6.5z"/></svg>
              <span class="select-menu-item-text css-truncate-target js-select-menu-filter-text">
                1350-resource-format-remove-text
              </span>
            </a>
            <a class="select-menu-item js-navigation-item js-navigation-open "
               href="/ckan/ckan/blob/1353-exception-resource-listing/ckan/config/routing.py"
               data-name="1353-exception-resource-listing"
               data-skip-pjax="true"
               rel="nofollow">
              <svg aria-hidden="true" class="octicon octicon-check select-menu-item-icon" height="16" version="1.1" viewBox="0 0 12 16" width="12"><path fill-rule="evenodd" d="M12 5l-8 8-4-4 1.5-1.5L4 10l6.5-6.5z"/></svg>
              <span class="select-menu-item-text css-truncate-target js-select-menu-filter-text">
                1353-exception-resource-listing
              </span>
            </a>
            <a class="select-menu-item js-navigation-item js-navigation-open "
               href="/ckan/ckan/blob/1357-alter-column/ckan/config/routing.py"
               data-name="1357-alter-column"
               data-skip-pjax="true"
               rel="nofollow">
              <svg aria-hidden="true" class="octicon octicon-check select-menu-item-icon" height="16" version="1.1" viewBox="0 0 12 16" width="12"><path fill-rule="evenodd" d="M12 5l-8 8-4-4 1.5-1.5L4 10l6.5-6.5z"/></svg>
              <span class="select-menu-item-text css-truncate-target js-select-menu-filter-text">
                1357-alter-column
              </span>
            </a>
            <a class="select-menu-item js-navigation-item js-navigation-open "
               href="/ckan/ckan/blob/1359-org_rev_list-missing/ckan/config/routing.py"
               data-name="1359-org_rev_list-missing"
               data-skip-pjax="true"
               rel="nofollow">
              <svg aria-hidden="true" class="octicon octicon-check select-menu-item-icon" height="16" version="1.1" viewBox="0 0 12 16" width="12"><path fill-rule="evenodd" d="M12 5l-8 8-4-4 1.5-1.5L4 10l6.5-6.5z"/></svg>
              <span class="select-menu-item-text css-truncate-target js-select-menu-filter-text">
                1359-org_rev_list-missing
              </span>
            </a>
            <a class="select-menu-item js-navigation-item js-navigation-open "
               href="/ckan/ckan/blob/1360-update-docstring/ckan/config/routing.py"
               data-name="1360-update-docstring"
               data-skip-pjax="true"
               rel="nofollow">
              <svg aria-hidden="true" class="octicon octicon-check select-menu-item-icon" height="16" version="1.1" viewBox="0 0 12 16" width="12"><path fill-rule="evenodd" d="M12 5l-8 8-4-4 1.5-1.5L4 10l6.5-6.5z"/></svg>
              <span class="select-menu-item-text css-truncate-target js-select-menu-filter-text">
                1360-update-docstring
              </span>
            </a>
            <a class="select-menu-item js-navigation-item js-navigation-open "
               href="/ckan/ckan/blob/1373-anon-user-datastore-search-sql/ckan/config/routing.py"
               data-name="1373-anon-user-datastore-search-sql"
               data-skip-pjax="true"
               rel="nofollow">
              <svg aria-hidden="true" class="octicon octicon-check select-menu-item-icon" height="16" version="1.1" viewBox="0 0 12 16" width="12"><path fill-rule="evenodd" d="M12 5l-8 8-4-4 1.5-1.5L4 10l6.5-6.5z"/></svg>
              <span class="select-menu-item-text css-truncate-target js-select-menu-filter-text">
                1373-anon-user-datastore-search-sql
              </span>
            </a>
            <a class="select-menu-item js-navigation-item js-navigation-open "
               href="/ckan/ckan/blob/1378/ckan/config/routing.py"
               data-name="1378"
               data-skip-pjax="true"
               rel="nofollow">
              <svg aria-hidden="true" class="octicon octicon-check select-menu-item-icon" height="16" version="1.1" viewBox="0 0 12 16" width="12"><path fill-rule="evenodd" d="M12 5l-8 8-4-4 1.5-1.5L4 10l6.5-6.5z"/></svg>
              <span class="select-menu-item-text css-truncate-target js-select-menu-filter-text">
                1378
              </span>
            </a>
            <a class="select-menu-item js-navigation-item js-navigation-open "
               href="/ckan/ckan/blob/1380-encourage-installing-latest-release/ckan/config/routing.py"
               data-name="1380-encourage-installing-latest-release"
               data-skip-pjax="true"
               rel="nofollow">
              <svg aria-hidden="true" class="octicon octicon-check select-menu-item-icon" height="16" version="1.1" viewBox="0 0 12 16" width="12"><path fill-rule="evenodd" d="M12 5l-8 8-4-4 1.5-1.5L4 10l6.5-6.5z"/></svg>
              <span class="select-menu-item-text css-truncate-target js-select-menu-filter-text">
                1380-encourage-installing-latest-release
              </span>
            </a>
            <a class="select-menu-item js-navigation-item js-navigation-open "
               href="/ckan/ckan/blob/1382-upload-labelling-tweaks/ckan/config/routing.py"
               data-name="1382-upload-labelling-tweaks"
               data-skip-pjax="true"
               rel="nofollow">
              <svg aria-hidden="true" class="octicon octicon-check select-menu-item-icon" height="16" version="1.1" viewBox="0 0 12 16" width="12"><path fill-rule="evenodd" d="M12 5l-8 8-4-4 1.5-1.5L4 10l6.5-6.5z"/></svg>
              <span class="select-menu-item-text css-truncate-target js-select-menu-filter-text">
                1382-upload-labelling-tweaks
              </span>
            </a>
            <a class="select-menu-item js-navigation-item js-navigation-open "
               href="/ckan/ckan/blob/1384-related-list-503/ckan/config/routing.py"
               data-name="1384-related-list-503"
               data-skip-pjax="true"
               rel="nofollow">
              <svg aria-hidden="true" class="octicon octicon-check select-menu-item-icon" height="16" version="1.1" viewBox="0 0 12 16" width="12"><path fill-rule="evenodd" d="M12 5l-8 8-4-4 1.5-1.5L4 10l6.5-6.5z"/></svg>
              <span class="select-menu-item-text css-truncate-target js-select-menu-filter-text">
                1384-related-list-503
              </span>
            </a>
            <a class="select-menu-item js-navigation-item js-navigation-open "
               href="/ckan/ckan/blob/1387-fix-resource-urls/ckan/config/routing.py"
               data-name="1387-fix-resource-urls"
               data-skip-pjax="true"
               rel="nofollow">
              <svg aria-hidden="true" class="octicon octicon-check select-menu-item-icon" height="16" version="1.1" viewBox="0 0 12 16" width="12"><path fill-rule="evenodd" d="M12 5l-8 8-4-4 1.5-1.5L4 10l6.5-6.5z"/></svg>
              <span class="select-menu-item-text css-truncate-target js-select-menu-filter-text">
                1387-fix-resource-urls
              </span>
            </a>
            <a class="select-menu-item js-navigation-item js-navigation-open "
               href="/ckan/ckan/blob/1389-release-docs-tweaks-2/ckan/config/routing.py"
               data-name="1389-release-docs-tweaks-2"
               data-skip-pjax="true"
               rel="nofollow">
              <svg aria-hidden="true" class="octicon octicon-check select-menu-item-icon" height="16" version="1.1" viewBox="0 0 12 16" width="12"><path fill-rule="evenodd" d="M12 5l-8 8-4-4 1.5-1.5L4 10l6.5-6.5z"/></svg>
              <span class="select-menu-item-text css-truncate-target js-select-menu-filter-text">
                1389-release-docs-tweaks-2
              </span>
            </a>
            <a class="select-menu-item js-navigation-item js-navigation-open "
               href="/ckan/ckan/blob/1390-group_dictize-exception/ckan/config/routing.py"
               data-name="1390-group_dictize-exception"
               data-skip-pjax="true"
               rel="nofollow">
              <svg aria-hidden="true" class="octicon octicon-check select-menu-item-icon" height="16" version="1.1" viewBox="0 0 12 16" width="12"><path fill-rule="evenodd" d="M12 5l-8 8-4-4 1.5-1.5L4 10l6.5-6.5z"/></svg>
              <span class="select-menu-item-text css-truncate-target js-select-menu-filter-text">
                1390-group_dictize-exception
              </span>
            </a>
            <a class="select-menu-item js-navigation-item js-navigation-open "
               href="/ckan/ckan/blob/1392-group-member-add-template-fix/ckan/config/routing.py"
               data-name="1392-group-member-add-template-fix"
               data-skip-pjax="true"
               rel="nofollow">
              <svg aria-hidden="true" class="octicon octicon-check select-menu-item-icon" height="16" version="1.1" viewBox="0 0 12 16" width="12"><path fill-rule="evenodd" d="M12 5l-8 8-4-4 1.5-1.5L4 10l6.5-6.5z"/></svg>
              <span class="select-menu-item-text css-truncate-target js-select-menu-filter-text">
                1392-group-member-add-template-fix
              </span>
            </a>
            <a class="select-menu-item js-navigation-item js-navigation-open "
               href="/ckan/ckan/blob/1393-bug-user-create-returns-email-for-api-key/ckan/config/routing.py"
               data-name="1393-bug-user-create-returns-email-for-api-key"
               data-skip-pjax="true"
               rel="nofollow">
              <svg aria-hidden="true" class="octicon octicon-check select-menu-item-icon" height="16" version="1.1" viewBox="0 0 12 16" width="12"><path fill-rule="evenodd" d="M12 5l-8 8-4-4 1.5-1.5L4 10l6.5-6.5z"/></svg>
              <span class="select-menu-item-text css-truncate-target js-select-menu-filter-text">
                1393-bug-user-create-returns-email-for-api-key
              </span>
            </a>
            <a class="select-menu-item js-navigation-item js-navigation-open "
               href="/ckan/ckan/blob/1396-html-contributing-docs/ckan/config/routing.py"
               data-name="1396-html-contributing-docs"
               data-skip-pjax="true"
               rel="nofollow">
              <svg aria-hidden="true" class="octicon octicon-check select-menu-item-icon" height="16" version="1.1" viewBox="0 0 12 16" width="12"><path fill-rule="evenodd" d="M12 5l-8 8-4-4 1.5-1.5L4 10l6.5-6.5z"/></svg>
              <span class="select-menu-item-text css-truncate-target js-select-menu-filter-text">
                1396-html-contributing-docs
              </span>
            </a>
            <a class="select-menu-item js-navigation-item js-navigation-open "
               href="/ckan/ckan/blob/1398-info-overflow-word-break/ckan/config/routing.py"
               data-name="1398-info-overflow-word-break"
               data-skip-pjax="true"
               rel="nofollow">
              <svg aria-hidden="true" class="octicon octicon-check select-menu-item-icon" height="16" version="1.1" viewBox="0 0 12 16" width="12"><path fill-rule="evenodd" d="M12 5l-8 8-4-4 1.5-1.5L4 10l6.5-6.5z"/></svg>
              <span class="select-menu-item-text css-truncate-target js-select-menu-filter-text">
                1398-info-overflow-word-break
              </span>
            </a>
            <a class="select-menu-item js-navigation-item js-navigation-open "
               href="/ckan/ckan/blob/1407-resource-group-logic/ckan/config/routing.py"
               data-name="1407-resource-group-logic"
               data-skip-pjax="true"
               rel="nofollow">
              <svg aria-hidden="true" class="octicon octicon-check select-menu-item-icon" height="16" version="1.1" viewBox="0 0 12 16" width="12"><path fill-rule="evenodd" d="M12 5l-8 8-4-4 1.5-1.5L4 10l6.5-6.5z"/></svg>
              <span class="select-menu-item-text css-truncate-target js-select-menu-filter-text">
                1407-resource-group-logic
              </span>
            </a>
            <a class="select-menu-item js-navigation-item js-navigation-open "
               href="/ckan/ckan/blob/1418-junk-errors/ckan/config/routing.py"
               data-name="1418-junk-errors"
               data-skip-pjax="true"
               rel="nofollow">
              <svg aria-hidden="true" class="octicon octicon-check select-menu-item-icon" height="16" version="1.1" viewBox="0 0 12 16" width="12"><path fill-rule="evenodd" d="M12 5l-8 8-4-4 1.5-1.5L4 10l6.5-6.5z"/></svg>
              <span class="select-menu-item-text css-truncate-target js-select-menu-filter-text">
                1418-junk-errors
              </span>
            </a>
            <a class="select-menu-item js-navigation-item js-navigation-open "
               href="/ckan/ckan/blob/1422-repoze-key/ckan/config/routing.py"
               data-name="1422-repoze-key"
               data-skip-pjax="true"
               rel="nofollow">
              <svg aria-hidden="true" class="octicon octicon-check select-menu-item-icon" height="16" version="1.1" viewBox="0 0 12 16" width="12"><path fill-rule="evenodd" d="M12 5l-8 8-4-4 1.5-1.5L4 10l6.5-6.5z"/></svg>
              <span class="select-menu-item-text css-truncate-target js-select-menu-filter-text">
                1422-repoze-key
              </span>
            </a>
            <a class="select-menu-item js-navigation-item js-navigation-open "
               href="/ckan/ckan/blob/1425-exception-fix/ckan/config/routing.py"
               data-name="1425-exception-fix"
               data-skip-pjax="true"
               rel="nofollow">
              <svg aria-hidden="true" class="octicon octicon-check select-menu-item-icon" height="16" version="1.1" viewBox="0 0 12 16" width="12"><path fill-rule="evenodd" d="M12 5l-8 8-4-4 1.5-1.5L4 10l6.5-6.5z"/></svg>
              <span class="select-menu-item-text css-truncate-target js-select-menu-filter-text">
                1425-exception-fix
              </span>
            </a>
            <a class="select-menu-item js-navigation-item js-navigation-open "
               href="/ckan/ckan/blob/1433-fix-context/ckan/config/routing.py"
               data-name="1433-fix-context"
               data-skip-pjax="true"
               rel="nofollow">
              <svg aria-hidden="true" class="octicon octicon-check select-menu-item-icon" height="16" version="1.1" viewBox="0 0 12 16" width="12"><path fill-rule="evenodd" d="M12 5l-8 8-4-4 1.5-1.5L4 10l6.5-6.5z"/></svg>
              <span class="select-menu-item-text css-truncate-target js-select-menu-filter-text">
                1433-fix-context
              </span>
            </a>
            <a class="select-menu-item js-navigation-item js-navigation-open "
               href="/ckan/ckan/blob/1434-feature-add-i18n-strings-from-core-extensions/ckan/config/routing.py"
               data-name="1434-feature-add-i18n-strings-from-core-extensions"
               data-skip-pjax="true"
               rel="nofollow">
              <svg aria-hidden="true" class="octicon octicon-check select-menu-item-icon" height="16" version="1.1" viewBox="0 0 12 16" width="12"><path fill-rule="evenodd" d="M12 5l-8 8-4-4 1.5-1.5L4 10l6.5-6.5z"/></svg>
              <span class="select-menu-item-text css-truncate-target js-select-menu-filter-text">
                1434-feature-add-i18n-strings-from-core-extensions
              </span>
            </a>
            <a class="select-menu-item js-navigation-item js-navigation-open "
               href="/ckan/ckan/blob/1437-package-update/ckan/config/routing.py"
               data-name="1437-package-update"
               data-skip-pjax="true"
               rel="nofollow">
              <svg aria-hidden="true" class="octicon octicon-check select-menu-item-icon" height="16" version="1.1" viewBox="0 0 12 16" width="12"><path fill-rule="evenodd" d="M12 5l-8 8-4-4 1.5-1.5L4 10l6.5-6.5z"/></svg>
              <span class="select-menu-item-text css-truncate-target js-select-menu-filter-text">
                1437-package-update
              </span>
            </a>
            <a class="select-menu-item js-navigation-item js-navigation-open "
               href="/ckan/ckan/blob/1446-datapusher-integration-issues/ckan/config/routing.py"
               data-name="1446-datapusher-integration-issues"
               data-skip-pjax="true"
               rel="nofollow">
              <svg aria-hidden="true" class="octicon octicon-check select-menu-item-icon" height="16" version="1.1" viewBox="0 0 12 16" width="12"><path fill-rule="evenodd" d="M12 5l-8 8-4-4 1.5-1.5L4 10l6.5-6.5z"/></svg>
              <span class="select-menu-item-text css-truncate-target js-select-menu-filter-text">
                1446-datapusher-integration-issues
              </span>
            </a>
            <a class="select-menu-item js-navigation-item js-navigation-open "
               href="/ckan/ckan/blob/1449-cant-delete-extra/ckan/config/routing.py"
               data-name="1449-cant-delete-extra"
               data-skip-pjax="true"
               rel="nofollow">
              <svg aria-hidden="true" class="octicon octicon-check select-menu-item-icon" height="16" version="1.1" viewBox="0 0 12 16" width="12"><path fill-rule="evenodd" d="M12 5l-8 8-4-4 1.5-1.5L4 10l6.5-6.5z"/></svg>
              <span class="select-menu-item-text css-truncate-target js-select-menu-filter-text">
                1449-cant-delete-extra
              </span>
            </a>
            <a class="select-menu-item js-navigation-item js-navigation-open "
               href="/ckan/ckan/blob/1450-resource-reordering-production/ckan/config/routing.py"
               data-name="1450-resource-reordering-production"
               data-skip-pjax="true"
               rel="nofollow">
              <svg aria-hidden="true" class="octicon octicon-check select-menu-item-icon" height="16" version="1.1" viewBox="0 0 12 16" width="12"><path fill-rule="evenodd" d="M12 5l-8 8-4-4 1.5-1.5L4 10l6.5-6.5z"/></svg>
              <span class="select-menu-item-text css-truncate-target js-select-menu-filter-text">
                1450-resource-reordering-production
              </span>
            </a>
            <a class="select-menu-item js-navigation-item js-navigation-open "
               href="/ckan/ckan/blob/1451-use-site-url-for-datastore-callback/ckan/config/routing.py"
               data-name="1451-use-site-url-for-datastore-callback"
               data-skip-pjax="true"
               rel="nofollow">
              <svg aria-hidden="true" class="octicon octicon-check select-menu-item-icon" height="16" version="1.1" viewBox="0 0 12 16" width="12"><path fill-rule="evenodd" d="M12 5l-8 8-4-4 1.5-1.5L4 10l6.5-6.5z"/></svg>
              <span class="select-menu-item-text css-truncate-target js-select-menu-filter-text">
                1451-use-site-url-for-datastore-callback
              </span>
            </a>
            <a class="select-menu-item js-navigation-item js-navigation-open "
               href="/ckan/ckan/blob/1452-textpreview-tests/ckan/config/routing.py"
               data-name="1452-textpreview-tests"
               data-skip-pjax="true"
               rel="nofollow">
              <svg aria-hidden="true" class="octicon octicon-check select-menu-item-icon" height="16" version="1.1" viewBox="0 0 12 16" width="12"><path fill-rule="evenodd" d="M12 5l-8 8-4-4 1.5-1.5L4 10l6.5-6.5z"/></svg>
              <span class="select-menu-item-text css-truncate-target js-select-menu-filter-text">
                1452-textpreview-tests
              </span>
            </a>
            <a class="select-menu-item js-navigation-item js-navigation-open "
               href="/ckan/ckan/blob/1453-sysadmins-not-create-unown-datasets/ckan/config/routing.py"
               data-name="1453-sysadmins-not-create-unown-datasets"
               data-skip-pjax="true"
               rel="nofollow">
              <svg aria-hidden="true" class="octicon octicon-check select-menu-item-icon" height="16" version="1.1" viewBox="0 0 12 16" width="12"><path fill-rule="evenodd" d="M12 5l-8 8-4-4 1.5-1.5L4 10l6.5-6.5z"/></svg>
              <span class="select-menu-item-text css-truncate-target js-select-menu-filter-text">
                1453-sysadmins-not-create-unown-datasets
              </span>
            </a>
            <a class="select-menu-item js-navigation-item js-navigation-open "
               href="/ckan/ckan/blob/1454-member-editing-fixes/ckan/config/routing.py"
               data-name="1454-member-editing-fixes"
               data-skip-pjax="true"
               rel="nofollow">
              <svg aria-hidden="true" class="octicon octicon-check select-menu-item-icon" height="16" version="1.1" viewBox="0 0 12 16" width="12"><path fill-rule="evenodd" d="M12 5l-8 8-4-4 1.5-1.5L4 10l6.5-6.5z"/></svg>
              <span class="select-menu-item-text css-truncate-target js-select-menu-filter-text">
                1454-member-editing-fixes
              </span>
            </a>
            <a class="select-menu-item js-navigation-item js-navigation-open "
               href="/ckan/ckan/blob/1455-fix-bulk-editing/ckan/config/routing.py"
               data-name="1455-fix-bulk-editing"
               data-skip-pjax="true"
               rel="nofollow">
              <svg aria-hidden="true" class="octicon octicon-check select-menu-item-icon" height="16" version="1.1" viewBox="0 0 12 16" width="12"><path fill-rule="evenodd" d="M12 5l-8 8-4-4 1.5-1.5L4 10l6.5-6.5z"/></svg>
              <span class="select-menu-item-text css-truncate-target js-select-menu-filter-text">
                1455-fix-bulk-editing
              </span>
            </a>
            <a class="select-menu-item js-navigation-item js-navigation-open "
               href="/ckan/ckan/blob/1457-super-important-fix/ckan/config/routing.py"
               data-name="1457-super-important-fix"
               data-skip-pjax="true"
               rel="nofollow">
              <svg aria-hidden="true" class="octicon octicon-check select-menu-item-icon" height="16" version="1.1" viewBox="0 0 12 16" width="12"><path fill-rule="evenodd" d="M12 5l-8 8-4-4 1.5-1.5L4 10l6.5-6.5z"/></svg>
              <span class="select-menu-item-text css-truncate-target js-select-menu-filter-text">
                1457-super-important-fix
              </span>
            </a>
            <a class="select-menu-item js-navigation-item js-navigation-open "
               href="/ckan/ckan/blob/1460-fix-group-remove-ie7/ckan/config/routing.py"
               data-name="1460-fix-group-remove-ie7"
               data-skip-pjax="true"
               rel="nofollow">
              <svg aria-hidden="true" class="octicon octicon-check select-menu-item-icon" height="16" version="1.1" viewBox="0 0 12 16" width="12"><path fill-rule="evenodd" d="M12 5l-8 8-4-4 1.5-1.5L4 10l6.5-6.5z"/></svg>
              <span class="select-menu-item-text css-truncate-target js-select-menu-filter-text">
                1460-fix-group-remove-ie7
              </span>
            </a>
            <a class="select-menu-item js-navigation-item js-navigation-open "
               href="/ckan/ckan/blob/1461-repeated-code-in-package_search/ckan/config/routing.py"
               data-name="1461-repeated-code-in-package_search"
               data-skip-pjax="true"
               rel="nofollow">
              <svg aria-hidden="true" class="octicon octicon-check select-menu-item-icon" height="16" version="1.1" viewBox="0 0 12 16" width="12"><path fill-rule="evenodd" d="M12 5l-8 8-4-4 1.5-1.5L4 10l6.5-6.5z"/></svg>
              <span class="select-menu-item-text css-truncate-target js-select-menu-filter-text">
                1461-repeated-code-in-package_search
              </span>
            </a>
            <a class="select-menu-item js-navigation-item js-navigation-open "
               href="/ckan/ckan/blob/1463-add-organization-feeds/ckan/config/routing.py"
               data-name="1463-add-organization-feeds"
               data-skip-pjax="true"
               rel="nofollow">
              <svg aria-hidden="true" class="octicon octicon-check select-menu-item-icon" height="16" version="1.1" viewBox="0 0 12 16" width="12"><path fill-rule="evenodd" d="M12 5l-8 8-4-4 1.5-1.5L4 10l6.5-6.5z"/></svg>
              <span class="select-menu-item-text css-truncate-target js-select-menu-filter-text">
                1463-add-organization-feeds
              </span>
            </a>
            <a class="select-menu-item js-navigation-item js-navigation-open "
               href="/ckan/ckan/blob/1470-member-auth-test-fail/ckan/config/routing.py"
               data-name="1470-member-auth-test-fail"
               data-skip-pjax="true"
               rel="nofollow">
              <svg aria-hidden="true" class="octicon octicon-check select-menu-item-icon" height="16" version="1.1" viewBox="0 0 12 16" width="12"><path fill-rule="evenodd" d="M12 5l-8 8-4-4 1.5-1.5L4 10l6.5-6.5z"/></svg>
              <span class="select-menu-item-text css-truncate-target js-select-menu-filter-text">
                1470-member-auth-test-fail
              </span>
            </a>
            <a class="select-menu-item js-navigation-item js-navigation-open "
               href="/ckan/ckan/blob/1471-delete-unowned-datasets/ckan/config/routing.py"
               data-name="1471-delete-unowned-datasets"
               data-skip-pjax="true"
               rel="nofollow">
              <svg aria-hidden="true" class="octicon octicon-check select-menu-item-icon" height="16" version="1.1" viewBox="0 0 12 16" width="12"><path fill-rule="evenodd" d="M12 5l-8 8-4-4 1.5-1.5L4 10l6.5-6.5z"/></svg>
              <span class="select-menu-item-text css-truncate-target js-select-menu-filter-text">
                1471-delete-unowned-datasets
              </span>
            </a>
            <a class="select-menu-item js-navigation-item js-navigation-open "
               href="/ckan/ckan/blob/1473-create-unowned-dataset-when-org-member/ckan/config/routing.py"
               data-name="1473-create-unowned-dataset-when-org-member"
               data-skip-pjax="true"
               rel="nofollow">
              <svg aria-hidden="true" class="octicon octicon-check select-menu-item-icon" height="16" version="1.1" viewBox="0 0 12 16" width="12"><path fill-rule="evenodd" d="M12 5l-8 8-4-4 1.5-1.5L4 10l6.5-6.5z"/></svg>
              <span class="select-menu-item-text css-truncate-target js-select-menu-filter-text">
                1473-create-unowned-dataset-when-org-member
              </span>
            </a>
            <a class="select-menu-item js-navigation-item js-navigation-open "
               href="/ckan/ckan/blob/1474-fix-resource-schema/ckan/config/routing.py"
               data-name="1474-fix-resource-schema"
               data-skip-pjax="true"
               rel="nofollow">
              <svg aria-hidden="true" class="octicon octicon-check select-menu-item-icon" height="16" version="1.1" viewBox="0 0 12 16" width="12"><path fill-rule="evenodd" d="M12 5l-8 8-4-4 1.5-1.5L4 10l6.5-6.5z"/></svg>
              <span class="select-menu-item-text css-truncate-target js-select-menu-filter-text">
                1474-fix-resource-schema
              </span>
            </a>
            <a class="select-menu-item js-navigation-item js-navigation-open "
               href="/ckan/ckan/blob/1484-use-eq/ckan/config/routing.py"
               data-name="1484-use-eq"
               data-skip-pjax="true"
               rel="nofollow">
              <svg aria-hidden="true" class="octicon octicon-check select-menu-item-icon" height="16" version="1.1" viewBox="0 0 12 16" width="12"><path fill-rule="evenodd" d="M12 5l-8 8-4-4 1.5-1.5L4 10l6.5-6.5z"/></svg>
              <span class="select-menu-item-text css-truncate-target js-select-menu-filter-text">
                1484-use-eq
              </span>
            </a>
            <a class="select-menu-item js-navigation-item js-navigation-open "
               href="/ckan/ckan/blob/1487-error-datapusher_hook-auth/ckan/config/routing.py"
               data-name="1487-error-datapusher_hook-auth"
               data-skip-pjax="true"
               rel="nofollow">
              <svg aria-hidden="true" class="octicon octicon-check select-menu-item-icon" height="16" version="1.1" viewBox="0 0 12 16" width="12"><path fill-rule="evenodd" d="M12 5l-8 8-4-4 1.5-1.5L4 10l6.5-6.5z"/></svg>
              <span class="select-menu-item-text css-truncate-target js-select-menu-filter-text">
                1487-error-datapusher_hook-auth
              </span>
            </a>
            <a class="select-menu-item js-navigation-item js-navigation-open "
               href="/ckan/ckan/blob/1488-more-robust-get-object-in-auth/ckan/config/routing.py"
               data-name="1488-more-robust-get-object-in-auth"
               data-skip-pjax="true"
               rel="nofollow">
              <svg aria-hidden="true" class="octicon octicon-check select-menu-item-icon" height="16" version="1.1" viewBox="0 0 12 16" width="12"><path fill-rule="evenodd" d="M12 5l-8 8-4-4 1.5-1.5L4 10l6.5-6.5z"/></svg>
              <span class="select-menu-item-text css-truncate-target js-select-menu-filter-text">
                1488-more-robust-get-object-in-auth
              </span>
            </a>
            <a class="select-menu-item js-navigation-item js-navigation-open "
               href="/ckan/ckan/blob/1490-datapusher_hook-callback-url/ckan/config/routing.py"
               data-name="1490-datapusher_hook-callback-url"
               data-skip-pjax="true"
               rel="nofollow">
              <svg aria-hidden="true" class="octicon octicon-check select-menu-item-icon" height="16" version="1.1" viewBox="0 0 12 16" width="12"><path fill-rule="evenodd" d="M12 5l-8 8-4-4 1.5-1.5L4 10l6.5-6.5z"/></svg>
              <span class="select-menu-item-text css-truncate-target js-select-menu-filter-text">
                1490-datapusher_hook-callback-url
              </span>
            </a>
            <a class="select-menu-item js-navigation-item js-navigation-open "
               href="/ckan/ckan/blob/1491-wrong-breadcrumbs/ckan/config/routing.py"
               data-name="1491-wrong-breadcrumbs"
               data-skip-pjax="true"
               rel="nofollow">
              <svg aria-hidden="true" class="octicon octicon-check select-menu-item-icon" height="16" version="1.1" viewBox="0 0 12 16" width="12"><path fill-rule="evenodd" d="M12 5l-8 8-4-4 1.5-1.5L4 10l6.5-6.5z"/></svg>
              <span class="select-menu-item-text css-truncate-target js-select-menu-filter-text">
                1491-wrong-breadcrumbs
              </span>
            </a>
            <a class="select-menu-item js-navigation-item js-navigation-open "
               href="/ckan/ckan/blob/1500-mock-web-request-on-paster-commands/ckan/config/routing.py"
               data-name="1500-mock-web-request-on-paster-commands"
               data-skip-pjax="true"
               rel="nofollow">
              <svg aria-hidden="true" class="octicon octicon-check select-menu-item-icon" height="16" version="1.1" viewBox="0 0 12 16" width="12"><path fill-rule="evenodd" d="M12 5l-8 8-4-4 1.5-1.5L4 10l6.5-6.5z"/></svg>
              <span class="select-menu-item-text css-truncate-target js-select-menu-filter-text">
                1500-mock-web-request-on-paster-commands
              </span>
            </a>
            <a class="select-menu-item js-navigation-item js-navigation-open "
               href="/ckan/ckan/blob/1503-two-licenses/ckan/config/routing.py"
               data-name="1503-two-licenses"
               data-skip-pjax="true"
               rel="nofollow">
              <svg aria-hidden="true" class="octicon octicon-check select-menu-item-icon" height="16" version="1.1" viewBox="0 0 12 16" width="12"><path fill-rule="evenodd" d="M12 5l-8 8-4-4 1.5-1.5L4 10l6.5-6.5z"/></svg>
              <span class="select-menu-item-text css-truncate-target js-select-menu-filter-text">
                1503-two-licenses
              </span>
            </a>
            <a class="select-menu-item js-navigation-item js-navigation-open "
               href="/ckan/ckan/blob/1507-current-package-list/ckan/config/routing.py"
               data-name="1507-current-package-list"
               data-skip-pjax="true"
               rel="nofollow">
              <svg aria-hidden="true" class="octicon octicon-check select-menu-item-icon" height="16" version="1.1" viewBox="0 0 12 16" width="12"><path fill-rule="evenodd" d="M12 5l-8 8-4-4 1.5-1.5L4 10l6.5-6.5z"/></svg>
              <span class="select-menu-item-text css-truncate-target js-select-menu-filter-text">
                1507-current-package-list
              </span>
            </a>
            <a class="select-menu-item js-navigation-item js-navigation-open "
               href="/ckan/ckan/blob/1508-oversized-forgot-password-button/ckan/config/routing.py"
               data-name="1508-oversized-forgot-password-button"
               data-skip-pjax="true"
               rel="nofollow">
              <svg aria-hidden="true" class="octicon octicon-check select-menu-item-icon" height="16" version="1.1" viewBox="0 0 12 16" width="12"><path fill-rule="evenodd" d="M12 5l-8 8-4-4 1.5-1.5L4 10l6.5-6.5z"/></svg>
              <span class="select-menu-item-text css-truncate-target js-select-menu-filter-text">
                1508-oversized-forgot-password-button
              </span>
            </a>
            <a class="select-menu-item js-navigation-item js-navigation-open "
               href="/ckan/ckan/blob/1512-defect-rename-user/ckan/config/routing.py"
               data-name="1512-defect-rename-user"
               data-skip-pjax="true"
               rel="nofollow">
              <svg aria-hidden="true" class="octicon octicon-check select-menu-item-icon" height="16" version="1.1" viewBox="0 0 12 16" width="12"><path fill-rule="evenodd" d="M12 5l-8 8-4-4 1.5-1.5L4 10l6.5-6.5z"/></svg>
              <span class="select-menu-item-text css-truncate-target js-select-menu-filter-text">
                1512-defect-rename-user
              </span>
            </a>
            <a class="select-menu-item js-navigation-item js-navigation-open "
               href="/ckan/ckan/blob/1517-size-mimetype/ckan/config/routing.py"
               data-name="1517-size-mimetype"
               data-skip-pjax="true"
               rel="nofollow">
              <svg aria-hidden="true" class="octicon octicon-check select-menu-item-icon" height="16" version="1.1" viewBox="0 0 12 16" width="12"><path fill-rule="evenodd" d="M12 5l-8 8-4-4 1.5-1.5L4 10l6.5-6.5z"/></svg>
              <span class="select-menu-item-text css-truncate-target js-select-menu-filter-text">
                1517-size-mimetype
              </span>
            </a>
            <a class="select-menu-item js-navigation-item js-navigation-open "
               href="/ckan/ckan/blob/1527-custom-emails-fix-tests/ckan/config/routing.py"
               data-name="1527-custom-emails-fix-tests"
               data-skip-pjax="true"
               rel="nofollow">
              <svg aria-hidden="true" class="octicon octicon-check select-menu-item-icon" height="16" version="1.1" viewBox="0 0 12 16" width="12"><path fill-rule="evenodd" d="M12 5l-8 8-4-4 1.5-1.5L4 10l6.5-6.5z"/></svg>
              <span class="select-menu-item-text css-truncate-target js-select-menu-filter-text">
                1527-custom-emails-fix-tests
              </span>
            </a>
            <a class="select-menu-item js-navigation-item js-navigation-open "
               href="/ckan/ckan/blob/1527-custom-emails/ckan/config/routing.py"
               data-name="1527-custom-emails"
               data-skip-pjax="true"
               rel="nofollow">
              <svg aria-hidden="true" class="octicon octicon-check select-menu-item-icon" height="16" version="1.1" viewBox="0 0 12 16" width="12"><path fill-rule="evenodd" d="M12 5l-8 8-4-4 1.5-1.5L4 10l6.5-6.5z"/></svg>
              <span class="select-menu-item-text css-truncate-target js-select-menu-filter-text">
                1527-custom-emails
              </span>
            </a>
            <a class="select-menu-item js-navigation-item js-navigation-open "
               href="/ckan/ckan/blob/1527-fix-failures/ckan/config/routing.py"
               data-name="1527-fix-failures"
               data-skip-pjax="true"
               rel="nofollow">
              <svg aria-hidden="true" class="octicon octicon-check select-menu-item-icon" height="16" version="1.1" viewBox="0 0 12 16" width="12"><path fill-rule="evenodd" d="M12 5l-8 8-4-4 1.5-1.5L4 10l6.5-6.5z"/></svg>
              <span class="select-menu-item-text css-truncate-target js-select-menu-filter-text">
                1527-fix-failures
              </span>
            </a>
            <a class="select-menu-item js-navigation-item js-navigation-open "
               href="/ckan/ckan/blob/1530-use-passlib/ckan/config/routing.py"
               data-name="1530-use-passlib"
               data-skip-pjax="true"
               rel="nofollow">
              <svg aria-hidden="true" class="octicon octicon-check select-menu-item-icon" height="16" version="1.1" viewBox="0 0 12 16" width="12"><path fill-rule="evenodd" d="M12 5l-8 8-4-4 1.5-1.5L4 10l6.5-6.5z"/></svg>
              <span class="select-menu-item-text css-truncate-target js-select-menu-filter-text">
                1530-use-passlib
              </span>
            </a>
            <a class="select-menu-item js-navigation-item js-navigation-open "
               href="/ckan/ckan/blob/1534-mimetype-fix/ckan/config/routing.py"
               data-name="1534-mimetype-fix"
               data-skip-pjax="true"
               rel="nofollow">
              <svg aria-hidden="true" class="octicon octicon-check select-menu-item-icon" height="16" version="1.1" viewBox="0 0 12 16" width="12"><path fill-rule="evenodd" d="M12 5l-8 8-4-4 1.5-1.5L4 10l6.5-6.5z"/></svg>
              <span class="select-menu-item-text css-truncate-target js-select-menu-filter-text">
                1534-mimetype-fix
              </span>
            </a>
            <a class="select-menu-item js-navigation-item js-navigation-open "
               href="/ckan/ckan/blob/1539-clean-trash/ckan/config/routing.py"
               data-name="1539-clean-trash"
               data-skip-pjax="true"
               rel="nofollow">
              <svg aria-hidden="true" class="octicon octicon-check select-menu-item-icon" height="16" version="1.1" viewBox="0 0 12 16" width="12"><path fill-rule="evenodd" d="M12 5l-8 8-4-4 1.5-1.5L4 10l6.5-6.5z"/></svg>
              <span class="select-menu-item-text css-truncate-target js-select-menu-filter-text">
                1539-clean-trash
              </span>
            </a>
            <a class="select-menu-item js-navigation-item js-navigation-open "
               href="/ckan/ckan/blob/1540-fix-logo-alt-text/ckan/config/routing.py"
               data-name="1540-fix-logo-alt-text"
               data-skip-pjax="true"
               rel="nofollow">
              <svg aria-hidden="true" class="octicon octicon-check select-menu-item-icon" height="16" version="1.1" viewBox="0 0 12 16" width="12"><path fill-rule="evenodd" d="M12 5l-8 8-4-4 1.5-1.5L4 10l6.5-6.5z"/></svg>
              <span class="select-menu-item-text css-truncate-target js-select-menu-filter-text">
                1540-fix-logo-alt-text
              </span>
            </a>
            <a class="select-menu-item js-navigation-item js-navigation-open "
               href="/ckan/ckan/blob/1541-gravatar-alt-tag/ckan/config/routing.py"
               data-name="1541-gravatar-alt-tag"
               data-skip-pjax="true"
               rel="nofollow">
              <svg aria-hidden="true" class="octicon octicon-check select-menu-item-icon" height="16" version="1.1" viewBox="0 0 12 16" width="12"><path fill-rule="evenodd" d="M12 5l-8 8-4-4 1.5-1.5L4 10l6.5-6.5z"/></svg>
              <span class="select-menu-item-text css-truncate-target js-select-menu-filter-text">
                1541-gravatar-alt-tag
              </span>
            </a>
            <a class="select-menu-item js-navigation-item js-navigation-open "
               href="/ckan/ckan/blob/1546-fix-sysadmin-text/ckan/config/routing.py"
               data-name="1546-fix-sysadmin-text"
               data-skip-pjax="true"
               rel="nofollow">
              <svg aria-hidden="true" class="octicon octicon-check select-menu-item-icon" height="16" version="1.1" viewBox="0 0 12 16" width="12"><path fill-rule="evenodd" d="M12 5l-8 8-4-4 1.5-1.5L4 10l6.5-6.5z"/></svg>
              <span class="select-menu-item-text css-truncate-target js-select-menu-filter-text">
                1546-fix-sysadmin-text
              </span>
            </a>
            <a class="select-menu-item js-navigation-item js-navigation-open "
               href="/ckan/ckan/blob/1557-deprecate-group_package_show/ckan/config/routing.py"
               data-name="1557-deprecate-group_package_show"
               data-skip-pjax="true"
               rel="nofollow">
              <svg aria-hidden="true" class="octicon octicon-check select-menu-item-icon" height="16" version="1.1" viewBox="0 0 12 16" width="12"><path fill-rule="evenodd" d="M12 5l-8 8-4-4 1.5-1.5L4 10l6.5-6.5z"/></svg>
              <span class="select-menu-item-text css-truncate-target js-select-menu-filter-text">
                1557-deprecate-group_package_show
              </span>
            </a>
            <a class="select-menu-item js-navigation-item js-navigation-open "
               href="/ckan/ckan/blob/1564-simple-code-contributions/ckan/config/routing.py"
               data-name="1564-simple-code-contributions"
               data-skip-pjax="true"
               rel="nofollow">
              <svg aria-hidden="true" class="octicon octicon-check select-menu-item-icon" height="16" version="1.1" viewBox="0 0 12 16" width="12"><path fill-rule="evenodd" d="M12 5l-8 8-4-4 1.5-1.5L4 10l6.5-6.5z"/></svg>
              <span class="select-menu-item-text css-truncate-target js-select-menu-filter-text">
                1564-simple-code-contributions
              </span>
            </a>
            <a class="select-menu-item js-navigation-item js-navigation-open "
               href="/ckan/ckan/blob/1572-dataset-purge/ckan/config/routing.py"
               data-name="1572-dataset-purge"
               data-skip-pjax="true"
               rel="nofollow">
              <svg aria-hidden="true" class="octicon octicon-check select-menu-item-icon" height="16" version="1.1" viewBox="0 0 12 16" width="12"><path fill-rule="evenodd" d="M12 5l-8 8-4-4 1.5-1.5L4 10l6.5-6.5z"/></svg>
              <span class="select-menu-item-text css-truncate-target js-select-menu-filter-text">
                1572-dataset-purge
              </span>
            </a>
            <a class="select-menu-item js-navigation-item js-navigation-open "
               href="/ckan/ckan/blob/1576-api-link/ckan/config/routing.py"
               data-name="1576-api-link"
               data-skip-pjax="true"
               rel="nofollow">
              <svg aria-hidden="true" class="octicon octicon-check select-menu-item-icon" height="16" version="1.1" viewBox="0 0 12 16" width="12"><path fill-rule="evenodd" d="M12 5l-8 8-4-4 1.5-1.5L4 10l6.5-6.5z"/></svg>
              <span class="select-menu-item-text css-truncate-target js-select-menu-filter-text">
                1576-api-link
              </span>
            </a>
            <a class="select-menu-item js-navigation-item js-navigation-open "
               href="/ckan/ckan/blob/1584-dont-lowercase-names-of-uploaded-files/ckan/config/routing.py"
               data-name="1584-dont-lowercase-names-of-uploaded-files"
               data-skip-pjax="true"
               rel="nofollow">
              <svg aria-hidden="true" class="octicon octicon-check select-menu-item-icon" height="16" version="1.1" viewBox="0 0 12 16" width="12"><path fill-rule="evenodd" d="M12 5l-8 8-4-4 1.5-1.5L4 10l6.5-6.5z"/></svg>
              <span class="select-menu-item-text css-truncate-target js-select-menu-filter-text">
                1584-dont-lowercase-names-of-uploaded-files
              </span>
            </a>
            <a class="select-menu-item js-navigation-item js-navigation-open "
               href="/ckan/ckan/blob/1594-package-group/ckan/config/routing.py"
               data-name="1594-package-group"
               data-skip-pjax="true"
               rel="nofollow">
              <svg aria-hidden="true" class="octicon octicon-check select-menu-item-icon" height="16" version="1.1" viewBox="0 0 12 16" width="12"><path fill-rule="evenodd" d="M12 5l-8 8-4-4 1.5-1.5L4 10l6.5-6.5z"/></svg>
              <span class="select-menu-item-text css-truncate-target js-select-menu-filter-text">
                1594-package-group
              </span>
            </a>
            <a class="select-menu-item js-navigation-item js-navigation-open "
               href="/ckan/ckan/blob/1596-dont-show-deleted-members/ckan/config/routing.py"
               data-name="1596-dont-show-deleted-members"
               data-skip-pjax="true"
               rel="nofollow">
              <svg aria-hidden="true" class="octicon octicon-check select-menu-item-icon" height="16" version="1.1" viewBox="0 0 12 16" width="12"><path fill-rule="evenodd" d="M12 5l-8 8-4-4 1.5-1.5L4 10l6.5-6.5z"/></svg>
              <span class="select-menu-item-text css-truncate-target js-select-menu-filter-text">
                1596-dont-show-deleted-members
              </span>
            </a>
            <a class="select-menu-item js-navigation-item js-navigation-open "
               href="/ckan/ckan/blob/1597-config-from-envvar/ckan/config/routing.py"
               data-name="1597-config-from-envvar"
               data-skip-pjax="true"
               rel="nofollow">
              <svg aria-hidden="true" class="octicon octicon-check select-menu-item-icon" height="16" version="1.1" viewBox="0 0 12 16" width="12"><path fill-rule="evenodd" d="M12 5l-8 8-4-4 1.5-1.5L4 10l6.5-6.5z"/></svg>
              <span class="select-menu-item-text css-truncate-target js-select-menu-filter-text">
                1597-config-from-envvar
              </span>
            </a>
            <a class="select-menu-item js-navigation-item js-navigation-open "
               href="/ckan/ckan/blob/1601-defect-organizations-server-error/ckan/config/routing.py"
               data-name="1601-defect-organizations-server-error"
               data-skip-pjax="true"
               rel="nofollow">
              <svg aria-hidden="true" class="octicon octicon-check select-menu-item-icon" height="16" version="1.1" viewBox="0 0 12 16" width="12"><path fill-rule="evenodd" d="M12 5l-8 8-4-4 1.5-1.5L4 10l6.5-6.5z"/></svg>
              <span class="select-menu-item-text css-truncate-target js-select-menu-filter-text">
                1601-defect-organizations-server-error
              </span>
            </a>
            <a class="select-menu-item js-navigation-item js-navigation-open "
               href="/ckan/ckan/blob/1622-oops-moved/ckan/config/routing.py"
               data-name="1622-oops-moved"
               data-skip-pjax="true"
               rel="nofollow">
              <svg aria-hidden="true" class="octicon octicon-check select-menu-item-icon" height="16" version="1.1" viewBox="0 0 12 16" width="12"><path fill-rule="evenodd" d="M12 5l-8 8-4-4 1.5-1.5L4 10l6.5-6.5z"/></svg>
              <span class="select-menu-item-text css-truncate-target js-select-menu-filter-text">
                1622-oops-moved
              </span>
            </a>
            <a class="select-menu-item js-navigation-item js-navigation-open "
               href="/ckan/ckan/blob/1625-remove-clean-action-name/ckan/config/routing.py"
               data-name="1625-remove-clean-action-name"
               data-skip-pjax="true"
               rel="nofollow">
              <svg aria-hidden="true" class="octicon octicon-check select-menu-item-icon" height="16" version="1.1" viewBox="0 0 12 16" width="12"><path fill-rule="evenodd" d="M12 5l-8 8-4-4 1.5-1.5L4 10l6.5-6.5z"/></svg>
              <span class="select-menu-item-text css-truncate-target js-select-menu-filter-text">
                1625-remove-clean-action-name
              </span>
            </a>
            <a class="select-menu-item js-navigation-item js-navigation-open "
               href="/ckan/ckan/blob/1635-feature-email-notifications-for-activity-streams/ckan/config/routing.py"
               data-name="1635-feature-email-notifications-for-activity-streams"
               data-skip-pjax="true"
               rel="nofollow">
              <svg aria-hidden="true" class="octicon octicon-check select-menu-item-icon" height="16" version="1.1" viewBox="0 0 12 16" width="12"><path fill-rule="evenodd" d="M12 5l-8 8-4-4 1.5-1.5L4 10l6.5-6.5z"/></svg>
              <span class="select-menu-item-text css-truncate-target js-select-menu-filter-text">
                1635-feature-email-notifications-for-activity-streams
              </span>
            </a>
            <a class="select-menu-item js-navigation-item js-navigation-open "
               href="/ckan/ckan/blob/1651-damn-travis/ckan/config/routing.py"
               data-name="1651-damn-travis"
               data-skip-pjax="true"
               rel="nofollow">
              <svg aria-hidden="true" class="octicon octicon-check select-menu-item-icon" height="16" version="1.1" viewBox="0 0 12 16" width="12"><path fill-rule="evenodd" d="M12 5l-8 8-4-4 1.5-1.5L4 10l6.5-6.5z"/></svg>
              <span class="select-menu-item-text css-truncate-target js-select-menu-filter-text">
                1651-damn-travis
              </span>
            </a>
            <a class="select-menu-item js-navigation-item js-navigation-open "
               href="/ckan/ckan/blob/1651-ubuntu-14.04/ckan/config/routing.py"
               data-name="1651-ubuntu-14.04"
               data-skip-pjax="true"
               rel="nofollow">
              <svg aria-hidden="true" class="octicon octicon-check select-menu-item-icon" height="16" version="1.1" viewBox="0 0 12 16" width="12"><path fill-rule="evenodd" d="M12 5l-8 8-4-4 1.5-1.5L4 10l6.5-6.5z"/></svg>
              <span class="select-menu-item-text css-truncate-target js-select-menu-filter-text">
                1651-ubuntu-14.04
              </span>
            </a>
            <a class="select-menu-item js-navigation-item js-navigation-open "
               href="/ckan/ckan/blob/1653-fix-paster-db-clean/ckan/config/routing.py"
               data-name="1653-fix-paster-db-clean"
               data-skip-pjax="true"
               rel="nofollow">
              <svg aria-hidden="true" class="octicon octicon-check select-menu-item-icon" height="16" version="1.1" viewBox="0 0 12 16" width="12"><path fill-rule="evenodd" d="M12 5l-8 8-4-4 1.5-1.5L4 10l6.5-6.5z"/></svg>
              <span class="select-menu-item-text css-truncate-target js-select-menu-filter-text">
                1653-fix-paster-db-clean
              </span>
            </a>
            <a class="select-menu-item js-navigation-item js-navigation-open "
               href="/ckan/ckan/blob/1657-email-hashes/ckan/config/routing.py"
               data-name="1657-email-hashes"
               data-skip-pjax="true"
               rel="nofollow">
              <svg aria-hidden="true" class="octicon octicon-check select-menu-item-icon" height="16" version="1.1" viewBox="0 0 12 16" width="12"><path fill-rule="evenodd" d="M12 5l-8 8-4-4 1.5-1.5L4 10l6.5-6.5z"/></svg>
              <span class="select-menu-item-text css-truncate-target js-select-menu-filter-text">
                1657-email-hashes
              </span>
            </a>
            <a class="select-menu-item js-navigation-item js-navigation-open "
               href="/ckan/ckan/blob/1665-group-auth-for-any-logged-in-user/ckan/config/routing.py"
               data-name="1665-group-auth-for-any-logged-in-user"
               data-skip-pjax="true"
               rel="nofollow">
              <svg aria-hidden="true" class="octicon octicon-check select-menu-item-icon" height="16" version="1.1" viewBox="0 0 12 16" width="12"><path fill-rule="evenodd" d="M12 5l-8 8-4-4 1.5-1.5L4 10l6.5-6.5z"/></svg>
              <span class="select-menu-item-text css-truncate-target js-select-menu-filter-text">
                1665-group-auth-for-any-logged-in-user
              </span>
            </a>
            <a class="select-menu-item js-navigation-item js-navigation-open "
               href="/ckan/ckan/blob/1668-deleted-users/ckan/config/routing.py"
               data-name="1668-deleted-users"
               data-skip-pjax="true"
               rel="nofollow">
              <svg aria-hidden="true" class="octicon octicon-check select-menu-item-icon" height="16" version="1.1" viewBox="0 0 12 16" width="12"><path fill-rule="evenodd" d="M12 5l-8 8-4-4 1.5-1.5L4 10l6.5-6.5z"/></svg>
              <span class="select-menu-item-text css-truncate-target js-select-menu-filter-text">
                1668-deleted-users
              </span>
            </a>
            <a class="select-menu-item js-navigation-item js-navigation-open "
               href="/ckan/ckan/blob/1669-rewrite-resource-create-tests/ckan/config/routing.py"
               data-name="1669-rewrite-resource-create-tests"
               data-skip-pjax="true"
               rel="nofollow">
              <svg aria-hidden="true" class="octicon octicon-check select-menu-item-icon" height="16" version="1.1" viewBox="0 0 12 16" width="12"><path fill-rule="evenodd" d="M12 5l-8 8-4-4 1.5-1.5L4 10l6.5-6.5z"/></svg>
              <span class="select-menu-item-text css-truncate-target js-select-menu-filter-text">
                1669-rewrite-resource-create-tests
              </span>
            </a>
            <a class="select-menu-item js-navigation-item js-navigation-open "
               href="/ckan/ckan/blob/1672-test-guidance-tweak/ckan/config/routing.py"
               data-name="1672-test-guidance-tweak"
               data-skip-pjax="true"
               rel="nofollow">
              <svg aria-hidden="true" class="octicon octicon-check select-menu-item-icon" height="16" version="1.1" viewBox="0 0 12 16" width="12"><path fill-rule="evenodd" d="M12 5l-8 8-4-4 1.5-1.5L4 10l6.5-6.5z"/></svg>
              <span class="select-menu-item-text css-truncate-target js-select-menu-filter-text">
                1672-test-guidance-tweak
              </span>
            </a>
            <a class="select-menu-item js-navigation-item js-navigation-open "
               href="/ckan/ckan/blob/1673-not-all-test-methods-need-docstrings/ckan/config/routing.py"
               data-name="1673-not-all-test-methods-need-docstrings"
               data-skip-pjax="true"
               rel="nofollow">
              <svg aria-hidden="true" class="octicon octicon-check select-menu-item-icon" height="16" version="1.1" viewBox="0 0 12 16" width="12"><path fill-rule="evenodd" d="M12 5l-8 8-4-4 1.5-1.5L4 10l6.5-6.5z"/></svg>
              <span class="select-menu-item-text css-truncate-target js-select-menu-filter-text">
                1673-not-all-test-methods-need-docstrings
              </span>
            </a>
            <a class="select-menu-item js-navigation-item js-navigation-open "
               href="/ckan/ckan/blob/1678-sync-search-by-default/ckan/config/routing.py"
               data-name="1678-sync-search-by-default"
               data-skip-pjax="true"
               rel="nofollow">
              <svg aria-hidden="true" class="octicon octicon-check select-menu-item-icon" height="16" version="1.1" viewBox="0 0 12 16" width="12"><path fill-rule="evenodd" d="M12 5l-8 8-4-4 1.5-1.5L4 10l6.5-6.5z"/></svg>
              <span class="select-menu-item-text css-truncate-target js-select-menu-filter-text">
                1678-sync-search-by-default
              </span>
            </a>
            <a class="select-menu-item js-navigation-item js-navigation-open "
               href="/ckan/ckan/blob/1696-groups-membership/ckan/config/routing.py"
               data-name="1696-groups-membership"
               data-skip-pjax="true"
               rel="nofollow">
              <svg aria-hidden="true" class="octicon octicon-check select-menu-item-icon" height="16" version="1.1" viewBox="0 0 12 16" width="12"><path fill-rule="evenodd" d="M12 5l-8 8-4-4 1.5-1.5L4 10l6.5-6.5z"/></svg>
              <span class="select-menu-item-text css-truncate-target js-select-menu-filter-text">
                1696-groups-membership
              </span>
            </a>
            <a class="select-menu-item js-navigation-item js-navigation-open "
               href="/ckan/ckan/blob/1701-date-field-index/ckan/config/routing.py"
               data-name="1701-date-field-index"
               data-skip-pjax="true"
               rel="nofollow">
              <svg aria-hidden="true" class="octicon octicon-check select-menu-item-icon" height="16" version="1.1" viewBox="0 0 12 16" width="12"><path fill-rule="evenodd" d="M12 5l-8 8-4-4 1.5-1.5L4 10l6.5-6.5z"/></svg>
              <span class="select-menu-item-text css-truncate-target js-select-menu-filter-text">
                1701-date-field-index
              </span>
            </a>
            <a class="select-menu-item js-navigation-item js-navigation-open "
               href="/ckan/ckan/blob/1707-404-resource-2/ckan/config/routing.py"
               data-name="1707-404-resource-2"
               data-skip-pjax="true"
               rel="nofollow">
              <svg aria-hidden="true" class="octicon octicon-check select-menu-item-icon" height="16" version="1.1" viewBox="0 0 12 16" width="12"><path fill-rule="evenodd" d="M12 5l-8 8-4-4 1.5-1.5L4 10l6.5-6.5z"/></svg>
              <span class="select-menu-item-text css-truncate-target js-select-menu-filter-text">
                1707-404-resource-2
              </span>
            </a>
            <a class="select-menu-item js-navigation-item js-navigation-open "
               href="/ckan/ckan/blob/1707-404-resource/ckan/config/routing.py"
               data-name="1707-404-resource"
               data-skip-pjax="true"
               rel="nofollow">
              <svg aria-hidden="true" class="octicon octicon-check select-menu-item-icon" height="16" version="1.1" viewBox="0 0 12 16" width="12"><path fill-rule="evenodd" d="M12 5l-8 8-4-4 1.5-1.5L4 10l6.5-6.5z"/></svg>
              <span class="select-menu-item-text css-truncate-target js-select-menu-filter-text">
                1707-404-resource
              </span>
            </a>
            <a class="select-menu-item js-navigation-item js-navigation-open "
               href="/ckan/ckan/blob/1707-test-failures/ckan/config/routing.py"
               data-name="1707-test-failures"
               data-skip-pjax="true"
               rel="nofollow">
              <svg aria-hidden="true" class="octicon octicon-check select-menu-item-icon" height="16" version="1.1" viewBox="0 0 12 16" width="12"><path fill-rule="evenodd" d="M12 5l-8 8-4-4 1.5-1.5L4 10l6.5-6.5z"/></svg>
              <span class="select-menu-item-text css-truncate-target js-select-menu-filter-text">
                1707-test-failures
              </span>
            </a>
            <a class="select-menu-item js-navigation-item js-navigation-open "
               href="/ckan/ckan/blob/1718-resource_search_returns_private_resources/ckan/config/routing.py"
               data-name="1718-resource_search_returns_private_resources"
               data-skip-pjax="true"
               rel="nofollow">
              <svg aria-hidden="true" class="octicon octicon-check select-menu-item-icon" height="16" version="1.1" viewBox="0 0 12 16" width="12"><path fill-rule="evenodd" d="M12 5l-8 8-4-4 1.5-1.5L4 10l6.5-6.5z"/></svg>
              <span class="select-menu-item-text css-truncate-target js-select-menu-filter-text">
                1718-resource_search_returns_private_resources
              </span>
            </a>
            <a class="select-menu-item js-navigation-item js-navigation-open "
               href="/ckan/ckan/blob/1723-wrong-fields-in-member-edit/ckan/config/routing.py"
               data-name="1723-wrong-fields-in-member-edit"
               data-skip-pjax="true"
               rel="nofollow">
              <svg aria-hidden="true" class="octicon octicon-check select-menu-item-icon" height="16" version="1.1" viewBox="0 0 12 16" width="12"><path fill-rule="evenodd" d="M12 5l-8 8-4-4 1.5-1.5L4 10l6.5-6.5z"/></svg>
              <span class="select-menu-item-text css-truncate-target js-select-menu-filter-text">
                1723-wrong-fields-in-member-edit
              </span>
            </a>
            <a class="select-menu-item js-navigation-item js-navigation-open "
               href="/ckan/ckan/blob/1736-test-factories-should-not-user-site-user/ckan/config/routing.py"
               data-name="1736-test-factories-should-not-user-site-user"
               data-skip-pjax="true"
               rel="nofollow">
              <svg aria-hidden="true" class="octicon octicon-check select-menu-item-icon" height="16" version="1.1" viewBox="0 0 12 16" width="12"><path fill-rule="evenodd" d="M12 5l-8 8-4-4 1.5-1.5L4 10l6.5-6.5z"/></svg>
              <span class="select-menu-item-text css-truncate-target js-select-menu-filter-text">
                1736-test-factories-should-not-user-site-user
              </span>
            </a>
            <a class="select-menu-item js-navigation-item js-navigation-open "
               href="/ckan/ckan/blob/1763-update-datastore-docs/ckan/config/routing.py"
               data-name="1763-update-datastore-docs"
               data-skip-pjax="true"
               rel="nofollow">
              <svg aria-hidden="true" class="octicon octicon-check select-menu-item-icon" height="16" version="1.1" viewBox="0 0 12 16" width="12"><path fill-rule="evenodd" d="M12 5l-8 8-4-4 1.5-1.5L4 10l6.5-6.5z"/></svg>
              <span class="select-menu-item-text css-truncate-target js-select-menu-filter-text">
                1763-update-datastore-docs
              </span>
            </a>
            <a class="select-menu-item js-navigation-item js-navigation-open "
               href="/ckan/ckan/blob/1768-organization-list/ckan/config/routing.py"
               data-name="1768-organization-list"
               data-skip-pjax="true"
               rel="nofollow">
              <svg aria-hidden="true" class="octicon octicon-check select-menu-item-icon" height="16" version="1.1" viewBox="0 0 12 16" width="12"><path fill-rule="evenodd" d="M12 5l-8 8-4-4 1.5-1.5L4 10l6.5-6.5z"/></svg>
              <span class="select-menu-item-text css-truncate-target js-select-menu-filter-text">
                1768-organization-list
              </span>
            </a>
            <a class="select-menu-item js-navigation-item js-navigation-open "
               href="/ckan/ckan/blob/1792-filterable-resource-views/ckan/config/routing.py"
               data-name="1792-filterable-resource-views"
               data-skip-pjax="true"
               rel="nofollow">
              <svg aria-hidden="true" class="octicon octicon-check select-menu-item-icon" height="16" version="1.1" viewBox="0 0 12 16" width="12"><path fill-rule="evenodd" d="M12 5l-8 8-4-4 1.5-1.5L4 10l6.5-6.5z"/></svg>
              <span class="select-menu-item-text css-truncate-target js-select-menu-filter-text">
                1792-filterable-resource-views
              </span>
            </a>
            <a class="select-menu-item js-navigation-item js-navigation-open "
               href="/ckan/ckan/blob/1811-make-docker-container-names-consistent/ckan/config/routing.py"
               data-name="1811-make-docker-container-names-consistent"
               data-skip-pjax="true"
               rel="nofollow">
              <svg aria-hidden="true" class="octicon octicon-check select-menu-item-icon" height="16" version="1.1" viewBox="0 0 12 16" width="12"><path fill-rule="evenodd" d="M12 5l-8 8-4-4 1.5-1.5L4 10l6.5-6.5z"/></svg>
              <span class="select-menu-item-text css-truncate-target js-select-menu-filter-text">
                1811-make-docker-container-names-consistent
              </span>
            </a>
            <a class="select-menu-item js-navigation-item js-navigation-open "
               href="/ckan/ckan/blob/1816-update-requirements-2.3/ckan/config/routing.py"
               data-name="1816-update-requirements-2.3"
               data-skip-pjax="true"
               rel="nofollow">
              <svg aria-hidden="true" class="octicon octicon-check select-menu-item-icon" height="16" version="1.1" viewBox="0 0 12 16" width="12"><path fill-rule="evenodd" d="M12 5l-8 8-4-4 1.5-1.5L4 10l6.5-6.5z"/></svg>
              <span class="select-menu-item-text css-truncate-target js-select-menu-filter-text">
                1816-update-requirements-2.3
              </span>
            </a>
            <a class="select-menu-item js-navigation-item js-navigation-open "
               href="/ckan/ckan/blob/1852-2-potential-db-less-views/ckan/config/routing.py"
               data-name="1852-2-potential-db-less-views"
               data-skip-pjax="true"
               rel="nofollow">
              <svg aria-hidden="true" class="octicon octicon-check select-menu-item-icon" height="16" version="1.1" viewBox="0 0 12 16" width="12"><path fill-rule="evenodd" d="M12 5l-8 8-4-4 1.5-1.5L4 10l6.5-6.5z"/></svg>
              <span class="select-menu-item-text css-truncate-target js-select-menu-filter-text">
                1852-2-potential-db-less-views
              </span>
            </a>
            <a class="select-menu-item js-navigation-item js-navigation-open "
               href="/ckan/ckan/blob/1852-default-resource-views/ckan/config/routing.py"
               data-name="1852-default-resource-views"
               data-skip-pjax="true"
               rel="nofollow">
              <svg aria-hidden="true" class="octicon octicon-check select-menu-item-icon" height="16" version="1.1" viewBox="0 0 12 16" width="12"><path fill-rule="evenodd" d="M12 5l-8 8-4-4 1.5-1.5L4 10l6.5-6.5z"/></svg>
              <span class="select-menu-item-text css-truncate-target js-select-menu-filter-text">
                1852-default-resource-views
              </span>
            </a>
            <a class="select-menu-item js-navigation-item js-navigation-open "
               href="/ckan/ckan/blob/1871-datastore-sql-tables/ckan/config/routing.py"
               data-name="1871-datastore-sql-tables"
               data-skip-pjax="true"
               rel="nofollow">
              <svg aria-hidden="true" class="octicon octicon-check select-menu-item-icon" height="16" version="1.1" viewBox="0 0 12 16" width="12"><path fill-rule="evenodd" d="M12 5l-8 8-4-4 1.5-1.5L4 10l6.5-6.5z"/></svg>
              <span class="select-menu-item-text css-truncate-target js-select-menu-filter-text">
                1871-datastore-sql-tables
              </span>
            </a>
            <a class="select-menu-item js-navigation-item js-navigation-open "
               href="/ckan/ckan/blob/1872-correct-ini-file/ckan/config/routing.py"
               data-name="1872-correct-ini-file"
               data-skip-pjax="true"
               rel="nofollow">
              <svg aria-hidden="true" class="octicon octicon-check select-menu-item-icon" height="16" version="1.1" viewBox="0 0 12 16" width="12"><path fill-rule="evenodd" d="M12 5l-8 8-4-4 1.5-1.5L4 10l6.5-6.5z"/></svg>
              <span class="select-menu-item-text css-truncate-target js-select-menu-filter-text">
                1872-correct-ini-file
              </span>
            </a>
            <a class="select-menu-item js-navigation-item js-navigation-open "
               href="/ckan/ckan/blob/1876-fix-some-broken-links-in-the-docs/ckan/config/routing.py"
               data-name="1876-fix-some-broken-links-in-the-docs"
               data-skip-pjax="true"
               rel="nofollow">
              <svg aria-hidden="true" class="octicon octicon-check select-menu-item-icon" height="16" version="1.1" viewBox="0 0 12 16" width="12"><path fill-rule="evenodd" d="M12 5l-8 8-4-4 1.5-1.5L4 10l6.5-6.5z"/></svg>
              <span class="select-menu-item-text css-truncate-target js-select-menu-filter-text">
                1876-fix-some-broken-links-in-the-docs
              </span>
            </a>
            <a class="select-menu-item js-navigation-item js-navigation-open "
               href="/ckan/ckan/blob/1882-incorrect-org-link/ckan/config/routing.py"
               data-name="1882-incorrect-org-link"
               data-skip-pjax="true"
               rel="nofollow">
              <svg aria-hidden="true" class="octicon octicon-check select-menu-item-icon" height="16" version="1.1" viewBox="0 0 12 16" width="12"><path fill-rule="evenodd" d="M12 5l-8 8-4-4 1.5-1.5L4 10l6.5-6.5z"/></svg>
              <span class="select-menu-item-text css-truncate-target js-select-menu-filter-text">
                1882-incorrect-org-link
              </span>
            </a>
            <a class="select-menu-item js-navigation-item js-navigation-open "
               href="/ckan/ckan/blob/1894-use-extras-and-convert_to_extras/ckan/config/routing.py"
               data-name="1894-use-extras-and-convert_to_extras"
               data-skip-pjax="true"
               rel="nofollow">
              <svg aria-hidden="true" class="octicon octicon-check select-menu-item-icon" height="16" version="1.1" viewBox="0 0 12 16" width="12"><path fill-rule="evenodd" d="M12 5l-8 8-4-4 1.5-1.5L4 10l6.5-6.5z"/></svg>
              <span class="select-menu-item-text css-truncate-target js-select-menu-filter-text">
                1894-use-extras-and-convert_to_extras
              </span>
            </a>
            <a class="select-menu-item js-navigation-item js-navigation-open "
               href="/ckan/ckan/blob/1903-remove-old-authz-code/ckan/config/routing.py"
               data-name="1903-remove-old-authz-code"
               data-skip-pjax="true"
               rel="nofollow">
              <svg aria-hidden="true" class="octicon octicon-check select-menu-item-icon" height="16" version="1.1" viewBox="0 0 12 16" width="12"><path fill-rule="evenodd" d="M12 5l-8 8-4-4 1.5-1.5L4 10l6.5-6.5z"/></svg>
              <span class="select-menu-item-text css-truncate-target js-select-menu-filter-text">
                1903-remove-old-authz-code
              </span>
            </a>
            <a class="select-menu-item js-navigation-item js-navigation-open "
               href="/ckan/ckan/blob/1917/ckan/config/routing.py"
               data-name="1917"
               data-skip-pjax="true"
               rel="nofollow">
              <svg aria-hidden="true" class="octicon octicon-check select-menu-item-icon" height="16" version="1.1" viewBox="0 0 12 16" width="12"><path fill-rule="evenodd" d="M12 5l-8 8-4-4 1.5-1.5L4 10l6.5-6.5z"/></svg>
              <span class="select-menu-item-text css-truncate-target js-select-menu-filter-text">
                1917
              </span>
            </a>
            <a class="select-menu-item js-navigation-item js-navigation-open "
               href="/ckan/ckan/blob/1936-stats-plugin-active-datasets/ckan/config/routing.py"
               data-name="1936-stats-plugin-active-datasets"
               data-skip-pjax="true"
               rel="nofollow">
              <svg aria-hidden="true" class="octicon octicon-check select-menu-item-icon" height="16" version="1.1" viewBox="0 0 12 16" width="12"><path fill-rule="evenodd" d="M12 5l-8 8-4-4 1.5-1.5L4 10l6.5-6.5z"/></svg>
              <span class="select-menu-item-text css-truncate-target js-select-menu-filter-text">
                1936-stats-plugin-active-datasets
              </span>
            </a>
            <a class="select-menu-item js-navigation-item js-navigation-open "
               href="/ckan/ckan/blob/1946-fix-sphinx-html-build/ckan/config/routing.py"
               data-name="1946-fix-sphinx-html-build"
               data-skip-pjax="true"
               rel="nofollow">
              <svg aria-hidden="true" class="octicon octicon-check select-menu-item-icon" height="16" version="1.1" viewBox="0 0 12 16" width="12"><path fill-rule="evenodd" d="M12 5l-8 8-4-4 1.5-1.5L4 10l6.5-6.5z"/></svg>
              <span class="select-menu-item-text css-truncate-target js-select-menu-filter-text">
                1946-fix-sphinx-html-build
              </span>
            </a>
            <a class="select-menu-item js-navigation-item js-navigation-open "
               href="/ckan/ckan/blob/1951-local-images-only/ckan/config/routing.py"
               data-name="1951-local-images-only"
               data-skip-pjax="true"
               rel="nofollow">
              <svg aria-hidden="true" class="octicon octicon-check select-menu-item-icon" height="16" version="1.1" viewBox="0 0 12 16" width="12"><path fill-rule="evenodd" d="M12 5l-8 8-4-4 1.5-1.5L4 10l6.5-6.5z"/></svg>
              <span class="select-menu-item-text css-truncate-target js-select-menu-filter-text">
                1951-local-images-only
              </span>
            </a>
            <a class="select-menu-item js-navigation-item js-navigation-open "
               href="/ckan/ckan/blob/1993-unmingle-bootstrap/ckan/config/routing.py"
               data-name="1993-unmingle-bootstrap"
               data-skip-pjax="true"
               rel="nofollow">
              <svg aria-hidden="true" class="octicon octicon-check select-menu-item-icon" height="16" version="1.1" viewBox="0 0 12 16" width="12"><path fill-rule="evenodd" d="M12 5l-8 8-4-4 1.5-1.5L4 10l6.5-6.5z"/></svg>
              <span class="select-menu-item-text css-truncate-target js-select-menu-filter-text">
                1993-unmingle-bootstrap
              </span>
            </a>
            <a class="select-menu-item js-navigation-item js-navigation-open "
               href="/ckan/ckan/blob/2007-datastore-active-fix/ckan/config/routing.py"
               data-name="2007-datastore-active-fix"
               data-skip-pjax="true"
               rel="nofollow">
              <svg aria-hidden="true" class="octicon octicon-check select-menu-item-icon" height="16" version="1.1" viewBox="0 0 12 16" width="12"><path fill-rule="evenodd" d="M12 5l-8 8-4-4 1.5-1.5L4 10l6.5-6.5z"/></svg>
              <span class="select-menu-item-text css-truncate-target js-select-menu-filter-text">
                2007-datastore-active-fix
              </span>
            </a>
            <a class="select-menu-item js-navigation-item js-navigation-open "
               href="/ckan/ckan/blob/2035-remove-auth-permissions-cache/ckan/config/routing.py"
               data-name="2035-remove-auth-permissions-cache"
               data-skip-pjax="true"
               rel="nofollow">
              <svg aria-hidden="true" class="octicon octicon-check select-menu-item-icon" height="16" version="1.1" viewBox="0 0 12 16" width="12"><path fill-rule="evenodd" d="M12 5l-8 8-4-4 1.5-1.5L4 10l6.5-6.5z"/></svg>
              <span class="select-menu-item-text css-truncate-target js-select-menu-filter-text">
                2035-remove-auth-permissions-cache
              </span>
            </a>
            <a class="select-menu-item js-navigation-item js-navigation-open "
               href="/ckan/ckan/blob/2037-fix-resource-create-auth-2/ckan/config/routing.py"
               data-name="2037-fix-resource-create-auth-2"
               data-skip-pjax="true"
               rel="nofollow">
              <svg aria-hidden="true" class="octicon octicon-check select-menu-item-icon" height="16" version="1.1" viewBox="0 0 12 16" width="12"><path fill-rule="evenodd" d="M12 5l-8 8-4-4 1.5-1.5L4 10l6.5-6.5z"/></svg>
              <span class="select-menu-item-text css-truncate-target js-select-menu-filter-text">
                2037-fix-resource-create-auth-2
              </span>
            </a>
            <a class="select-menu-item js-navigation-item js-navigation-open "
               href="/ckan/ckan/blob/2037-fix-resource-create-auth/ckan/config/routing.py"
               data-name="2037-fix-resource-create-auth"
               data-skip-pjax="true"
               rel="nofollow">
              <svg aria-hidden="true" class="octicon octicon-check select-menu-item-icon" height="16" version="1.1" viewBox="0 0 12 16" width="12"><path fill-rule="evenodd" d="M12 5l-8 8-4-4 1.5-1.5L4 10l6.5-6.5z"/></svg>
              <span class="select-menu-item-text css-truncate-target js-select-menu-filter-text">
                2037-fix-resource-create-auth
              </span>
            </a>
            <a class="select-menu-item js-navigation-item js-navigation-open "
               href="/ckan/ckan/blob/2049-remove-group_package_show/ckan/config/routing.py"
               data-name="2049-remove-group_package_show"
               data-skip-pjax="true"
               rel="nofollow">
              <svg aria-hidden="true" class="octicon octicon-check select-menu-item-icon" height="16" version="1.1" viewBox="0 0 12 16" width="12"><path fill-rule="evenodd" d="M12 5l-8 8-4-4 1.5-1.5L4 10l6.5-6.5z"/></svg>
              <span class="select-menu-item-text css-truncate-target js-select-menu-filter-text">
                2049-remove-group_package_show
              </span>
            </a>
            <a class="select-menu-item js-navigation-item js-navigation-open "
               href="/ckan/ckan/blob/2068-remove-remnant/ckan/config/routing.py"
               data-name="2068-remove-remnant"
               data-skip-pjax="true"
               rel="nofollow">
              <svg aria-hidden="true" class="octicon octicon-check select-menu-item-icon" height="16" version="1.1" viewBox="0 0 12 16" width="12"><path fill-rule="evenodd" d="M12 5l-8 8-4-4 1.5-1.5L4 10l6.5-6.5z"/></svg>
              <span class="select-menu-item-text css-truncate-target js-select-menu-filter-text">
                2068-remove-remnant
              </span>
            </a>
            <a class="select-menu-item js-navigation-item js-navigation-open "
               href="/ckan/ckan/blob/2070-rating-moved/ckan/config/routing.py"
               data-name="2070-rating-moved"
               data-skip-pjax="true"
               rel="nofollow">
              <svg aria-hidden="true" class="octicon octicon-check select-menu-item-icon" height="16" version="1.1" viewBox="0 0 12 16" width="12"><path fill-rule="evenodd" d="M12 5l-8 8-4-4 1.5-1.5L4 10l6.5-6.5z"/></svg>
              <span class="select-menu-item-text css-truncate-target js-select-menu-filter-text">
                2070-rating-moved
              </span>
            </a>
            <a class="select-menu-item js-navigation-item js-navigation-open "
               href="/ckan/ckan/blob/2072-resource-status-test/ckan/config/routing.py"
               data-name="2072-resource-status-test"
               data-skip-pjax="true"
               rel="nofollow">
              <svg aria-hidden="true" class="octicon octicon-check select-menu-item-icon" height="16" version="1.1" viewBox="0 0 12 16" width="12"><path fill-rule="evenodd" d="M12 5l-8 8-4-4 1.5-1.5L4 10l6.5-6.5z"/></svg>
              <span class="select-menu-item-text css-truncate-target js-select-menu-filter-text">
                2072-resource-status-test
              </span>
            </a>
            <a class="select-menu-item js-navigation-item js-navigation-open "
               href="/ckan/ckan/blob/2087-remove-site-read-auth/ckan/config/routing.py"
               data-name="2087-remove-site-read-auth"
               data-skip-pjax="true"
               rel="nofollow">
              <svg aria-hidden="true" class="octicon octicon-check select-menu-item-icon" height="16" version="1.1" viewBox="0 0 12 16" width="12"><path fill-rule="evenodd" d="M12 5l-8 8-4-4 1.5-1.5L4 10l6.5-6.5z"/></svg>
              <span class="select-menu-item-text css-truncate-target js-select-menu-filter-text">
                2087-remove-site-read-auth
              </span>
            </a>
            <a class="select-menu-item js-navigation-item js-navigation-open "
               href="/ckan/ckan/blob/2104-vocab-auth/ckan/config/routing.py"
               data-name="2104-vocab-auth"
               data-skip-pjax="true"
               rel="nofollow">
              <svg aria-hidden="true" class="octicon octicon-check select-menu-item-icon" height="16" version="1.1" viewBox="0 0 12 16" width="12"><path fill-rule="evenodd" d="M12 5l-8 8-4-4 1.5-1.5L4 10l6.5-6.5z"/></svg>
              <span class="select-menu-item-text css-truncate-target js-select-menu-filter-text">
                2104-vocab-auth
              </span>
            </a>
            <a class="select-menu-item js-navigation-item js-navigation-open "
               href="/ckan/ckan/blob/2108-document-who-ini-changes/ckan/config/routing.py"
               data-name="2108-document-who-ini-changes"
               data-skip-pjax="true"
               rel="nofollow">
              <svg aria-hidden="true" class="octicon octicon-check select-menu-item-icon" height="16" version="1.1" viewBox="0 0 12 16" width="12"><path fill-rule="evenodd" d="M12 5l-8 8-4-4 1.5-1.5L4 10l6.5-6.5z"/></svg>
              <span class="select-menu-item-text css-truncate-target js-select-menu-filter-text">
                2108-document-who-ini-changes
              </span>
            </a>
            <a class="select-menu-item js-navigation-item js-navigation-open "
               href="/ckan/ckan/blob/2142-fix-crash-on-creating-dataset-in-web-ui/ckan/config/routing.py"
               data-name="2142-fix-crash-on-creating-dataset-in-web-ui"
               data-skip-pjax="true"
               rel="nofollow">
              <svg aria-hidden="true" class="octicon octicon-check select-menu-item-icon" height="16" version="1.1" viewBox="0 0 12 16" width="12"><path fill-rule="evenodd" d="M12 5l-8 8-4-4 1.5-1.5L4 10l6.5-6.5z"/></svg>
              <span class="select-menu-item-text css-truncate-target js-select-menu-filter-text">
                2142-fix-crash-on-creating-dataset-in-web-ui
              </span>
            </a>
            <a class="select-menu-item js-navigation-item js-navigation-open "
               href="/ckan/ckan/blob/2158-resource-extras/ckan/config/routing.py"
               data-name="2158-resource-extras"
               data-skip-pjax="true"
               rel="nofollow">
              <svg aria-hidden="true" class="octicon octicon-check select-menu-item-icon" height="16" version="1.1" viewBox="0 0 12 16" width="12"><path fill-rule="evenodd" d="M12 5l-8 8-4-4 1.5-1.5L4 10l6.5-6.5z"/></svg>
              <span class="select-menu-item-text css-truncate-target js-select-menu-filter-text">
                2158-resource-extras
              </span>
            </a>
            <a class="select-menu-item js-navigation-item js-navigation-open "
               href="/ckan/ckan/blob/2165-check-access-log/ckan/config/routing.py"
               data-name="2165-check-access-log"
               data-skip-pjax="true"
               rel="nofollow">
              <svg aria-hidden="true" class="octicon octicon-check select-menu-item-icon" height="16" version="1.1" viewBox="0 0 12 16" width="12"><path fill-rule="evenodd" d="M12 5l-8 8-4-4 1.5-1.5L4 10l6.5-6.5z"/></svg>
              <span class="select-menu-item-text css-truncate-target js-select-menu-filter-text">
                2165-check-access-log
              </span>
            </a>
            <a class="select-menu-item js-navigation-item js-navigation-open "
               href="/ckan/ckan/blob/2167-remove-extra_msg/ckan/config/routing.py"
               data-name="2167-remove-extra_msg"
               data-skip-pjax="true"
               rel="nofollow">
              <svg aria-hidden="true" class="octicon octicon-check select-menu-item-icon" height="16" version="1.1" viewBox="0 0 12 16" width="12"><path fill-rule="evenodd" d="M12 5l-8 8-4-4 1.5-1.5L4 10l6.5-6.5z"/></svg>
              <span class="select-menu-item-text css-truncate-target js-select-menu-filter-text">
                2167-remove-extra_msg
              </span>
            </a>
            <a class="select-menu-item js-navigation-item js-navigation-open "
               href="/ckan/ckan/blob/2175-package-show-validate-custom-schema/ckan/config/routing.py"
               data-name="2175-package-show-validate-custom-schema"
               data-skip-pjax="true"
               rel="nofollow">
              <svg aria-hidden="true" class="octicon octicon-check select-menu-item-icon" height="16" version="1.1" viewBox="0 0 12 16" width="12"><path fill-rule="evenodd" d="M12 5l-8 8-4-4 1.5-1.5L4 10l6.5-6.5z"/></svg>
              <span class="select-menu-item-text css-truncate-target js-select-menu-filter-text">
                2175-package-show-validate-custom-schema
              </span>
            </a>
            <a class="select-menu-item js-navigation-item js-navigation-open "
               href="/ckan/ckan/blob/2188-deleted-groups-visible/ckan/config/routing.py"
               data-name="2188-deleted-groups-visible"
               data-skip-pjax="true"
               rel="nofollow">
              <svg aria-hidden="true" class="octicon octicon-check select-menu-item-icon" height="16" version="1.1" viewBox="0 0 12 16" width="12"><path fill-rule="evenodd" d="M12 5l-8 8-4-4 1.5-1.5L4 10l6.5-6.5z"/></svg>
              <span class="select-menu-item-text css-truncate-target js-select-menu-filter-text">
                2188-deleted-groups-visible
              </span>
            </a>
            <a class="select-menu-item js-navigation-item js-navigation-open "
               href="/ckan/ckan/blob/2204-resource-views-cli/ckan/config/routing.py"
               data-name="2204-resource-views-cli"
               data-skip-pjax="true"
               rel="nofollow">
              <svg aria-hidden="true" class="octicon octicon-check select-menu-item-icon" height="16" version="1.1" viewBox="0 0 12 16" width="12"><path fill-rule="evenodd" d="M12 5l-8 8-4-4 1.5-1.5L4 10l6.5-6.5z"/></svg>
              <span class="select-menu-item-text css-truncate-target js-select-menu-filter-text">
                2204-resource-views-cli
              </span>
            </a>
            <a class="select-menu-item js-navigation-item js-navigation-open "
               href="/ckan/ckan/blob/2205-resource-views-docs/ckan/config/routing.py"
               data-name="2205-resource-views-docs"
               data-skip-pjax="true"
               rel="nofollow">
              <svg aria-hidden="true" class="octicon octicon-check select-menu-item-icon" height="16" version="1.1" viewBox="0 0 12 16" width="12"><path fill-rule="evenodd" d="M12 5l-8 8-4-4 1.5-1.5L4 10l6.5-6.5z"/></svg>
              <span class="select-menu-item-text css-truncate-target js-select-menu-filter-text">
                2205-resource-views-docs
              </span>
            </a>
            <a class="select-menu-item js-navigation-item js-navigation-open "
               href="/ckan/ckan/blob/2210-use-group-show-not-group-dictize/ckan/config/routing.py"
               data-name="2210-use-group-show-not-group-dictize"
               data-skip-pjax="true"
               rel="nofollow">
              <svg aria-hidden="true" class="octicon octicon-check select-menu-item-icon" height="16" version="1.1" viewBox="0 0 12 16" width="12"><path fill-rule="evenodd" d="M12 5l-8 8-4-4 1.5-1.5L4 10l6.5-6.5z"/></svg>
              <span class="select-menu-item-text css-truncate-target js-select-menu-filter-text">
                2210-use-group-show-not-group-dictize
              </span>
            </a>
            <a class="select-menu-item js-navigation-item js-navigation-open "
               href="/ckan/ckan/blob/2222-fix-resource-views-format/ckan/config/routing.py"
               data-name="2222-fix-resource-views-format"
               data-skip-pjax="true"
               rel="nofollow">
              <svg aria-hidden="true" class="octicon octicon-check select-menu-item-icon" height="16" version="1.1" viewBox="0 0 12 16" width="12"><path fill-rule="evenodd" d="M12 5l-8 8-4-4 1.5-1.5L4 10l6.5-6.5z"/></svg>
              <span class="select-menu-item-text css-truncate-target js-select-menu-filter-text">
                2222-fix-resource-views-format
              </span>
            </a>
            <a class="select-menu-item js-navigation-item js-navigation-open "
               href="/ckan/ckan/blob/2234-further-migration-checks/ckan/config/routing.py"
               data-name="2234-further-migration-checks"
               data-skip-pjax="true"
               rel="nofollow">
              <svg aria-hidden="true" class="octicon octicon-check select-menu-item-icon" height="16" version="1.1" viewBox="0 0 12 16" width="12"><path fill-rule="evenodd" d="M12 5l-8 8-4-4 1.5-1.5L4 10l6.5-6.5z"/></svg>
              <span class="select-menu-item-text css-truncate-target js-select-menu-filter-text">
                2234-further-migration-checks
              </span>
            </a>
            <a class="select-menu-item js-navigation-item js-navigation-open "
               href="/ckan/ckan/blob/2234-persist-datastore_active/ckan/config/routing.py"
               data-name="2234-persist-datastore_active"
               data-skip-pjax="true"
               rel="nofollow">
              <svg aria-hidden="true" class="octicon octicon-check select-menu-item-icon" height="16" version="1.1" viewBox="0 0 12 16" width="12"><path fill-rule="evenodd" d="M12 5l-8 8-4-4 1.5-1.5L4 10l6.5-6.5z"/></svg>
              <span class="select-menu-item-text css-truncate-target js-select-menu-filter-text">
                2234-persist-datastore_active
              </span>
            </a>
            <a class="select-menu-item js-navigation-item js-navigation-open "
               href="/ckan/ckan/blob/2257-clean-helper-functions/ckan/config/routing.py"
               data-name="2257-clean-helper-functions"
               data-skip-pjax="true"
               rel="nofollow">
              <svg aria-hidden="true" class="octicon octicon-check select-menu-item-icon" height="16" version="1.1" viewBox="0 0 12 16" width="12"><path fill-rule="evenodd" d="M12 5l-8 8-4-4 1.5-1.5L4 10l6.5-6.5z"/></svg>
              <span class="select-menu-item-text css-truncate-target js-select-menu-filter-text">
                2257-clean-helper-functions
              </span>
            </a>
            <a class="select-menu-item js-navigation-item js-navigation-open "
               href="/ckan/ckan/blob/2266-update-deployment-template/ckan/config/routing.py"
               data-name="2266-update-deployment-template"
               data-skip-pjax="true"
               rel="nofollow">
              <svg aria-hidden="true" class="octicon octicon-check select-menu-item-icon" height="16" version="1.1" viewBox="0 0 12 16" width="12"><path fill-rule="evenodd" d="M12 5l-8 8-4-4 1.5-1.5L4 10l6.5-6.5z"/></svg>
              <span class="select-menu-item-text css-truncate-target js-select-menu-filter-text">
                2266-update-deployment-template
              </span>
            </a>
            <a class="select-menu-item js-navigation-item js-navigation-open "
               href="/ckan/ckan/blob/2302-simple-themes/ckan/config/routing.py"
               data-name="2302-simple-themes"
               data-skip-pjax="true"
               rel="nofollow">
              <svg aria-hidden="true" class="octicon octicon-check select-menu-item-icon" height="16" version="1.1" viewBox="0 0 12 16" width="12"><path fill-rule="evenodd" d="M12 5l-8 8-4-4 1.5-1.5L4 10l6.5-6.5z"/></svg>
              <span class="select-menu-item-text css-truncate-target js-select-menu-filter-text">
                2302-simple-themes
              </span>
            </a>
            <a class="select-menu-item js-navigation-item js-navigation-open "
               href="/ckan/ckan/blob/2307-datasets-in-dashboard/ckan/config/routing.py"
               data-name="2307-datasets-in-dashboard"
               data-skip-pjax="true"
               rel="nofollow">
              <svg aria-hidden="true" class="octicon octicon-check select-menu-item-icon" height="16" version="1.1" viewBox="0 0 12 16" width="12"><path fill-rule="evenodd" d="M12 5l-8 8-4-4 1.5-1.5L4 10l6.5-6.5z"/></svg>
              <span class="select-menu-item-text css-truncate-target js-select-menu-filter-text">
                2307-datasets-in-dashboard
              </span>
            </a>
            <a class="select-menu-item js-navigation-item js-navigation-open "
               href="/ckan/ckan/blob/2311-resource-view-default-title/ckan/config/routing.py"
               data-name="2311-resource-view-default-title"
               data-skip-pjax="true"
               rel="nofollow">
              <svg aria-hidden="true" class="octicon octicon-check select-menu-item-icon" height="16" version="1.1" viewBox="0 0 12 16" width="12"><path fill-rule="evenodd" d="M12 5l-8 8-4-4 1.5-1.5L4 10l6.5-6.5z"/></svg>
              <span class="select-menu-item-text css-truncate-target js-select-menu-filter-text">
                2311-resource-view-default-title
              </span>
            </a>
            <a class="select-menu-item js-navigation-item js-navigation-open "
               href="/ckan/ckan/blob/2313-deprecate-old-facet-data-structures-and-related-functions/ckan/config/routing.py"
               data-name="2313-deprecate-old-facet-data-structures-and-related-functions"
               data-skip-pjax="true"
               rel="nofollow">
              <svg aria-hidden="true" class="octicon octicon-check select-menu-item-icon" height="16" version="1.1" viewBox="0 0 12 16" width="12"><path fill-rule="evenodd" d="M12 5l-8 8-4-4 1.5-1.5L4 10l6.5-6.5z"/></svg>
              <span class="select-menu-item-text css-truncate-target js-select-menu-filter-text">
                2313-deprecate-old-facet-data-structures-and-related-functions
              </span>
            </a>
            <a class="select-menu-item js-navigation-item js-navigation-open "
               href="/ckan/ckan/blob/2322-recline-views-datastore-only/ckan/config/routing.py"
               data-name="2322-recline-views-datastore-only"
               data-skip-pjax="true"
               rel="nofollow">
              <svg aria-hidden="true" class="octicon octicon-check select-menu-item-icon" height="16" version="1.1" viewBox="0 0 12 16" width="12"><path fill-rule="evenodd" d="M12 5l-8 8-4-4 1.5-1.5L4 10l6.5-6.5z"/></svg>
              <span class="select-menu-item-text css-truncate-target js-select-menu-filter-text">
                2322-recline-views-datastore-only
              </span>
            </a>
            <a class="select-menu-item js-navigation-item js-navigation-open "
               href="/ckan/ckan/blob/2334-date-check-utcnow/ckan/config/routing.py"
               data-name="2334-date-check-utcnow"
               data-skip-pjax="true"
               rel="nofollow">
              <svg aria-hidden="true" class="octicon octicon-check select-menu-item-icon" height="16" version="1.1" viewBox="0 0 12 16" width="12"><path fill-rule="evenodd" d="M12 5l-8 8-4-4 1.5-1.5L4 10l6.5-6.5z"/></svg>
              <span class="select-menu-item-text css-truncate-target js-select-menu-filter-text">
                2334-date-check-utcnow
              </span>
            </a>
            <a class="select-menu-item js-navigation-item js-navigation-open "
               href="/ckan/ckan/blob/2350-license-schema/ckan/config/routing.py"
               data-name="2350-license-schema"
               data-skip-pjax="true"
               rel="nofollow">
              <svg aria-hidden="true" class="octicon octicon-check select-menu-item-icon" height="16" version="1.1" viewBox="0 0 12 16" width="12"><path fill-rule="evenodd" d="M12 5l-8 8-4-4 1.5-1.5L4 10l6.5-6.5z"/></svg>
              <span class="select-menu-item-text css-truncate-target js-select-menu-filter-text">
                2350-license-schema
              </span>
            </a>
            <a class="select-menu-item js-navigation-item js-navigation-open "
               href="/ckan/ckan/blob/2362-toolkit-doc-part1/ckan/config/routing.py"
               data-name="2362-toolkit-doc-part1"
               data-skip-pjax="true"
               rel="nofollow">
              <svg aria-hidden="true" class="octicon octicon-check select-menu-item-icon" height="16" version="1.1" viewBox="0 0 12 16" width="12"><path fill-rule="evenodd" d="M12 5l-8 8-4-4 1.5-1.5L4 10l6.5-6.5z"/></svg>
              <span class="select-menu-item-text css-truncate-target js-select-menu-filter-text">
                2362-toolkit-doc-part1
              </span>
            </a>
            <a class="select-menu-item js-navigation-item js-navigation-open "
               href="/ckan/ckan/blob/2366-remove-authorization-groups/ckan/config/routing.py"
               data-name="2366-remove-authorization-groups"
               data-skip-pjax="true"
               rel="nofollow">
              <svg aria-hidden="true" class="octicon octicon-check select-menu-item-icon" height="16" version="1.1" viewBox="0 0 12 16" width="12"><path fill-rule="evenodd" d="M12 5l-8 8-4-4 1.5-1.5L4 10l6.5-6.5z"/></svg>
              <span class="select-menu-item-text css-truncate-target js-select-menu-filter-text">
                2366-remove-authorization-groups
              </span>
            </a>
            <a class="select-menu-item js-navigation-item js-navigation-open "
               href="/ckan/ckan/blob/2368-get-request-param-helper/ckan/config/routing.py"
               data-name="2368-get-request-param-helper"
               data-skip-pjax="true"
               rel="nofollow">
              <svg aria-hidden="true" class="octicon octicon-check select-menu-item-icon" height="16" version="1.1" viewBox="0 0 12 16" width="12"><path fill-rule="evenodd" d="M12 5l-8 8-4-4 1.5-1.5L4 10l6.5-6.5z"/></svg>
              <span class="select-menu-item-text css-truncate-target js-select-menu-filter-text">
                2368-get-request-param-helper
              </span>
            </a>
            <a class="select-menu-item js-navigation-item js-navigation-open "
               href="/ckan/ckan/blob/2375-demo-organizations/ckan/config/routing.py"
               data-name="2375-demo-organizations"
               data-skip-pjax="true"
               rel="nofollow">
              <svg aria-hidden="true" class="octicon octicon-check select-menu-item-icon" height="16" version="1.1" viewBox="0 0 12 16" width="12"><path fill-rule="evenodd" d="M12 5l-8 8-4-4 1.5-1.5L4 10l6.5-6.5z"/></svg>
              <span class="select-menu-item-text css-truncate-target js-select-menu-filter-text">
                2375-demo-organizations
              </span>
            </a>
            <a class="select-menu-item js-navigation-item js-navigation-open "
               href="/ckan/ckan/blob/2375-demo-theme-development-frontend-build/ckan/config/routing.py"
               data-name="2375-demo-theme-development-frontend-build"
               data-skip-pjax="true"
               rel="nofollow">
              <svg aria-hidden="true" class="octicon octicon-check select-menu-item-icon" height="16" version="1.1" viewBox="0 0 12 16" width="12"><path fill-rule="evenodd" d="M12 5l-8 8-4-4 1.5-1.5L4 10l6.5-6.5z"/></svg>
              <span class="select-menu-item-text css-truncate-target js-select-menu-filter-text">
                2375-demo-theme-development-frontend-build
              </span>
            </a>
            <a class="select-menu-item js-navigation-item js-navigation-open "
               href="/ckan/ckan/blob/2375-demo-theme-stable/ckan/config/routing.py"
               data-name="2375-demo-theme-stable"
               data-skip-pjax="true"
               rel="nofollow">
              <svg aria-hidden="true" class="octicon octicon-check select-menu-item-icon" height="16" version="1.1" viewBox="0 0 12 16" width="12"><path fill-rule="evenodd" d="M12 5l-8 8-4-4 1.5-1.5L4 10l6.5-6.5z"/></svg>
              <span class="select-menu-item-text css-truncate-target js-select-menu-filter-text">
                2375-demo-theme-stable
              </span>
            </a>
            <a class="select-menu-item js-navigation-item js-navigation-open "
               href="/ckan/ckan/blob/2387-fix-geojson-field-map-view/ckan/config/routing.py"
               data-name="2387-fix-geojson-field-map-view"
               data-skip-pjax="true"
               rel="nofollow">
              <svg aria-hidden="true" class="octicon octicon-check select-menu-item-icon" height="16" version="1.1" viewBox="0 0 12 16" width="12"><path fill-rule="evenodd" d="M12 5l-8 8-4-4 1.5-1.5L4 10l6.5-6.5z"/></svg>
              <span class="select-menu-item-text css-truncate-target js-select-menu-filter-text">
                2387-fix-geojson-field-map-view
              </span>
            </a>
            <a class="select-menu-item js-navigation-item js-navigation-open "
               href="/ckan/ckan/blob/2388-out-of-the-box-auth-settings/ckan/config/routing.py"
               data-name="2388-out-of-the-box-auth-settings"
               data-skip-pjax="true"
               rel="nofollow">
              <svg aria-hidden="true" class="octicon octicon-check select-menu-item-icon" height="16" version="1.1" viewBox="0 0 12 16" width="12"><path fill-rule="evenodd" d="M12 5l-8 8-4-4 1.5-1.5L4 10l6.5-6.5z"/></svg>
              <span class="select-menu-item-text css-truncate-target js-select-menu-filter-text">
                2388-out-of-the-box-auth-settings
              </span>
            </a>
            <a class="select-menu-item js-navigation-item js-navigation-open "
               href="/ckan/ckan/blob/2426-imapper-delete/ckan/config/routing.py"
               data-name="2426-imapper-delete"
               data-skip-pjax="true"
               rel="nofollow">
              <svg aria-hidden="true" class="octicon octicon-check select-menu-item-icon" height="16" version="1.1" viewBox="0 0 12 16" width="12"><path fill-rule="evenodd" d="M12 5l-8 8-4-4 1.5-1.5L4 10l6.5-6.5z"/></svg>
              <span class="select-menu-item-text css-truncate-target js-select-menu-filter-text">
                2426-imapper-delete
              </span>
            </a>
            <a class="select-menu-item js-navigation-item js-navigation-open "
               href="/ckan/ckan/blob/2428-audit-dependencies/ckan/config/routing.py"
               data-name="2428-audit-dependencies"
               data-skip-pjax="true"
               rel="nofollow">
              <svg aria-hidden="true" class="octicon octicon-check select-menu-item-icon" height="16" version="1.1" viewBox="0 0 12 16" width="12"><path fill-rule="evenodd" d="M12 5l-8 8-4-4 1.5-1.5L4 10l6.5-6.5z"/></svg>
              <span class="select-menu-item-text css-truncate-target js-select-menu-filter-text">
                2428-audit-dependencies
              </span>
            </a>
            <a class="select-menu-item js-navigation-item js-navigation-open "
               href="/ckan/ckan/blob/2429-config-env-var/ckan/config/routing.py"
               data-name="2429-config-env-var"
               data-skip-pjax="true"
               rel="nofollow">
              <svg aria-hidden="true" class="octicon octicon-check select-menu-item-icon" height="16" version="1.1" viewBox="0 0 12 16" width="12"><path fill-rule="evenodd" d="M12 5l-8 8-4-4 1.5-1.5L4 10l6.5-6.5z"/></svg>
              <span class="select-menu-item-text css-truncate-target js-select-menu-filter-text">
                2429-config-env-var
              </span>
            </a>
            <a class="select-menu-item js-navigation-item js-navigation-open "
               href="/ckan/ckan/blob/2435-exception-package_update/ckan/config/routing.py"
               data-name="2435-exception-package_update"
               data-skip-pjax="true"
               rel="nofollow">
              <svg aria-hidden="true" class="octicon octicon-check select-menu-item-icon" height="16" version="1.1" viewBox="0 0 12 16" width="12"><path fill-rule="evenodd" d="M12 5l-8 8-4-4 1.5-1.5L4 10l6.5-6.5z"/></svg>
              <span class="select-menu-item-text css-truncate-target js-select-menu-filter-text">
                2435-exception-package_update
              </span>
            </a>
            <a class="select-menu-item js-navigation-item js-navigation-open "
               href="/ckan/ckan/blob/2438-resource_search-action-accessible-via-get-request/ckan/config/routing.py"
               data-name="2438-resource_search-action-accessible-via-get-request"
               data-skip-pjax="true"
               rel="nofollow">
              <svg aria-hidden="true" class="octicon octicon-check select-menu-item-icon" height="16" version="1.1" viewBox="0 0 12 16" width="12"><path fill-rule="evenodd" d="M12 5l-8 8-4-4 1.5-1.5L4 10l6.5-6.5z"/></svg>
              <span class="select-menu-item-text css-truncate-target js-select-menu-filter-text">
                2438-resource_search-action-accessible-via-get-request
              </span>
            </a>
            <a class="select-menu-item js-navigation-item js-navigation-open "
               href="/ckan/ckan/blob/2439-tag_search-and-tag_autocomplete-GETable/ckan/config/routing.py"
               data-name="2439-tag_search-and-tag_autocomplete-GETable"
               data-skip-pjax="true"
               rel="nofollow">
              <svg aria-hidden="true" class="octicon octicon-check select-menu-item-icon" height="16" version="1.1" viewBox="0 0 12 16" width="12"><path fill-rule="evenodd" d="M12 5l-8 8-4-4 1.5-1.5L4 10l6.5-6.5z"/></svg>
              <span class="select-menu-item-text css-truncate-target js-select-menu-filter-text">
                2439-tag_search-and-tag_autocomplete-GETable
              </span>
            </a>
            <a class="select-menu-item js-navigation-item js-navigation-open "
               href="/ckan/ckan/blob/2462-upgrade-beaker/ckan/config/routing.py"
               data-name="2462-upgrade-beaker"
               data-skip-pjax="true"
               rel="nofollow">
              <svg aria-hidden="true" class="octicon octicon-check select-menu-item-icon" height="16" version="1.1" viewBox="0 0 12 16" width="12"><path fill-rule="evenodd" d="M12 5l-8 8-4-4 1.5-1.5L4 10l6.5-6.5z"/></svg>
              <span class="select-menu-item-text css-truncate-target js-select-menu-filter-text">
                2462-upgrade-beaker
              </span>
            </a>
            <a class="select-menu-item js-navigation-item js-navigation-open "
               href="/ckan/ckan/blob/2478-licenses-specific/ckan/config/routing.py"
               data-name="2478-licenses-specific"
               data-skip-pjax="true"
               rel="nofollow">
              <svg aria-hidden="true" class="octicon octicon-check select-menu-item-icon" height="16" version="1.1" viewBox="0 0 12 16" width="12"><path fill-rule="evenodd" d="M12 5l-8 8-4-4 1.5-1.5L4 10l6.5-6.5z"/></svg>
              <span class="select-menu-item-text css-truncate-target js-select-menu-filter-text">
                2478-licenses-specific
              </span>
            </a>
            <a class="select-menu-item js-navigation-item js-navigation-open "
               href="/ckan/ckan/blob/2482-related-items-500-error-followers/ckan/config/routing.py"
               data-name="2482-related-items-500-error-followers"
               data-skip-pjax="true"
               rel="nofollow">
              <svg aria-hidden="true" class="octicon octicon-check select-menu-item-icon" height="16" version="1.1" viewBox="0 0 12 16" width="12"><path fill-rule="evenodd" d="M12 5l-8 8-4-4 1.5-1.5L4 10l6.5-6.5z"/></svg>
              <span class="select-menu-item-text css-truncate-target js-select-menu-filter-text">
                2482-related-items-500-error-followers
              </span>
            </a>
            <a class="select-menu-item js-navigation-item js-navigation-open "
               href="/ckan/ckan/blob/2484-new-context-default-views/ckan/config/routing.py"
               data-name="2484-new-context-default-views"
               data-skip-pjax="true"
               rel="nofollow">
              <svg aria-hidden="true" class="octicon octicon-check select-menu-item-icon" height="16" version="1.1" viewBox="0 0 12 16" width="12"><path fill-rule="evenodd" d="M12 5l-8 8-4-4 1.5-1.5L4 10l6.5-6.5z"/></svg>
              <span class="select-menu-item-text css-truncate-target js-select-menu-filter-text">
                2484-new-context-default-views
              </span>
            </a>
            <a class="select-menu-item js-navigation-item js-navigation-open "
               href="/ckan/ckan/blob/2495-user-follow-tests/ckan/config/routing.py"
               data-name="2495-user-follow-tests"
               data-skip-pjax="true"
               rel="nofollow">
              <svg aria-hidden="true" class="octicon octicon-check select-menu-item-icon" height="16" version="1.1" viewBox="0 0 12 16" width="12"><path fill-rule="evenodd" d="M12 5l-8 8-4-4 1.5-1.5L4 10l6.5-6.5z"/></svg>
              <span class="select-menu-item-text css-truncate-target js-select-menu-filter-text">
                2495-user-follow-tests
              </span>
            </a>
            <a class="select-menu-item js-navigation-item js-navigation-open "
               href="/ckan/ckan/blob/2496-group-follow-tests/ckan/config/routing.py"
               data-name="2496-group-follow-tests"
               data-skip-pjax="true"
               rel="nofollow">
              <svg aria-hidden="true" class="octicon octicon-check select-menu-item-icon" height="16" version="1.1" viewBox="0 0 12 16" width="12"><path fill-rule="evenodd" d="M12 5l-8 8-4-4 1.5-1.5L4 10l6.5-6.5z"/></svg>
              <span class="select-menu-item-text css-truncate-target js-select-menu-filter-text">
                2496-group-follow-tests
              </span>
            </a>
            <a class="select-menu-item js-navigation-item js-navigation-open "
               href="/ckan/ckan/blob/2497-lose-language-on-abort/ckan/config/routing.py"
               data-name="2497-lose-language-on-abort"
               data-skip-pjax="true"
               rel="nofollow">
              <svg aria-hidden="true" class="octicon octicon-check select-menu-item-icon" height="16" version="1.1" viewBox="0 0 12 16" width="12"><path fill-rule="evenodd" d="M12 5l-8 8-4-4 1.5-1.5L4 10l6.5-6.5z"/></svg>
              <span class="select-menu-item-text css-truncate-target js-select-menu-filter-text">
                2497-lose-language-on-abort
              </span>
            </a>
            <a class="select-menu-item js-navigation-item js-navigation-open "
               href="/ckan/ckan/blob/2497-package-follow-tests/ckan/config/routing.py"
               data-name="2497-package-follow-tests"
               data-skip-pjax="true"
               rel="nofollow">
              <svg aria-hidden="true" class="octicon octicon-check select-menu-item-icon" height="16" version="1.1" viewBox="0 0 12 16" width="12"><path fill-rule="evenodd" d="M12 5l-8 8-4-4 1.5-1.5L4 10l6.5-6.5z"/></svg>
              <span class="select-menu-item-text css-truncate-target js-select-menu-filter-text">
                2497-package-follow-tests
              </span>
            </a>
            <a class="select-menu-item js-navigation-item js-navigation-open "
               href="/ckan/ckan/blob/2505-docs-improvements-for-1.7.1/ckan/config/routing.py"
               data-name="2505-docs-improvements-for-1.7.1"
               data-skip-pjax="true"
               rel="nofollow">
              <svg aria-hidden="true" class="octicon octicon-check select-menu-item-icon" height="16" version="1.1" viewBox="0 0 12 16" width="12"><path fill-rule="evenodd" d="M12 5l-8 8-4-4 1.5-1.5L4 10l6.5-6.5z"/></svg>
              <span class="select-menu-item-text css-truncate-target js-select-menu-filter-text">
                2505-docs-improvements-for-1.7.1
              </span>
            </a>
            <a class="select-menu-item js-navigation-item js-navigation-open "
               href="/ckan/ckan/blob/2510-iuploader-interface/ckan/config/routing.py"
               data-name="2510-iuploader-interface"
               data-skip-pjax="true"
               rel="nofollow">
              <svg aria-hidden="true" class="octicon octicon-check select-menu-item-icon" height="16" version="1.1" viewBox="0 0 12 16" width="12"><path fill-rule="evenodd" d="M12 5l-8 8-4-4 1.5-1.5L4 10l6.5-6.5z"/></svg>
              <span class="select-menu-item-text css-truncate-target js-select-menu-filter-text">
                2510-iuploader-interface
              </span>
            </a>
            <a class="select-menu-item js-navigation-item js-navigation-open "
               href="/ckan/ckan/blob/2515-related-tab-issue/ckan/config/routing.py"
               data-name="2515-related-tab-issue"
               data-skip-pjax="true"
               rel="nofollow">
              <svg aria-hidden="true" class="octicon octicon-check select-menu-item-icon" height="16" version="1.1" viewBox="0 0 12 16" width="12"><path fill-rule="evenodd" d="M12 5l-8 8-4-4 1.5-1.5L4 10l6.5-6.5z"/></svg>
              <span class="select-menu-item-text css-truncate-target js-select-menu-filter-text">
                2515-related-tab-issue
              </span>
            </a>
            <a class="select-menu-item js-navigation-item js-navigation-open "
               href="/ckan/ckan/blob/2516-purge-the-docs/ckan/config/routing.py"
               data-name="2516-purge-the-docs"
               data-skip-pjax="true"
               rel="nofollow">
              <svg aria-hidden="true" class="octicon octicon-check select-menu-item-icon" height="16" version="1.1" viewBox="0 0 12 16" width="12"><path fill-rule="evenodd" d="M12 5l-8 8-4-4 1.5-1.5L4 10l6.5-6.5z"/></svg>
              <span class="select-menu-item-text css-truncate-target js-select-menu-filter-text">
                2516-purge-the-docs
              </span>
            </a>
            <a class="select-menu-item js-navigation-item js-navigation-open "
               href="/ckan/ckan/blob/2518-datapusher-tracebacks/ckan/config/routing.py"
               data-name="2518-datapusher-tracebacks"
               data-skip-pjax="true"
               rel="nofollow">
              <svg aria-hidden="true" class="octicon octicon-check select-menu-item-icon" height="16" version="1.1" viewBox="0 0 12 16" width="12"><path fill-rule="evenodd" d="M12 5l-8 8-4-4 1.5-1.5L4 10l6.5-6.5z"/></svg>
              <span class="select-menu-item-text css-truncate-target js-select-menu-filter-text">
                2518-datapusher-tracebacks
              </span>
            </a>
            <a class="select-menu-item js-navigation-item js-navigation-open "
               href="/ckan/ckan/blob/2520-remove-attributedict/ckan/config/routing.py"
               data-name="2520-remove-attributedict"
               data-skip-pjax="true"
               rel="nofollow">
              <svg aria-hidden="true" class="octicon octicon-check select-menu-item-icon" height="16" version="1.1" viewBox="0 0 12 16" width="12"><path fill-rule="evenodd" d="M12 5l-8 8-4-4 1.5-1.5L4 10l6.5-6.5z"/></svg>
              <span class="select-menu-item-text css-truncate-target js-select-menu-filter-text">
                2520-remove-attributedict
              </span>
            </a>
            <a class="select-menu-item js-navigation-item js-navigation-open "
               href="/ckan/ckan/blob/2530-proxy-forbidden/ckan/config/routing.py"
               data-name="2530-proxy-forbidden"
               data-skip-pjax="true"
               rel="nofollow">
              <svg aria-hidden="true" class="octicon octicon-check select-menu-item-icon" height="16" version="1.1" viewBox="0 0 12 16" width="12"><path fill-rule="evenodd" d="M12 5l-8 8-4-4 1.5-1.5L4 10l6.5-6.5z"/></svg>
              <span class="select-menu-item-text css-truncate-target js-select-menu-filter-text">
                2530-proxy-forbidden
              </span>
            </a>
            <a class="select-menu-item js-navigation-item js-navigation-open "
               href="/ckan/ckan/blob/2532-dont-filter-datasets-on-views-create/ckan/config/routing.py"
               data-name="2532-dont-filter-datasets-on-views-create"
               data-skip-pjax="true"
               rel="nofollow">
              <svg aria-hidden="true" class="octicon octicon-check select-menu-item-icon" height="16" version="1.1" viewBox="0 0 12 16" width="12"><path fill-rule="evenodd" d="M12 5l-8 8-4-4 1.5-1.5L4 10l6.5-6.5z"/></svg>
              <span class="select-menu-item-text css-truncate-target js-select-menu-filter-text">
                2532-dont-filter-datasets-on-views-create
              </span>
            </a>
            <a class="select-menu-item js-navigation-item js-navigation-open "
               href="/ckan/ckan/blob/2549-merge-organizations/ckan/config/routing.py"
               data-name="2549-merge-organizations"
               data-skip-pjax="true"
               rel="nofollow">
              <svg aria-hidden="true" class="octicon octicon-check select-menu-item-icon" height="16" version="1.1" viewBox="0 0 12 16" width="12"><path fill-rule="evenodd" d="M12 5l-8 8-4-4 1.5-1.5L4 10l6.5-6.5z"/></svg>
              <span class="select-menu-item-text css-truncate-target js-select-menu-filter-text">
                2549-merge-organizations
              </span>
            </a>
            <a class="select-menu-item js-navigation-item js-navigation-open "
               href="/ckan/ckan/blob/2554-improve-group_list/ckan/config/routing.py"
               data-name="2554-improve-group_list"
               data-skip-pjax="true"
               rel="nofollow">
              <svg aria-hidden="true" class="octicon octicon-check select-menu-item-icon" height="16" version="1.1" viewBox="0 0 12 16" width="12"><path fill-rule="evenodd" d="M12 5l-8 8-4-4 1.5-1.5L4 10l6.5-6.5z"/></svg>
              <span class="select-menu-item-text css-truncate-target js-select-menu-filter-text">
                2554-improve-group_list
              </span>
            </a>
            <a class="select-menu-item js-navigation-item js-navigation-open "
               href="/ckan/ckan/blob/2555-deprecate-old-postgres/ckan/config/routing.py"
               data-name="2555-deprecate-old-postgres"
               data-skip-pjax="true"
               rel="nofollow">
              <svg aria-hidden="true" class="octicon octicon-check select-menu-item-icon" height="16" version="1.1" viewBox="0 0 12 16" width="12"><path fill-rule="evenodd" d="M12 5l-8 8-4-4 1.5-1.5L4 10l6.5-6.5z"/></svg>
              <span class="select-menu-item-text css-truncate-target js-select-menu-filter-text">
                2555-deprecate-old-postgres
              </span>
            </a>
            <a class="select-menu-item js-navigation-item js-navigation-open "
               href="/ckan/ckan/blob/2562-datastore-search-sql-private/ckan/config/routing.py"
               data-name="2562-datastore-search-sql-private"
               data-skip-pjax="true"
               rel="nofollow">
              <svg aria-hidden="true" class="octicon octicon-check select-menu-item-icon" height="16" version="1.1" viewBox="0 0 12 16" width="12"><path fill-rule="evenodd" d="M12 5l-8 8-4-4 1.5-1.5L4 10l6.5-6.5z"/></svg>
              <span class="select-menu-item-text css-truncate-target js-select-menu-filter-text">
                2562-datastore-search-sql-private
              </span>
            </a>
            <a class="select-menu-item js-navigation-item js-navigation-open "
               href="/ckan/ckan/blob/2575-license-i18n/ckan/config/routing.py"
               data-name="2575-license-i18n"
               data-skip-pjax="true"
               rel="nofollow">
              <svg aria-hidden="true" class="octicon octicon-check select-menu-item-icon" height="16" version="1.1" viewBox="0 0 12 16" width="12"><path fill-rule="evenodd" d="M12 5l-8 8-4-4 1.5-1.5L4 10l6.5-6.5z"/></svg>
              <span class="select-menu-item-text css-truncate-target js-select-menu-filter-text">
                2575-license-i18n
              </span>
            </a>
            <a class="select-menu-item js-navigation-item js-navigation-open "
               href="/ckan/ckan/blob/2592-update-source-install-docs/ckan/config/routing.py"
               data-name="2592-update-source-install-docs"
               data-skip-pjax="true"
               rel="nofollow">
              <svg aria-hidden="true" class="octicon octicon-check select-menu-item-icon" height="16" version="1.1" viewBox="0 0 12 16" width="12"><path fill-rule="evenodd" d="M12 5l-8 8-4-4 1.5-1.5L4 10l6.5-6.5z"/></svg>
              <span class="select-menu-item-text css-truncate-target js-select-menu-filter-text">
                2592-update-source-install-docs
              </span>
            </a>
            <a class="select-menu-item js-navigation-item js-navigation-open "
               href="/ckan/ckan/blob/2600-bug-replace-broken-login-to-add-organization-button/ckan/config/routing.py"
               data-name="2600-bug-replace-broken-login-to-add-organization-button"
               data-skip-pjax="true"
               rel="nofollow">
              <svg aria-hidden="true" class="octicon octicon-check select-menu-item-icon" height="16" version="1.1" viewBox="0 0 12 16" width="12"><path fill-rule="evenodd" d="M12 5l-8 8-4-4 1.5-1.5L4 10l6.5-6.5z"/></svg>
              <span class="select-menu-item-text css-truncate-target js-select-menu-filter-text">
                2600-bug-replace-broken-login-to-add-organization-button
              </span>
            </a>
            <a class="select-menu-item js-navigation-item js-navigation-open "
               href="/ckan/ckan/blob/2605-delete-history/ckan/config/routing.py"
               data-name="2605-delete-history"
               data-skip-pjax="true"
               rel="nofollow">
              <svg aria-hidden="true" class="octicon octicon-check select-menu-item-icon" height="16" version="1.1" viewBox="0 0 12 16" width="12"><path fill-rule="evenodd" d="M12 5l-8 8-4-4 1.5-1.5L4 10l6.5-6.5z"/></svg>
              <span class="select-menu-item-text css-truncate-target js-select-menu-filter-text">
                2605-delete-history
              </span>
            </a>
            <a class="select-menu-item js-navigation-item js-navigation-open "
               href="/ckan/ckan/blob/2605-user-get-groups-caching/ckan/config/routing.py"
               data-name="2605-user-get-groups-caching"
               data-skip-pjax="true"
               rel="nofollow">
              <svg aria-hidden="true" class="octicon octicon-check select-menu-item-icon" height="16" version="1.1" viewBox="0 0 12 16" width="12"><path fill-rule="evenodd" d="M12 5l-8 8-4-4 1.5-1.5L4 10l6.5-6.5z"/></svg>
              <span class="select-menu-item-text css-truncate-target js-select-menu-filter-text">
                2605-user-get-groups-caching
              </span>
            </a>
            <a class="select-menu-item js-navigation-item js-navigation-open "
               href="/ckan/ckan/blob/2609-delete-related-items/ckan/config/routing.py"
               data-name="2609-delete-related-items"
               data-skip-pjax="true"
               rel="nofollow">
              <svg aria-hidden="true" class="octicon octicon-check select-menu-item-icon" height="16" version="1.1" viewBox="0 0 12 16" width="12"><path fill-rule="evenodd" d="M12 5l-8 8-4-4 1.5-1.5L4 10l6.5-6.5z"/></svg>
              <span class="select-menu-item-text css-truncate-target js-select-menu-filter-text">
                2609-delete-related-items
              </span>
            </a>
            <a class="select-menu-item js-navigation-item js-navigation-open "
               href="/ckan/ckan/blob/2615-activities_for_follow/ckan/config/routing.py"
               data-name="2615-activities_for_follow"
               data-skip-pjax="true"
               rel="nofollow">
              <svg aria-hidden="true" class="octicon octicon-check select-menu-item-icon" height="16" version="1.1" viewBox="0 0 12 16" width="12"><path fill-rule="evenodd" d="M12 5l-8 8-4-4 1.5-1.5L4 10l6.5-6.5z"/></svg>
              <span class="select-menu-item-text css-truncate-target js-select-menu-filter-text">
                2615-activities_for_follow
              </span>
            </a>
            <a class="select-menu-item js-navigation-item js-navigation-open "
               href="/ckan/ckan/blob/2617-group-form/ckan/config/routing.py"
               data-name="2617-group-form"
               data-skip-pjax="true"
               rel="nofollow">
              <svg aria-hidden="true" class="octicon octicon-check select-menu-item-icon" height="16" version="1.1" viewBox="0 0 12 16" width="12"><path fill-rule="evenodd" d="M12 5l-8 8-4-4 1.5-1.5L4 10l6.5-6.5z"/></svg>
              <span class="select-menu-item-text css-truncate-target js-select-menu-filter-text">
                2617-group-form
              </span>
            </a>
            <a class="select-menu-item js-navigation-item js-navigation-open "
               href="/ckan/ckan/blob/2618-nested-resources/ckan/config/routing.py"
               data-name="2618-nested-resources"
               data-skip-pjax="true"
               rel="nofollow">
              <svg aria-hidden="true" class="octicon octicon-check select-menu-item-icon" height="16" version="1.1" viewBox="0 0 12 16" width="12"><path fill-rule="evenodd" d="M12 5l-8 8-4-4 1.5-1.5L4 10l6.5-6.5z"/></svg>
              <span class="select-menu-item-text css-truncate-target js-select-menu-filter-text">
                2618-nested-resources
              </span>
            </a>
            <a class="select-menu-item js-navigation-item js-navigation-open "
               href="/ckan/ckan/blob/2619-close-tag/ckan/config/routing.py"
               data-name="2619-close-tag"
               data-skip-pjax="true"
               rel="nofollow">
              <svg aria-hidden="true" class="octicon octicon-check select-menu-item-icon" height="16" version="1.1" viewBox="0 0 12 16" width="12"><path fill-rule="evenodd" d="M12 5l-8 8-4-4 1.5-1.5L4 10l6.5-6.5z"/></svg>
              <span class="select-menu-item-text css-truncate-target js-select-menu-filter-text">
                2619-close-tag
              </span>
            </a>
            <a class="select-menu-item js-navigation-item js-navigation-open "
               href="/ckan/ckan/blob/2624-organization-tags/ckan/config/routing.py"
               data-name="2624-organization-tags"
               data-skip-pjax="true"
               rel="nofollow">
              <svg aria-hidden="true" class="octicon octicon-check select-menu-item-icon" height="16" version="1.1" viewBox="0 0 12 16" width="12"><path fill-rule="evenodd" d="M12 5l-8 8-4-4 1.5-1.5L4 10l6.5-6.5z"/></svg>
              <span class="select-menu-item-text css-truncate-target js-select-menu-filter-text">
                2624-organization-tags
              </span>
            </a>
            <a class="select-menu-item js-navigation-item js-navigation-open "
               href="/ckan/ckan/blob/2627-bug-form-to-db-schema-not-called/ckan/config/routing.py"
               data-name="2627-bug-form-to-db-schema-not-called"
               data-skip-pjax="true"
               rel="nofollow">
              <svg aria-hidden="true" class="octicon octicon-check select-menu-item-icon" height="16" version="1.1" viewBox="0 0 12 16" width="12"><path fill-rule="evenodd" d="M12 5l-8 8-4-4 1.5-1.5L4 10l6.5-6.5z"/></svg>
              <span class="select-menu-item-text css-truncate-target js-select-menu-filter-text">
                2627-bug-form-to-db-schema-not-called
              </span>
            </a>
            <a class="select-menu-item js-navigation-item js-navigation-open "
               href="/ckan/ckan/blob/2631-group-purge/ckan/config/routing.py"
               data-name="2631-group-purge"
               data-skip-pjax="true"
               rel="nofollow">
              <svg aria-hidden="true" class="octicon octicon-check select-menu-item-icon" height="16" version="1.1" viewBox="0 0 12 16" width="12"><path fill-rule="evenodd" d="M12 5l-8 8-4-4 1.5-1.5L4 10l6.5-6.5z"/></svg>
              <span class="select-menu-item-text css-truncate-target js-select-menu-filter-text">
                2631-group-purge
              </span>
            </a>
            <a class="select-menu-item js-navigation-item js-navigation-open "
               href="/ckan/ckan/blob/2632-check-allowed-helper-functions-exist/ckan/config/routing.py"
               data-name="2632-check-allowed-helper-functions-exist"
               data-skip-pjax="true"
               rel="nofollow">
              <svg aria-hidden="true" class="octicon octicon-check select-menu-item-icon" height="16" version="1.1" viewBox="0 0 12 16" width="12"><path fill-rule="evenodd" d="M12 5l-8 8-4-4 1.5-1.5L4 10l6.5-6.5z"/></svg>
              <span class="select-menu-item-text css-truncate-target js-select-menu-filter-text">
                2632-check-allowed-helper-functions-exist
              </span>
            </a>
            <a class="select-menu-item js-navigation-item js-navigation-open "
               href="/ckan/ckan/blob/2634-changelog-update/ckan/config/routing.py"
               data-name="2634-changelog-update"
               data-skip-pjax="true"
               rel="nofollow">
              <svg aria-hidden="true" class="octicon octicon-check select-menu-item-icon" height="16" version="1.1" viewBox="0 0 12 16" width="12"><path fill-rule="evenodd" d="M12 5l-8 8-4-4 1.5-1.5L4 10l6.5-6.5z"/></svg>
              <span class="select-menu-item-text css-truncate-target js-select-menu-filter-text">
                2634-changelog-update
              </span>
            </a>
            <a class="select-menu-item js-navigation-item js-navigation-open "
               href="/ckan/ckan/blob/2636-fix-encoding-create-ext/ckan/config/routing.py"
               data-name="2636-fix-encoding-create-ext"
               data-skip-pjax="true"
               rel="nofollow">
              <svg aria-hidden="true" class="octicon octicon-check select-menu-item-icon" height="16" version="1.1" viewBox="0 0 12 16" width="12"><path fill-rule="evenodd" d="M12 5l-8 8-4-4 1.5-1.5L4 10l6.5-6.5z"/></svg>
              <span class="select-menu-item-text css-truncate-target js-select-menu-filter-text">
                2636-fix-encoding-create-ext
              </span>
            </a>
            <a class="select-menu-item js-navigation-item js-navigation-open "
               href="/ckan/ckan/blob/2639-update-recline-for-1.8-release/ckan/config/routing.py"
               data-name="2639-update-recline-for-1.8-release"
               data-skip-pjax="true"
               rel="nofollow">
              <svg aria-hidden="true" class="octicon octicon-check select-menu-item-icon" height="16" version="1.1" viewBox="0 0 12 16" width="12"><path fill-rule="evenodd" d="M12 5l-8 8-4-4 1.5-1.5L4 10l6.5-6.5z"/></svg>
              <span class="select-menu-item-text css-truncate-target js-select-menu-filter-text">
                2639-update-recline-for-1.8-release
              </span>
            </a>
            <a class="select-menu-item js-navigation-item js-navigation-open "
               href="/ckan/ckan/blob/2640-new-recline-on-demo/ckan/config/routing.py"
               data-name="2640-new-recline-on-demo"
               data-skip-pjax="true"
               rel="nofollow">
              <svg aria-hidden="true" class="octicon octicon-check select-menu-item-icon" height="16" version="1.1" viewBox="0 0 12 16" width="12"><path fill-rule="evenodd" d="M12 5l-8 8-4-4 1.5-1.5L4 10l6.5-6.5z"/></svg>
              <span class="select-menu-item-text css-truncate-target js-select-menu-filter-text">
                2640-new-recline-on-demo
              </span>
            </a>
            <a class="select-menu-item js-navigation-item js-navigation-open "
               href="/ckan/ckan/blob/2650-markdown-resource-description/ckan/config/routing.py"
               data-name="2650-markdown-resource-description"
               data-skip-pjax="true"
               rel="nofollow">
              <svg aria-hidden="true" class="octicon octicon-check select-menu-item-icon" height="16" version="1.1" viewBox="0 0 12 16" width="12"><path fill-rule="evenodd" d="M12 5l-8 8-4-4 1.5-1.5L4 10l6.5-6.5z"/></svg>
              <span class="select-menu-item-text css-truncate-target js-select-menu-filter-text">
                2650-markdown-resource-description
              </span>
            </a>
            <a class="select-menu-item js-navigation-item js-navigation-open "
               href="/ckan/ckan/blob/2651-rival-patch/ckan/config/routing.py"
               data-name="2651-rival-patch"
               data-skip-pjax="true"
               rel="nofollow">
              <svg aria-hidden="true" class="octicon octicon-check select-menu-item-icon" height="16" version="1.1" viewBox="0 0 12 16" width="12"><path fill-rule="evenodd" d="M12 5l-8 8-4-4 1.5-1.5L4 10l6.5-6.5z"/></svg>
              <span class="select-menu-item-text css-truncate-target js-select-menu-filter-text">
                2651-rival-patch
              </span>
            </a>
            <a class="select-menu-item js-navigation-item js-navigation-open "
               href="/ckan/ckan/blob/2651-tsv-preview-fails/ckan/config/routing.py"
               data-name="2651-tsv-preview-fails"
               data-skip-pjax="true"
               rel="nofollow">
              <svg aria-hidden="true" class="octicon octicon-check select-menu-item-icon" height="16" version="1.1" viewBox="0 0 12 16" width="12"><path fill-rule="evenodd" d="M12 5l-8 8-4-4 1.5-1.5L4 10l6.5-6.5z"/></svg>
              <span class="select-menu-item-text css-truncate-target js-select-menu-filter-text">
                2651-tsv-preview-fails
              </span>
            </a>
            <a class="select-menu-item js-navigation-item js-navigation-open "
               href="/ckan/ckan/blob/2664-tag-errors/ckan/config/routing.py"
               data-name="2664-tag-errors"
               data-skip-pjax="true"
               rel="nofollow">
              <svg aria-hidden="true" class="octicon octicon-check select-menu-item-icon" height="16" version="1.1" viewBox="0 0 12 16" width="12"><path fill-rule="evenodd" d="M12 5l-8 8-4-4 1.5-1.5L4 10l6.5-6.5z"/></svg>
              <span class="select-menu-item-text css-truncate-target js-select-menu-filter-text">
                2664-tag-errors
              </span>
            </a>
            <a class="select-menu-item js-navigation-item js-navigation-open "
               href="/ckan/ckan/blob/2667-edit-resource-form/ckan/config/routing.py"
               data-name="2667-edit-resource-form"
               data-skip-pjax="true"
               rel="nofollow">
              <svg aria-hidden="true" class="octicon octicon-check select-menu-item-icon" height="16" version="1.1" viewBox="0 0 12 16" width="12"><path fill-rule="evenodd" d="M12 5l-8 8-4-4 1.5-1.5L4 10l6.5-6.5z"/></svg>
              <span class="select-menu-item-text css-truncate-target js-select-menu-filter-text">
                2667-edit-resource-form
              </span>
            </a>
            <a class="select-menu-item js-navigation-item js-navigation-open "
               href="/ckan/ckan/blob/2670-get-children-groups-defect/ckan/config/routing.py"
               data-name="2670-get-children-groups-defect"
               data-skip-pjax="true"
               rel="nofollow">
              <svg aria-hidden="true" class="octicon octicon-check select-menu-item-icon" height="16" version="1.1" viewBox="0 0 12 16" width="12"><path fill-rule="evenodd" d="M12 5l-8 8-4-4 1.5-1.5L4 10l6.5-6.5z"/></svg>
              <span class="select-menu-item-text css-truncate-target js-select-menu-filter-text">
                2670-get-children-groups-defect
              </span>
            </a>
            <a class="select-menu-item js-navigation-item js-navigation-open "
               href="/ckan/ckan/blob/2671-fix-partial-updates/ckan/config/routing.py"
               data-name="2671-fix-partial-updates"
               data-skip-pjax="true"
               rel="nofollow">
              <svg aria-hidden="true" class="octicon octicon-check select-menu-item-icon" height="16" version="1.1" viewBox="0 0 12 16" width="12"><path fill-rule="evenodd" d="M12 5l-8 8-4-4 1.5-1.5L4 10l6.5-6.5z"/></svg>
              <span class="select-menu-item-text css-truncate-target js-select-menu-filter-text">
                2671-fix-partial-updates
              </span>
            </a>
            <a class="select-menu-item js-navigation-item js-navigation-open "
               href="/ckan/ckan/blob/2672-is_modifed-passive-should-be-true/ckan/config/routing.py"
               data-name="2672-is_modifed-passive-should-be-true"
               data-skip-pjax="true"
               rel="nofollow">
              <svg aria-hidden="true" class="octicon octicon-check select-menu-item-icon" height="16" version="1.1" viewBox="0 0 12 16" width="12"><path fill-rule="evenodd" d="M12 5l-8 8-4-4 1.5-1.5L4 10l6.5-6.5z"/></svg>
              <span class="select-menu-item-text css-truncate-target js-select-menu-filter-text">
                2672-is_modifed-passive-should-be-true
              </span>
            </a>
            <a class="select-menu-item js-navigation-item js-navigation-open "
               href="/ckan/ckan/blob/2673-deleting-routes/ckan/config/routing.py"
               data-name="2673-deleting-routes"
               data-skip-pjax="true"
               rel="nofollow">
              <svg aria-hidden="true" class="octicon octicon-check select-menu-item-icon" height="16" version="1.1" viewBox="0 0 12 16" width="12"><path fill-rule="evenodd" d="M12 5l-8 8-4-4 1.5-1.5L4 10l6.5-6.5z"/></svg>
              <span class="select-menu-item-text css-truncate-target js-select-menu-filter-text">
                2673-deleting-routes
              </span>
            </a>
            <a class="select-menu-item js-navigation-item js-navigation-open "
               href="/ckan/ckan/blob/2678-core-multilingual-fields/ckan/config/routing.py"
               data-name="2678-core-multilingual-fields"
               data-skip-pjax="true"
               rel="nofollow">
              <svg aria-hidden="true" class="octicon octicon-check select-menu-item-icon" height="16" version="1.1" viewBox="0 0 12 16" width="12"><path fill-rule="evenodd" d="M12 5l-8 8-4-4 1.5-1.5L4 10l6.5-6.5z"/></svg>
              <span class="select-menu-item-text css-truncate-target js-select-menu-filter-text">
                2678-core-multilingual-fields
              </span>
            </a>
            <a class="select-menu-item js-navigation-item js-navigation-open "
               href="/ckan/ckan/blob/2681-lazy-json/ckan/config/routing.py"
               data-name="2681-lazy-json"
               data-skip-pjax="true"
               rel="nofollow">
              <svg aria-hidden="true" class="octicon octicon-check select-menu-item-icon" height="16" version="1.1" viewBox="0 0 12 16" width="12"><path fill-rule="evenodd" d="M12 5l-8 8-4-4 1.5-1.5L4 10l6.5-6.5z"/></svg>
              <span class="select-menu-item-text css-truncate-target js-select-menu-filter-text">
                2681-lazy-json
              </span>
            </a>
            <a class="select-menu-item js-navigation-item js-navigation-open "
               href="/ckan/ckan/blob/2682-bug-tracking-double-counting/ckan/config/routing.py"
               data-name="2682-bug-tracking-double-counting"
               data-skip-pjax="true"
               rel="nofollow">
              <svg aria-hidden="true" class="octicon octicon-check select-menu-item-icon" height="16" version="1.1" viewBox="0 0 12 16" width="12"><path fill-rule="evenodd" d="M12 5l-8 8-4-4 1.5-1.5L4 10l6.5-6.5z"/></svg>
              <span class="select-menu-item-text css-truncate-target js-select-menu-filter-text">
                2682-bug-tracking-double-counting
              </span>
            </a>
            <a class="select-menu-item js-navigation-item js-navigation-open "
               href="/ckan/ckan/blob/2688-sorting-for-groups/ckan/config/routing.py"
               data-name="2688-sorting-for-groups"
               data-skip-pjax="true"
               rel="nofollow">
              <svg aria-hidden="true" class="octicon octicon-check select-menu-item-icon" height="16" version="1.1" viewBox="0 0 12 16" width="12"><path fill-rule="evenodd" d="M12 5l-8 8-4-4 1.5-1.5L4 10l6.5-6.5z"/></svg>
              <span class="select-menu-item-text css-truncate-target js-select-menu-filter-text">
                2688-sorting-for-groups
              </span>
            </a>
            <a class="select-menu-item js-navigation-item js-navigation-open "
               href="/ckan/ckan/blob/2710-nicer-api-page/ckan/config/routing.py"
               data-name="2710-nicer-api-page"
               data-skip-pjax="true"
               rel="nofollow">
              <svg aria-hidden="true" class="octicon octicon-check select-menu-item-icon" height="16" version="1.1" viewBox="0 0 12 16" width="12"><path fill-rule="evenodd" d="M12 5l-8 8-4-4 1.5-1.5L4 10l6.5-6.5z"/></svg>
              <span class="select-menu-item-text css-truncate-target js-select-menu-filter-text">
                2710-nicer-api-page
              </span>
            </a>
            <a class="select-menu-item js-navigation-item js-navigation-open "
               href="/ckan/ckan/blob/2732-file-upload-refactor/ckan/config/routing.py"
               data-name="2732-file-upload-refactor"
               data-skip-pjax="true"
               rel="nofollow">
              <svg aria-hidden="true" class="octicon octicon-check select-menu-item-icon" height="16" version="1.1" viewBox="0 0 12 16" width="12"><path fill-rule="evenodd" d="M12 5l-8 8-4-4 1.5-1.5L4 10l6.5-6.5z"/></svg>
              <span class="select-menu-item-text css-truncate-target js-select-menu-filter-text">
                2732-file-upload-refactor
              </span>
            </a>
            <a class="select-menu-item js-navigation-item js-navigation-open "
               href="/ckan/ckan/blob/2733-feature-datastore/ckan/config/routing.py"
               data-name="2733-feature-datastore"
               data-skip-pjax="true"
               rel="nofollow">
              <svg aria-hidden="true" class="octicon octicon-check select-menu-item-icon" height="16" version="1.1" viewBox="0 0 12 16" width="12"><path fill-rule="evenodd" d="M12 5l-8 8-4-4 1.5-1.5L4 10l6.5-6.5z"/></svg>
              <span class="select-menu-item-text css-truncate-target js-select-menu-filter-text">
                2733-feature-datastore
              </span>
            </a>
            <a class="select-menu-item js-navigation-item js-navigation-open "
               href="/ckan/ckan/blob/2735-metadata-created-as-field/ckan/config/routing.py"
               data-name="2735-metadata-created-as-field"
               data-skip-pjax="true"
               rel="nofollow">
              <svg aria-hidden="true" class="octicon octicon-check select-menu-item-icon" height="16" version="1.1" viewBox="0 0 12 16" width="12"><path fill-rule="evenodd" d="M12 5l-8 8-4-4 1.5-1.5L4 10l6.5-6.5z"/></svg>
              <span class="select-menu-item-text css-truncate-target js-select-menu-filter-text">
                2735-metadata-created-as-field
              </span>
            </a>
            <a class="select-menu-item js-navigation-item js-navigation-open "
               href="/ckan/ckan/blob/2736-bad-merge-check-po-files/ckan/config/routing.py"
               data-name="2736-bad-merge-check-po-files"
               data-skip-pjax="true"
               rel="nofollow">
              <svg aria-hidden="true" class="octicon octicon-check select-menu-item-icon" height="16" version="1.1" viewBox="0 0 12 16" width="12"><path fill-rule="evenodd" d="M12 5l-8 8-4-4 1.5-1.5L4 10l6.5-6.5z"/></svg>
              <span class="select-menu-item-text css-truncate-target js-select-menu-filter-text">
                2736-bad-merge-check-po-files
              </span>
            </a>
            <a class="select-menu-item js-navigation-item js-navigation-open "
               href="/ckan/ckan/blob/2741-admin-index-within-new-demo/ckan/config/routing.py"
               data-name="2741-admin-index-within-new-demo"
               data-skip-pjax="true"
               rel="nofollow">
              <svg aria-hidden="true" class="octicon octicon-check select-menu-item-icon" height="16" version="1.1" viewBox="0 0 12 16" width="12"><path fill-rule="evenodd" d="M12 5l-8 8-4-4 1.5-1.5L4 10l6.5-6.5z"/></svg>
              <span class="select-menu-item-text css-truncate-target js-select-menu-filter-text">
                2741-admin-index-within-new-demo
              </span>
            </a>
            <a class="select-menu-item js-navigation-item js-navigation-open "
               href="/ckan/ckan/blob/2741-remove-rdf-cruft/ckan/config/routing.py"
               data-name="2741-remove-rdf-cruft"
               data-skip-pjax="true"
               rel="nofollow">
              <svg aria-hidden="true" class="octicon octicon-check select-menu-item-icon" height="16" version="1.1" viewBox="0 0 12 16" width="12"><path fill-rule="evenodd" d="M12 5l-8 8-4-4 1.5-1.5L4 10l6.5-6.5z"/></svg>
              <span class="select-menu-item-text css-truncate-target js-select-menu-filter-text">
                2741-remove-rdf-cruft
              </span>
            </a>
            <a class="select-menu-item js-navigation-item js-navigation-open "
               href="/ckan/ckan/blob/2750-add-docs-and-examples-for-idatasetform-and-igroupform/ckan/config/routing.py"
               data-name="2750-add-docs-and-examples-for-idatasetform-and-igroupform"
               data-skip-pjax="true"
               rel="nofollow">
              <svg aria-hidden="true" class="octicon octicon-check select-menu-item-icon" height="16" version="1.1" viewBox="0 0 12 16" width="12"><path fill-rule="evenodd" d="M12 5l-8 8-4-4 1.5-1.5L4 10l6.5-6.5z"/></svg>
              <span class="select-menu-item-text css-truncate-target js-select-menu-filter-text">
                2750-add-docs-and-examples-for-idatasetform-and-igroupform
              </span>
            </a>
            <a class="select-menu-item js-navigation-item js-navigation-open "
               href="/ckan/ckan/blob/2755-slow-user-pages/ckan/config/routing.py"
               data-name="2755-slow-user-pages"
               data-skip-pjax="true"
               rel="nofollow">
              <svg aria-hidden="true" class="octicon octicon-check select-menu-item-icon" height="16" version="1.1" viewBox="0 0 12 16" width="12"><path fill-rule="evenodd" d="M12 5l-8 8-4-4 1.5-1.5L4 10l6.5-6.5z"/></svg>
              <span class="select-menu-item-text css-truncate-target js-select-menu-filter-text">
                2755-slow-user-pages
              </span>
            </a>
            <a class="select-menu-item js-navigation-item js-navigation-open "
               href="/ckan/ckan/blob/2757-source-install-upgrade-docs/ckan/config/routing.py"
               data-name="2757-source-install-upgrade-docs"
               data-skip-pjax="true"
               rel="nofollow">
              <svg aria-hidden="true" class="octicon octicon-check select-menu-item-icon" height="16" version="1.1" viewBox="0 0 12 16" width="12"><path fill-rule="evenodd" d="M12 5l-8 8-4-4 1.5-1.5L4 10l6.5-6.5z"/></svg>
              <span class="select-menu-item-text css-truncate-target js-select-menu-filter-text">
                2757-source-install-upgrade-docs
              </span>
            </a>
            <a class="select-menu-item js-navigation-item js-navigation-open "
               href="/ckan/ckan/blob/2770-fanstatic-error-pages/ckan/config/routing.py"
               data-name="2770-fanstatic-error-pages"
               data-skip-pjax="true"
               rel="nofollow">
              <svg aria-hidden="true" class="octicon octicon-check select-menu-item-icon" height="16" version="1.1" viewBox="0 0 12 16" width="12"><path fill-rule="evenodd" d="M12 5l-8 8-4-4 1.5-1.5L4 10l6.5-6.5z"/></svg>
              <span class="select-menu-item-text css-truncate-target js-select-menu-filter-text">
                2770-fanstatic-error-pages
              </span>
            </a>
            <a class="select-menu-item js-navigation-item js-navigation-open "
               href="/ckan/ckan/blob/2772-remove-less/ckan/config/routing.py"
               data-name="2772-remove-less"
               data-skip-pjax="true"
               rel="nofollow">
              <svg aria-hidden="true" class="octicon octicon-check select-menu-item-icon" height="16" version="1.1" viewBox="0 0 12 16" width="12"><path fill-rule="evenodd" d="M12 5l-8 8-4-4 1.5-1.5L4 10l6.5-6.5z"/></svg>
              <span class="select-menu-item-text css-truncate-target js-select-menu-filter-text">
                2772-remove-less
              </span>
            </a>
            <a class="select-menu-item js-navigation-item js-navigation-open "
               href="/ckan/ckan/blob/2777-defect-user-show/ckan/config/routing.py"
               data-name="2777-defect-user-show"
               data-skip-pjax="true"
               rel="nofollow">
              <svg aria-hidden="true" class="octicon octicon-check select-menu-item-icon" height="16" version="1.1" viewBox="0 0 12 16" width="12"><path fill-rule="evenodd" d="M12 5l-8 8-4-4 1.5-1.5L4 10l6.5-6.5z"/></svg>
              <span class="select-menu-item-text css-truncate-target js-select-menu-filter-text">
                2777-defect-user-show
              </span>
            </a>
            <a class="select-menu-item js-navigation-item js-navigation-open "
               href="/ckan/ckan/blob/2783-improve-ext-trans-docs/ckan/config/routing.py"
               data-name="2783-improve-ext-trans-docs"
               data-skip-pjax="true"
               rel="nofollow">
              <svg aria-hidden="true" class="octicon octicon-check select-menu-item-icon" height="16" version="1.1" viewBox="0 0 12 16" width="12"><path fill-rule="evenodd" d="M12 5l-8 8-4-4 1.5-1.5L4 10l6.5-6.5z"/></svg>
              <span class="select-menu-item-text css-truncate-target js-select-menu-filter-text">
                2783-improve-ext-trans-docs
              </span>
            </a>
            <a class="select-menu-item js-navigation-item js-navigation-open "
               href="/ckan/ckan/blob/2784-migrations-for-extensions/ckan/config/routing.py"
               data-name="2784-migrations-for-extensions"
               data-skip-pjax="true"
               rel="nofollow">
              <svg aria-hidden="true" class="octicon octicon-check select-menu-item-icon" height="16" version="1.1" viewBox="0 0 12 16" width="12"><path fill-rule="evenodd" d="M12 5l-8 8-4-4 1.5-1.5L4 10l6.5-6.5z"/></svg>
              <span class="select-menu-item-text css-truncate-target js-select-menu-filter-text">
                2784-migrations-for-extensions
              </span>
            </a>
            <a class="select-menu-item js-navigation-item js-navigation-open "
               href="/ckan/ckan/blob/2784-model-dictize-sensitive-data/ckan/config/routing.py"
               data-name="2784-model-dictize-sensitive-data"
               data-skip-pjax="true"
               rel="nofollow">
              <svg aria-hidden="true" class="octicon octicon-check select-menu-item-icon" height="16" version="1.1" viewBox="0 0 12 16" width="12"><path fill-rule="evenodd" d="M12 5l-8 8-4-4 1.5-1.5L4 10l6.5-6.5z"/></svg>
              <span class="select-menu-item-text css-truncate-target js-select-menu-filter-text">
                2784-model-dictize-sensitive-data
              </span>
            </a>
            <a class="select-menu-item js-navigation-item js-navigation-open "
               href="/ckan/ckan/blob/2788-speed-improvements/ckan/config/routing.py"
               data-name="2788-speed-improvements"
               data-skip-pjax="true"
               rel="nofollow">
              <svg aria-hidden="true" class="octicon octicon-check select-menu-item-icon" height="16" version="1.1" viewBox="0 0 12 16" width="12"><path fill-rule="evenodd" d="M12 5l-8 8-4-4 1.5-1.5L4 10l6.5-6.5z"/></svg>
              <span class="select-menu-item-text css-truncate-target js-select-menu-filter-text">
                2788-speed-improvements
              </span>
            </a>
            <a class="select-menu-item js-navigation-item js-navigation-open "
               href="/ckan/ckan/blob/2795-coveralls-requirement/ckan/config/routing.py"
               data-name="2795-coveralls-requirement"
               data-skip-pjax="true"
               rel="nofollow">
              <svg aria-hidden="true" class="octicon octicon-check select-menu-item-icon" height="16" version="1.1" viewBox="0 0 12 16" width="12"><path fill-rule="evenodd" d="M12 5l-8 8-4-4 1.5-1.5L4 10l6.5-6.5z"/></svg>
              <span class="select-menu-item-text css-truncate-target js-select-menu-filter-text">
                2795-coveralls-requirement
              </span>
            </a>
            <a class="select-menu-item js-navigation-item js-navigation-open "
               href="/ckan/ckan/blob/2802-fix-assert/ckan/config/routing.py"
               data-name="2802-fix-assert"
               data-skip-pjax="true"
               rel="nofollow">
              <svg aria-hidden="true" class="octicon octicon-check select-menu-item-icon" height="16" version="1.1" viewBox="0 0 12 16" width="12"><path fill-rule="evenodd" d="M12 5l-8 8-4-4 1.5-1.5L4 10l6.5-6.5z"/></svg>
              <span class="select-menu-item-text css-truncate-target js-select-menu-filter-text">
                2802-fix-assert
              </span>
            </a>
            <a class="select-menu-item js-navigation-item js-navigation-open "
               href="/ckan/ckan/blob/2805-show-404-for-deleted-datasets/ckan/config/routing.py"
               data-name="2805-show-404-for-deleted-datasets"
               data-skip-pjax="true"
               rel="nofollow">
              <svg aria-hidden="true" class="octicon octicon-check select-menu-item-icon" height="16" version="1.1" viewBox="0 0 12 16" width="12"><path fill-rule="evenodd" d="M12 5l-8 8-4-4 1.5-1.5L4 10l6.5-6.5z"/></svg>
              <span class="select-menu-item-text css-truncate-target js-select-menu-filter-text">
                2805-show-404-for-deleted-datasets
              </span>
            </a>
            <a class="select-menu-item js-navigation-item js-navigation-open "
               href="/ckan/ckan/blob/2811-bug-dataset-author-and-maintainer-email-links/ckan/config/routing.py"
               data-name="2811-bug-dataset-author-and-maintainer-email-links"
               data-skip-pjax="true"
               rel="nofollow">
              <svg aria-hidden="true" class="octicon octicon-check select-menu-item-icon" height="16" version="1.1" viewBox="0 0 12 16" width="12"><path fill-rule="evenodd" d="M12 5l-8 8-4-4 1.5-1.5L4 10l6.5-6.5z"/></svg>
              <span class="select-menu-item-text css-truncate-target js-select-menu-filter-text">
                2811-bug-dataset-author-and-maintainer-email-links
              </span>
            </a>
            <a class="select-menu-item js-navigation-item js-navigation-open "
               href="/ckan/ckan/blob/2815-defect-db-to-form-package-schema-strips-tracking-summary-and-is-open/ckan/config/routing.py"
               data-name="2815-defect-db-to-form-package-schema-strips-tracking-summary-and-is-open"
               data-skip-pjax="true"
               rel="nofollow">
              <svg aria-hidden="true" class="octicon octicon-check select-menu-item-icon" height="16" version="1.1" viewBox="0 0 12 16" width="12"><path fill-rule="evenodd" d="M12 5l-8 8-4-4 1.5-1.5L4 10l6.5-6.5z"/></svg>
              <span class="select-menu-item-text css-truncate-target js-select-menu-filter-text">
                2815-defect-db-to-form-package-schema-strips-tracking-summary-and-is-open
              </span>
            </a>
            <a class="select-menu-item js-navigation-item js-navigation-open "
               href="/ckan/ckan/blob/2816-re-add-model-bits/ckan/config/routing.py"
               data-name="2816-re-add-model-bits"
               data-skip-pjax="true"
               rel="nofollow">
              <svg aria-hidden="true" class="octicon octicon-check select-menu-item-icon" height="16" version="1.1" viewBox="0 0 12 16" width="12"><path fill-rule="evenodd" d="M12 5l-8 8-4-4 1.5-1.5L4 10l6.5-6.5z"/></svg>
              <span class="select-menu-item-text css-truncate-target js-select-menu-filter-text">
                2816-re-add-model-bits
              </span>
            </a>
            <a class="select-menu-item js-navigation-item js-navigation-open "
               href="/ckan/ckan/blob/2823-use-sqlalchemy-cache-for-more-objects/ckan/config/routing.py"
               data-name="2823-use-sqlalchemy-cache-for-more-objects"
               data-skip-pjax="true"
               rel="nofollow">
              <svg aria-hidden="true" class="octicon octicon-check select-menu-item-icon" height="16" version="1.1" viewBox="0 0 12 16" width="12"><path fill-rule="evenodd" d="M12 5l-8 8-4-4 1.5-1.5L4 10l6.5-6.5z"/></svg>
              <span class="select-menu-item-text css-truncate-target js-select-menu-filter-text">
                2823-use-sqlalchemy-cache-for-more-objects
              </span>
            </a>
            <a class="select-menu-item js-navigation-item js-navigation-open "
               href="/ckan/ckan/blob/2833-remove-genshi/ckan/config/routing.py"
               data-name="2833-remove-genshi"
               data-skip-pjax="true"
               rel="nofollow">
              <svg aria-hidden="true" class="octicon octicon-check select-menu-item-icon" height="16" version="1.1" viewBox="0 0 12 16" width="12"><path fill-rule="evenodd" d="M12 5l-8 8-4-4 1.5-1.5L4 10l6.5-6.5z"/></svg>
              <span class="select-menu-item-text css-truncate-target js-select-menu-filter-text">
                2833-remove-genshi
              </span>
            </a>
            <a class="select-menu-item js-navigation-item js-navigation-open "
               href="/ckan/ckan/blob/2843-cannot-add-existing-datasets-to-organizations/ckan/config/routing.py"
               data-name="2843-cannot-add-existing-datasets-to-organizations"
               data-skip-pjax="true"
               rel="nofollow">
              <svg aria-hidden="true" class="octicon octicon-check select-menu-item-icon" height="16" version="1.1" viewBox="0 0 12 16" width="12"><path fill-rule="evenodd" d="M12 5l-8 8-4-4 1.5-1.5L4 10l6.5-6.5z"/></svg>
              <span class="select-menu-item-text css-truncate-target js-select-menu-filter-text">
                2843-cannot-add-existing-datasets-to-organizations
              </span>
            </a>
            <a class="select-menu-item js-navigation-item js-navigation-open "
               href="/ckan/ckan/blob/2844-optional-resource-url/ckan/config/routing.py"
               data-name="2844-optional-resource-url"
               data-skip-pjax="true"
               rel="nofollow">
              <svg aria-hidden="true" class="octicon octicon-check select-menu-item-icon" height="16" version="1.1" viewBox="0 0 12 16" width="12"><path fill-rule="evenodd" d="M12 5l-8 8-4-4 1.5-1.5L4 10l6.5-6.5z"/></svg>
              <span class="select-menu-item-text css-truncate-target js-select-menu-filter-text">
                2844-optional-resource-url
              </span>
            </a>
            <a class="select-menu-item js-navigation-item js-navigation-open "
               href="/ckan/ckan/blob/2844-re-enable-simple-search-for-1.8/ckan/config/routing.py"
               data-name="2844-re-enable-simple-search-for-1.8"
               data-skip-pjax="true"
               rel="nofollow">
              <svg aria-hidden="true" class="octicon octicon-check select-menu-item-icon" height="16" version="1.1" viewBox="0 0 12 16" width="12"><path fill-rule="evenodd" d="M12 5l-8 8-4-4 1.5-1.5L4 10l6.5-6.5z"/></svg>
              <span class="select-menu-item-text css-truncate-target js-select-menu-filter-text">
                2844-re-enable-simple-search-for-1.8
              </span>
            </a>
            <a class="select-menu-item js-navigation-item js-navigation-open "
               href="/ckan/ckan/blob/2844-re-enable-simple-search/ckan/config/routing.py"
               data-name="2844-re-enable-simple-search"
               data-skip-pjax="true"
               rel="nofollow">
              <svg aria-hidden="true" class="octicon octicon-check select-menu-item-icon" height="16" version="1.1" viewBox="0 0 12 16" width="12"><path fill-rule="evenodd" d="M12 5l-8 8-4-4 1.5-1.5L4 10l6.5-6.5z"/></svg>
              <span class="select-menu-item-text css-truncate-target js-select-menu-filter-text">
                2844-re-enable-simple-search
              </span>
            </a>
            <a class="select-menu-item js-navigation-item js-navigation-open "
               href="/ckan/ckan/blob/2844-sql-only-no-solr/ckan/config/routing.py"
               data-name="2844-sql-only-no-solr"
               data-skip-pjax="true"
               rel="nofollow">
              <svg aria-hidden="true" class="octicon octicon-check select-menu-item-icon" height="16" version="1.1" viewBox="0 0 12 16" width="12"><path fill-rule="evenodd" d="M12 5l-8 8-4-4 1.5-1.5L4 10l6.5-6.5z"/></svg>
              <span class="select-menu-item-text css-truncate-target js-select-menu-filter-text">
                2844-sql-only-no-solr
              </span>
            </a>
            <a class="select-menu-item js-navigation-item js-navigation-open "
               href="/ckan/ckan/blob/2845-bug-editing-organization-removes-datasets/ckan/config/routing.py"
               data-name="2845-bug-editing-organization-removes-datasets"
               data-skip-pjax="true"
               rel="nofollow">
              <svg aria-hidden="true" class="octicon octicon-check select-menu-item-icon" height="16" version="1.1" viewBox="0 0 12 16" width="12"><path fill-rule="evenodd" d="M12 5l-8 8-4-4 1.5-1.5L4 10l6.5-6.5z"/></svg>
              <span class="select-menu-item-text css-truncate-target js-select-menu-filter-text">
                2845-bug-editing-organization-removes-datasets
              </span>
            </a>
            <a class="select-menu-item js-navigation-item js-navigation-open "
               href="/ckan/ckan/blob/2848-fix-default-schema-on-package_search/ckan/config/routing.py"
               data-name="2848-fix-default-schema-on-package_search"
               data-skip-pjax="true"
               rel="nofollow">
              <svg aria-hidden="true" class="octicon octicon-check select-menu-item-icon" height="16" version="1.1" viewBox="0 0 12 16" width="12"><path fill-rule="evenodd" d="M12 5l-8 8-4-4 1.5-1.5L4 10l6.5-6.5z"/></svg>
              <span class="select-menu-item-text css-truncate-target js-select-menu-filter-text">
                2848-fix-default-schema-on-package_search
              </span>
            </a>
            <a class="select-menu-item js-navigation-item js-navigation-open "
               href="/ckan/ckan/blob/2852-ensure-grouptype-used/ckan/config/routing.py"
               data-name="2852-ensure-grouptype-used"
               data-skip-pjax="true"
               rel="nofollow">
              <svg aria-hidden="true" class="octicon octicon-check select-menu-item-icon" height="16" version="1.1" viewBox="0 0 12 16" width="12"><path fill-rule="evenodd" d="M12 5l-8 8-4-4 1.5-1.5L4 10l6.5-6.5z"/></svg>
              <span class="select-menu-item-text css-truncate-target js-select-menu-filter-text">
                2852-ensure-grouptype-used
              </span>
            </a>
            <a class="select-menu-item js-navigation-item js-navigation-open "
               href="/ckan/ckan/blob/2856-related-controller-fix/ckan/config/routing.py"
               data-name="2856-related-controller-fix"
               data-skip-pjax="true"
               rel="nofollow">
              <svg aria-hidden="true" class="octicon octicon-check select-menu-item-icon" height="16" version="1.1" viewBox="0 0 12 16" width="12"><path fill-rule="evenodd" d="M12 5l-8 8-4-4 1.5-1.5L4 10l6.5-6.5z"/></svg>
              <span class="select-menu-item-text css-truncate-target js-select-menu-filter-text">
                2856-related-controller-fix
              </span>
            </a>
            <a class="select-menu-item js-navigation-item js-navigation-open "
               href="/ckan/ckan/blob/2859-fix-the-build/ckan/config/routing.py"
               data-name="2859-fix-the-build"
               data-skip-pjax="true"
               rel="nofollow">
              <svg aria-hidden="true" class="octicon octicon-check select-menu-item-icon" height="16" version="1.1" viewBox="0 0 12 16" width="12"><path fill-rule="evenodd" d="M12 5l-8 8-4-4 1.5-1.5L4 10l6.5-6.5z"/></svg>
              <span class="select-menu-item-text css-truncate-target js-select-menu-filter-text">
                2859-fix-the-build
              </span>
            </a>
            <a class="select-menu-item js-navigation-item js-navigation-open "
               href="/ckan/ckan/blob/2866-missing-reset-key/ckan/config/routing.py"
               data-name="2866-missing-reset-key"
               data-skip-pjax="true"
               rel="nofollow">
              <svg aria-hidden="true" class="octicon octicon-check select-menu-item-icon" height="16" version="1.1" viewBox="0 0 12 16" width="12"><path fill-rule="evenodd" d="M12 5l-8 8-4-4 1.5-1.5L4 10l6.5-6.5z"/></svg>
              <span class="select-menu-item-text css-truncate-target js-select-menu-filter-text">
                2866-missing-reset-key
              </span>
            </a>
            <a class="select-menu-item js-navigation-item js-navigation-open "
               href="/ckan/ckan/blob/2867-unicode-error-url-for/ckan/config/routing.py"
               data-name="2867-unicode-error-url-for"
               data-skip-pjax="true"
               rel="nofollow">
              <svg aria-hidden="true" class="octicon octicon-check select-menu-item-icon" height="16" version="1.1" viewBox="0 0 12 16" width="12"><path fill-rule="evenodd" d="M12 5l-8 8-4-4 1.5-1.5L4 10l6.5-6.5z"/></svg>
              <span class="select-menu-item-text css-truncate-target js-select-menu-filter-text">
                2867-unicode-error-url-for
              </span>
            </a>
            <a class="select-menu-item js-navigation-item js-navigation-open "
               href="/ckan/ckan/blob/2868-feed-search-error/ckan/config/routing.py"
               data-name="2868-feed-search-error"
               data-skip-pjax="true"
               rel="nofollow">
              <svg aria-hidden="true" class="octicon octicon-check select-menu-item-icon" height="16" version="1.1" viewBox="0 0 12 16" width="12"><path fill-rule="evenodd" d="M12 5l-8 8-4-4 1.5-1.5L4 10l6.5-6.5z"/></svg>
              <span class="select-menu-item-text css-truncate-target js-select-menu-filter-text">
                2868-feed-search-error
              </span>
            </a>
            <a class="select-menu-item js-navigation-item js-navigation-open "
               href="/ckan/ckan/blob/2872-bug-non-open-licenses-marked-as-open/ckan/config/routing.py"
               data-name="2872-bug-non-open-licenses-marked-as-open"
               data-skip-pjax="true"
               rel="nofollow">
              <svg aria-hidden="true" class="octicon octicon-check select-menu-item-icon" height="16" version="1.1" viewBox="0 0 12 16" width="12"><path fill-rule="evenodd" d="M12 5l-8 8-4-4 1.5-1.5L4 10l6.5-6.5z"/></svg>
              <span class="select-menu-item-text css-truncate-target js-select-menu-filter-text">
                2872-bug-non-open-licenses-marked-as-open
              </span>
            </a>
            <a class="select-menu-item js-navigation-item js-navigation-open "
               href="/ckan/ckan/blob/2878-org-roles-permissions/ckan/config/routing.py"
               data-name="2878-org-roles-permissions"
               data-skip-pjax="true"
               rel="nofollow">
              <svg aria-hidden="true" class="octicon octicon-check select-menu-item-icon" height="16" version="1.1" viewBox="0 0 12 16" width="12"><path fill-rule="evenodd" d="M12 5l-8 8-4-4 1.5-1.5L4 10l6.5-6.5z"/></svg>
              <span class="select-menu-item-text css-truncate-target js-select-menu-filter-text">
                2878-org-roles-permissions
              </span>
            </a>
            <a class="select-menu-item js-navigation-item js-navigation-open "
               href="/ckan/ckan/blob/2879-private-datasets/ckan/config/routing.py"
               data-name="2879-private-datasets"
               data-skip-pjax="true"
               rel="nofollow">
              <svg aria-hidden="true" class="octicon octicon-check select-menu-item-icon" height="16" version="1.1" viewBox="0 0 12 16" width="12"><path fill-rule="evenodd" d="M12 5l-8 8-4-4 1.5-1.5L4 10l6.5-6.5z"/></svg>
              <span class="select-menu-item-text css-truncate-target js-select-menu-filter-text">
                2879-private-datasets
              </span>
            </a>
            <a class="select-menu-item js-navigation-item js-navigation-open "
               href="/ckan/ckan/blob/2879-remove-lib-dumper/ckan/config/routing.py"
               data-name="2879-remove-lib-dumper"
               data-skip-pjax="true"
               rel="nofollow">
              <svg aria-hidden="true" class="octicon octicon-check select-menu-item-icon" height="16" version="1.1" viewBox="0 0 12 16" width="12"><path fill-rule="evenodd" d="M12 5l-8 8-4-4 1.5-1.5L4 10l6.5-6.5z"/></svg>
              <span class="select-menu-item-text css-truncate-target js-select-menu-filter-text">
                2879-remove-lib-dumper
              </span>
            </a>
            <a class="select-menu-item js-navigation-item js-navigation-open "
               href="/ckan/ckan/blob/2888-datapreview-iframe/ckan/config/routing.py"
               data-name="2888-datapreview-iframe"
               data-skip-pjax="true"
               rel="nofollow">
              <svg aria-hidden="true" class="octicon octicon-check select-menu-item-icon" height="16" version="1.1" viewBox="0 0 12 16" width="12"><path fill-rule="evenodd" d="M12 5l-8 8-4-4 1.5-1.5L4 10l6.5-6.5z"/></svg>
              <span class="select-menu-item-text css-truncate-target js-select-menu-filter-text">
                2888-datapreview-iframe
              </span>
            </a>
            <a class="select-menu-item js-navigation-item js-navigation-open "
               href="/ckan/ckan/blob/2911-internal-doc-of-org-group-auth/ckan/config/routing.py"
               data-name="2911-internal-doc-of-org-group-auth"
               data-skip-pjax="true"
               rel="nofollow">
              <svg aria-hidden="true" class="octicon octicon-check select-menu-item-icon" height="16" version="1.1" viewBox="0 0 12 16" width="12"><path fill-rule="evenodd" d="M12 5l-8 8-4-4 1.5-1.5L4 10l6.5-6.5z"/></svg>
              <span class="select-menu-item-text css-truncate-target js-select-menu-filter-text">
                2911-internal-doc-of-org-group-auth
              </span>
            </a>
            <a class="select-menu-item js-navigation-item js-navigation-open "
               href="/ckan/ckan/blob/2919-domain-object-count/ckan/config/routing.py"
               data-name="2919-domain-object-count"
               data-skip-pjax="true"
               rel="nofollow">
              <svg aria-hidden="true" class="octicon octicon-check select-menu-item-icon" height="16" version="1.1" viewBox="0 0 12 16" width="12"><path fill-rule="evenodd" d="M12 5l-8 8-4-4 1.5-1.5L4 10l6.5-6.5z"/></svg>
              <span class="select-menu-item-text css-truncate-target js-select-menu-filter-text">
                2919-domain-object-count
              </span>
            </a>
            <a class="select-menu-item js-navigation-item js-navigation-open "
               href="/ckan/ckan/blob/2920-duplicate-validator-func/ckan/config/routing.py"
               data-name="2920-duplicate-validator-func"
               data-skip-pjax="true"
               rel="nofollow">
              <svg aria-hidden="true" class="octicon octicon-check select-menu-item-icon" height="16" version="1.1" viewBox="0 0 12 16" width="12"><path fill-rule="evenodd" d="M12 5l-8 8-4-4 1.5-1.5L4 10l6.5-6.5z"/></svg>
              <span class="select-menu-item-text css-truncate-target js-select-menu-filter-text">
                2920-duplicate-validator-func
              </span>
            </a>
            <a class="select-menu-item js-navigation-item js-navigation-open "
               href="/ckan/ckan/blob/2923-recline-headers/ckan/config/routing.py"
               data-name="2923-recline-headers"
               data-skip-pjax="true"
               rel="nofollow">
              <svg aria-hidden="true" class="octicon octicon-check select-menu-item-icon" height="16" version="1.1" viewBox="0 0 12 16" width="12"><path fill-rule="evenodd" d="M12 5l-8 8-4-4 1.5-1.5L4 10l6.5-6.5z"/></svg>
              <span class="select-menu-item-text css-truncate-target js-select-menu-filter-text">
                2923-recline-headers
              </span>
            </a>
            <a class="select-menu-item js-navigation-item js-navigation-open "
               href="/ckan/ckan/blob/2935-data-viewer-new-datastore/ckan/config/routing.py"
               data-name="2935-data-viewer-new-datastore"
               data-skip-pjax="true"
               rel="nofollow">
              <svg aria-hidden="true" class="octicon octicon-check select-menu-item-icon" height="16" version="1.1" viewBox="0 0 12 16" width="12"><path fill-rule="evenodd" d="M12 5l-8 8-4-4 1.5-1.5L4 10l6.5-6.5z"/></svg>
              <span class="select-menu-item-text css-truncate-target js-select-menu-filter-text">
                2935-data-viewer-new-datastore
              </span>
            </a>
            <a class="select-menu-item js-navigation-item js-navigation-open "
               href="/ckan/ckan/blob/2939-orgs/ckan/config/routing.py"
               data-name="2939-orgs"
               data-skip-pjax="true"
               rel="nofollow">
              <svg aria-hidden="true" class="octicon octicon-check select-menu-item-icon" height="16" version="1.1" viewBox="0 0 12 16" width="12"><path fill-rule="evenodd" d="M12 5l-8 8-4-4 1.5-1.5L4 10l6.5-6.5z"/></svg>
              <span class="select-menu-item-text css-truncate-target js-select-menu-filter-text">
                2939-orgs
              </span>
            </a>
            <a class="select-menu-item js-navigation-item js-navigation-open "
               href="/ckan/ckan/blob/2941-follower-support/ckan/config/routing.py"
               data-name="2941-follower-support"
               data-skip-pjax="true"
               rel="nofollow">
              <svg aria-hidden="true" class="octicon octicon-check select-menu-item-icon" height="16" version="1.1" viewBox="0 0 12 16" width="12"><path fill-rule="evenodd" d="M12 5l-8 8-4-4 1.5-1.5L4 10l6.5-6.5z"/></svg>
              <span class="select-menu-item-text css-truncate-target js-select-menu-filter-text">
                2941-follower-support
              </span>
            </a>
            <a class="select-menu-item js-navigation-item js-navigation-open "
               href="/ckan/ckan/blob/2946-unsupported-docs-banner/ckan/config/routing.py"
               data-name="2946-unsupported-docs-banner"
               data-skip-pjax="true"
               rel="nofollow">
              <svg aria-hidden="true" class="octicon octicon-check select-menu-item-icon" height="16" version="1.1" viewBox="0 0 12 16" width="12"><path fill-rule="evenodd" d="M12 5l-8 8-4-4 1.5-1.5L4 10l6.5-6.5z"/></svg>
              <span class="select-menu-item-text css-truncate-target js-select-menu-filter-text">
                2946-unsupported-docs-banner
              </span>
            </a>
            <a class="select-menu-item js-navigation-item js-navigation-open "
               href="/ckan/ckan/blob/2949-reenable-data-api-button/ckan/config/routing.py"
               data-name="2949-reenable-data-api-button"
               data-skip-pjax="true"
               rel="nofollow">
              <svg aria-hidden="true" class="octicon octicon-check select-menu-item-icon" height="16" version="1.1" viewBox="0 0 12 16" width="12"><path fill-rule="evenodd" d="M12 5l-8 8-4-4 1.5-1.5L4 10l6.5-6.5z"/></svg>
              <span class="select-menu-item-text css-truncate-target js-select-menu-filter-text">
                2949-reenable-data-api-button
              </span>
            </a>
            <a class="select-menu-item js-navigation-item js-navigation-open "
               href="/ckan/ckan/blob/2950-paster-minify-command/ckan/config/routing.py"
               data-name="2950-paster-minify-command"
               data-skip-pjax="true"
               rel="nofollow">
              <svg aria-hidden="true" class="octicon octicon-check select-menu-item-icon" height="16" version="1.1" viewBox="0 0 12 16" width="12"><path fill-rule="evenodd" d="M12 5l-8 8-4-4 1.5-1.5L4 10l6.5-6.5z"/></svg>
              <span class="select-menu-item-text css-truncate-target js-select-menu-filter-text">
                2950-paster-minify-command
              </span>
            </a>
            <a class="select-menu-item js-navigation-item js-navigation-open "
               href="/ckan/ckan/blob/2953-template-is-a-dir/ckan/config/routing.py"
               data-name="2953-template-is-a-dir"
               data-skip-pjax="true"
               rel="nofollow">
              <svg aria-hidden="true" class="octicon octicon-check select-menu-item-icon" height="16" version="1.1" viewBox="0 0 12 16" width="12"><path fill-rule="evenodd" d="M12 5l-8 8-4-4 1.5-1.5L4 10l6.5-6.5z"/></svg>
              <span class="select-menu-item-text css-truncate-target js-select-menu-filter-text">
                2953-template-is-a-dir
              </span>
            </a>
            <a class="select-menu-item js-navigation-item js-navigation-open "
               href="/ckan/ckan/blob/2955-update-recline/ckan/config/routing.py"
               data-name="2955-update-recline"
               data-skip-pjax="true"
               rel="nofollow">
              <svg aria-hidden="true" class="octicon octicon-check select-menu-item-icon" height="16" version="1.1" viewBox="0 0 12 16" width="12"><path fill-rule="evenodd" d="M12 5l-8 8-4-4 1.5-1.5L4 10l6.5-6.5z"/></svg>
              <span class="select-menu-item-text css-truncate-target js-select-menu-filter-text">
                2955-update-recline
              </span>
            </a>
            <a class="select-menu-item js-navigation-item js-navigation-open "
               href="/ckan/ckan/blob/2956-resource-editing/ckan/config/routing.py"
               data-name="2956-resource-editing"
               data-skip-pjax="true"
               rel="nofollow">
              <svg aria-hidden="true" class="octicon octicon-check select-menu-item-icon" height="16" version="1.1" viewBox="0 0 12 16" width="12"><path fill-rule="evenodd" d="M12 5l-8 8-4-4 1.5-1.5L4 10l6.5-6.5z"/></svg>
              <span class="select-menu-item-text css-truncate-target js-select-menu-filter-text">
                2956-resource-editing
              </span>
            </a>
            <a class="select-menu-item js-navigation-item js-navigation-open "
               href="/ckan/ckan/blob/2959-bug-index-datasets-when-group-name-changes/ckan/config/routing.py"
               data-name="2959-bug-index-datasets-when-group-name-changes"
               data-skip-pjax="true"
               rel="nofollow">
              <svg aria-hidden="true" class="octicon octicon-check select-menu-item-icon" height="16" version="1.1" viewBox="0 0 12 16" width="12"><path fill-rule="evenodd" d="M12 5l-8 8-4-4 1.5-1.5L4 10l6.5-6.5z"/></svg>
              <span class="select-menu-item-text css-truncate-target js-select-menu-filter-text">
                2959-bug-index-datasets-when-group-name-changes
              </span>
            </a>
            <a class="select-menu-item js-navigation-item js-navigation-open "
               href="/ckan/ckan/blob/2961-pluggable-previews/ckan/config/routing.py"
               data-name="2961-pluggable-previews"
               data-skip-pjax="true"
               rel="nofollow">
              <svg aria-hidden="true" class="octicon octicon-check select-menu-item-icon" height="16" version="1.1" viewBox="0 0 12 16" width="12"><path fill-rule="evenodd" d="M12 5l-8 8-4-4 1.5-1.5L4 10l6.5-6.5z"/></svg>
              <span class="select-menu-item-text css-truncate-target js-select-menu-filter-text">
                2961-pluggable-previews
              </span>
            </a>
            <a class="select-menu-item js-navigation-item js-navigation-open "
               href="/ckan/ckan/blob/2968-fix-redirect-with-nonroot/ckan/config/routing.py"
               data-name="2968-fix-redirect-with-nonroot"
               data-skip-pjax="true"
               rel="nofollow">
              <svg aria-hidden="true" class="octicon octicon-check select-menu-item-icon" height="16" version="1.1" viewBox="0 0 12 16" width="12"><path fill-rule="evenodd" d="M12 5l-8 8-4-4 1.5-1.5L4 10l6.5-6.5z"/></svg>
              <span class="select-menu-item-text css-truncate-target js-select-menu-filter-text">
                2968-fix-redirect-with-nonroot
              </span>
            </a>
            <a class="select-menu-item js-navigation-item js-navigation-open "
               href="/ckan/ckan/blob/2972-solr-travis/ckan/config/routing.py"
               data-name="2972-solr-travis"
               data-skip-pjax="true"
               rel="nofollow">
              <svg aria-hidden="true" class="octicon octicon-check select-menu-item-icon" height="16" version="1.1" viewBox="0 0 12 16" width="12"><path fill-rule="evenodd" d="M12 5l-8 8-4-4 1.5-1.5L4 10l6.5-6.5z"/></svg>
              <span class="select-menu-item-text css-truncate-target js-select-menu-filter-text">
                2972-solr-travis
              </span>
            </a>
            <a class="select-menu-item js-navigation-item js-navigation-open "
               href="/ckan/ckan/blob/3000-slow-debug-render/ckan/config/routing.py"
               data-name="3000-slow-debug-render"
               data-skip-pjax="true"
               rel="nofollow">
              <svg aria-hidden="true" class="octicon octicon-check select-menu-item-icon" height="16" version="1.1" viewBox="0 0 12 16" width="12"><path fill-rule="evenodd" d="M12 5l-8 8-4-4 1.5-1.5L4 10l6.5-6.5z"/></svg>
              <span class="select-menu-item-text css-truncate-target js-select-menu-filter-text">
                3000-slow-debug-render
              </span>
            </a>
            <a class="select-menu-item js-navigation-item js-navigation-open "
               href="/ckan/ckan/blob/3002-escape-legacy-solr-params/ckan/config/routing.py"
               data-name="3002-escape-legacy-solr-params"
               data-skip-pjax="true"
               rel="nofollow">
              <svg aria-hidden="true" class="octicon octicon-check select-menu-item-icon" height="16" version="1.1" viewBox="0 0 12 16" width="12"><path fill-rule="evenodd" d="M12 5l-8 8-4-4 1.5-1.5L4 10l6.5-6.5z"/></svg>
              <span class="select-menu-item-text css-truncate-target js-select-menu-filter-text">
                3002-escape-legacy-solr-params
              </span>
            </a>
            <a class="select-menu-item js-navigation-item js-navigation-open "
               href="/ckan/ckan/blob/3002-jsonp-get/ckan/config/routing.py"
               data-name="3002-jsonp-get"
               data-skip-pjax="true"
               rel="nofollow">
              <svg aria-hidden="true" class="octicon octicon-check select-menu-item-icon" height="16" version="1.1" viewBox="0 0 12 16" width="12"><path fill-rule="evenodd" d="M12 5l-8 8-4-4 1.5-1.5L4 10l6.5-6.5z"/></svg>
              <span class="select-menu-item-text css-truncate-target js-select-menu-filter-text">
                3002-jsonp-get
              </span>
            </a>
            <a class="select-menu-item js-navigation-item js-navigation-open "
               href="/ckan/ckan/blob/3003-new-pg-db-in-utf8/ckan/config/routing.py"
               data-name="3003-new-pg-db-in-utf8"
               data-skip-pjax="true"
               rel="nofollow">
              <svg aria-hidden="true" class="octicon octicon-check select-menu-item-icon" height="16" version="1.1" viewBox="0 0 12 16" width="12"><path fill-rule="evenodd" d="M12 5l-8 8-4-4 1.5-1.5L4 10l6.5-6.5z"/></svg>
              <span class="select-menu-item-text css-truncate-target js-select-menu-filter-text">
                3003-new-pg-db-in-utf8
              </span>
            </a>
            <a class="select-menu-item js-navigation-item js-navigation-open "
               href="/ckan/ckan/blob/3005-update-jinja2/ckan/config/routing.py"
               data-name="3005-update-jinja2"
               data-skip-pjax="true"
               rel="nofollow">
              <svg aria-hidden="true" class="octicon octicon-check select-menu-item-icon" height="16" version="1.1" viewBox="0 0 12 16" width="12"><path fill-rule="evenodd" d="M12 5l-8 8-4-4 1.5-1.5L4 10l6.5-6.5z"/></svg>
              <span class="select-menu-item-text css-truncate-target js-select-menu-filter-text">
                3005-update-jinja2
              </span>
            </a>
            <a class="select-menu-item js-navigation-item js-navigation-open "
               href="/ckan/ckan/blob/3009-on-site-notification-of-new-activity/ckan/config/routing.py"
               data-name="3009-on-site-notification-of-new-activity"
               data-skip-pjax="true"
               rel="nofollow">
              <svg aria-hidden="true" class="octicon octicon-check select-menu-item-icon" height="16" version="1.1" viewBox="0 0 12 16" width="12"><path fill-rule="evenodd" d="M12 5l-8 8-4-4 1.5-1.5L4 10l6.5-6.5z"/></svg>
              <span class="select-menu-item-text css-truncate-target js-select-menu-filter-text">
                3009-on-site-notification-of-new-activity
              </span>
            </a>
            <a class="select-menu-item js-navigation-item js-navigation-open "
               href="/ckan/ckan/blob/3011-recline-updates/ckan/config/routing.py"
               data-name="3011-recline-updates"
               data-skip-pjax="true"
               rel="nofollow">
              <svg aria-hidden="true" class="octicon octicon-check select-menu-item-icon" height="16" version="1.1" viewBox="0 0 12 16" width="12"><path fill-rule="evenodd" d="M12 5l-8 8-4-4 1.5-1.5L4 10l6.5-6.5z"/></svg>
              <span class="select-menu-item-text css-truncate-target js-select-menu-filter-text">
                3011-recline-updates
              </span>
            </a>
            <a class="select-menu-item js-navigation-item js-navigation-open "
               href="/ckan/ckan/blob/3012-dg-auth/ckan/config/routing.py"
               data-name="3012-dg-auth"
               data-skip-pjax="true"
               rel="nofollow">
              <svg aria-hidden="true" class="octicon octicon-check select-menu-item-icon" height="16" version="1.1" viewBox="0 0 12 16" width="12"><path fill-rule="evenodd" d="M12 5l-8 8-4-4 1.5-1.5L4 10l6.5-6.5z"/></svg>
              <span class="select-menu-item-text css-truncate-target js-select-menu-filter-text">
                3012-dg-auth
              </span>
            </a>
            <a class="select-menu-item js-navigation-item js-navigation-open "
               href="/ckan/ckan/blob/3012-fix-datastore_active-getting-lost/ckan/config/routing.py"
               data-name="3012-fix-datastore_active-getting-lost"
               data-skip-pjax="true"
               rel="nofollow">
              <svg aria-hidden="true" class="octicon octicon-check select-menu-item-icon" height="16" version="1.1" viewBox="0 0 12 16" width="12"><path fill-rule="evenodd" d="M12 5l-8 8-4-4 1.5-1.5L4 10l6.5-6.5z"/></svg>
              <span class="select-menu-item-text css-truncate-target js-select-menu-filter-text">
                3012-fix-datastore_active-getting-lost
              </span>
            </a>
            <a class="select-menu-item js-navigation-item js-navigation-open "
               href="/ckan/ckan/blob/3016-template-tweaks/ckan/config/routing.py"
               data-name="3016-template-tweaks"
               data-skip-pjax="true"
               rel="nofollow">
              <svg aria-hidden="true" class="octicon octicon-check select-menu-item-icon" height="16" version="1.1" viewBox="0 0 12 16" width="12"><path fill-rule="evenodd" d="M12 5l-8 8-4-4 1.5-1.5L4 10l6.5-6.5z"/></svg>
              <span class="select-menu-item-text css-truncate-target js-select-menu-filter-text">
                3016-template-tweaks
              </span>
            </a>
            <a class="select-menu-item js-navigation-item js-navigation-open "
               href="/ckan/ckan/blob/3017-demo-stable/ckan/config/routing.py"
               data-name="3017-demo-stable"
               data-skip-pjax="true"
               rel="nofollow">
              <svg aria-hidden="true" class="octicon octicon-check select-menu-item-icon" height="16" version="1.1" viewBox="0 0 12 16" width="12"><path fill-rule="evenodd" d="M12 5l-8 8-4-4 1.5-1.5L4 10l6.5-6.5z"/></svg>
              <span class="select-menu-item-text css-truncate-target js-select-menu-filter-text">
                3017-demo-stable
              </span>
            </a>
            <a class="select-menu-item js-navigation-item js-navigation-open "
               href="/ckan/ckan/blob/3018-activity-streams-load-more/ckan/config/routing.py"
               data-name="3018-activity-streams-load-more"
               data-skip-pjax="true"
               rel="nofollow">
              <svg aria-hidden="true" class="octicon octicon-check select-menu-item-icon" height="16" version="1.1" viewBox="0 0 12 16" width="12"><path fill-rule="evenodd" d="M12 5l-8 8-4-4 1.5-1.5L4 10l6.5-6.5z"/></svg>
              <span class="select-menu-item-text css-truncate-target js-select-menu-filter-text">
                3018-activity-streams-load-more
              </span>
            </a>
            <a class="select-menu-item js-navigation-item js-navigation-open "
               href="/ckan/ckan/blob/3020-bug-update-coding-standards/ckan/config/routing.py"
               data-name="3020-bug-update-coding-standards"
               data-skip-pjax="true"
               rel="nofollow">
              <svg aria-hidden="true" class="octicon octicon-check select-menu-item-icon" height="16" version="1.1" viewBox="0 0 12 16" width="12"><path fill-rule="evenodd" d="M12 5l-8 8-4-4 1.5-1.5L4 10l6.5-6.5z"/></svg>
              <span class="select-menu-item-text css-truncate-target js-select-menu-filter-text">
                3020-bug-update-coding-standards
              </span>
            </a>
            <a class="select-menu-item js-navigation-item js-navigation-open "
               href="/ckan/ckan/blob/3023-data_dict-extension-points/ckan/config/routing.py"
               data-name="3023-data_dict-extension-points"
               data-skip-pjax="true"
               rel="nofollow">
              <svg aria-hidden="true" class="octicon octicon-check select-menu-item-icon" height="16" version="1.1" viewBox="0 0 12 16" width="12"><path fill-rule="evenodd" d="M12 5l-8 8-4-4 1.5-1.5L4 10l6.5-6.5z"/></svg>
              <span class="select-menu-item-text css-truncate-target js-select-menu-filter-text">
                3023-data_dict-extension-points
              </span>
            </a>
            <a class="select-menu-item js-navigation-item js-navigation-open "
               href="/ckan/ckan/blob/3024-add-activity-stream-tab-to-dataset-read-page/ckan/config/routing.py"
               data-name="3024-add-activity-stream-tab-to-dataset-read-page"
               data-skip-pjax="true"
               rel="nofollow">
              <svg aria-hidden="true" class="octicon octicon-check select-menu-item-icon" height="16" version="1.1" viewBox="0 0 12 16" width="12"><path fill-rule="evenodd" d="M12 5l-8 8-4-4 1.5-1.5L4 10l6.5-6.5z"/></svg>
              <span class="select-menu-item-text css-truncate-target js-select-menu-filter-text">
                3024-add-activity-stream-tab-to-dataset-read-page
              </span>
            </a>
            <a class="select-menu-item js-navigation-item js-navigation-open "
               href="/ckan/ckan/blob/3025-add-requests-to-requests/ckan/config/routing.py"
               data-name="3025-add-requests-to-requests"
               data-skip-pjax="true"
               rel="nofollow">
              <svg aria-hidden="true" class="octicon octicon-check select-menu-item-icon" height="16" version="1.1" viewBox="0 0 12 16" width="12"><path fill-rule="evenodd" d="M12 5l-8 8-4-4 1.5-1.5L4 10l6.5-6.5z"/></svg>
              <span class="select-menu-item-text css-truncate-target js-select-menu-filter-text">
                3025-add-requests-to-requests
              </span>
            </a>
            <a class="select-menu-item js-navigation-item js-navigation-open "
               href="/ckan/ckan/blob/3026-nav_named_link-icons/ckan/config/routing.py"
               data-name="3026-nav_named_link-icons"
               data-skip-pjax="true"
               rel="nofollow">
              <svg aria-hidden="true" class="octicon octicon-check select-menu-item-icon" height="16" version="1.1" viewBox="0 0 12 16" width="12"><path fill-rule="evenodd" d="M12 5l-8 8-4-4 1.5-1.5L4 10l6.5-6.5z"/></svg>
              <span class="select-menu-item-text css-truncate-target js-select-menu-filter-text">
                3026-nav_named_link-icons
              </span>
            </a>
            <a class="select-menu-item js-navigation-item js-navigation-open "
               href="/ckan/ckan/blob/3032-coveralls-circleci/ckan/config/routing.py"
               data-name="3032-coveralls-circleci"
               data-skip-pjax="true"
               rel="nofollow">
              <svg aria-hidden="true" class="octicon octicon-check select-menu-item-icon" height="16" version="1.1" viewBox="0 0 12 16" width="12"><path fill-rule="evenodd" d="M12 5l-8 8-4-4 1.5-1.5L4 10l6.5-6.5z"/></svg>
              <span class="select-menu-item-text css-truncate-target js-select-menu-filter-text">
                3032-coveralls-circleci
              </span>
            </a>
            <a class="select-menu-item js-navigation-item js-navigation-open "
               href="/ckan/ckan/blob/3033-build-status-badge/ckan/config/routing.py"
               data-name="3033-build-status-badge"
               data-skip-pjax="true"
               rel="nofollow">
              <svg aria-hidden="true" class="octicon octicon-check select-menu-item-icon" height="16" version="1.1" viewBox="0 0 12 16" width="12"><path fill-rule="evenodd" d="M12 5l-8 8-4-4 1.5-1.5L4 10l6.5-6.5z"/></svg>
              <span class="select-menu-item-text css-truncate-target js-select-menu-filter-text">
                3033-build-status-badge
              </span>
            </a>
            <a class="select-menu-item js-navigation-item js-navigation-open "
               href="/ckan/ckan/blob/3041-helpererror/ckan/config/routing.py"
               data-name="3041-helpererror"
               data-skip-pjax="true"
               rel="nofollow">
              <svg aria-hidden="true" class="octicon octicon-check select-menu-item-icon" height="16" version="1.1" viewBox="0 0 12 16" width="12"><path fill-rule="evenodd" d="M12 5l-8 8-4-4 1.5-1.5L4 10l6.5-6.5z"/></svg>
              <span class="select-menu-item-text css-truncate-target js-select-menu-filter-text">
                3041-helpererror
              </span>
            </a>
            <a class="select-menu-item js-navigation-item js-navigation-open "
               href="/ckan/ckan/blob/3053-old-session-data/ckan/config/routing.py"
               data-name="3053-old-session-data"
               data-skip-pjax="true"
               rel="nofollow">
              <svg aria-hidden="true" class="octicon octicon-check select-menu-item-icon" height="16" version="1.1" viewBox="0 0 12 16" width="12"><path fill-rule="evenodd" d="M12 5l-8 8-4-4 1.5-1.5L4 10l6.5-6.5z"/></svg>
              <span class="select-menu-item-text css-truncate-target js-select-menu-filter-text">
                3053-old-session-data
              </span>
            </a>
            <a class="select-menu-item js-navigation-item js-navigation-open "
               href="/ckan/ckan/blob/3055-deprecate-h.url/ckan/config/routing.py"
               data-name="3055-deprecate-h.url"
               data-skip-pjax="true"
               rel="nofollow">
              <svg aria-hidden="true" class="octicon octicon-check select-menu-item-icon" height="16" version="1.1" viewBox="0 0 12 16" width="12"><path fill-rule="evenodd" d="M12 5l-8 8-4-4 1.5-1.5L4 10l6.5-6.5z"/></svg>
              <span class="select-menu-item-text css-truncate-target js-select-menu-filter-text">
                3055-deprecate-h.url
              </span>
            </a>
            <a class="select-menu-item js-navigation-item js-navigation-open "
               href="/ckan/ckan/blob/3062-functionaltestbase-changes-2/ckan/config/routing.py"
               data-name="3062-functionaltestbase-changes-2"
               data-skip-pjax="true"
               rel="nofollow">
              <svg aria-hidden="true" class="octicon octicon-check select-menu-item-icon" height="16" version="1.1" viewBox="0 0 12 16" width="12"><path fill-rule="evenodd" d="M12 5l-8 8-4-4 1.5-1.5L4 10l6.5-6.5z"/></svg>
              <span class="select-menu-item-text css-truncate-target js-select-menu-filter-text">
                3062-functionaltestbase-changes-2
              </span>
            </a>
            <a class="select-menu-item js-navigation-item js-navigation-open "
               href="/ckan/ckan/blob/3062-functionaltestbase-changes/ckan/config/routing.py"
               data-name="3062-functionaltestbase-changes"
               data-skip-pjax="true"
               rel="nofollow">
              <svg aria-hidden="true" class="octicon octicon-check select-menu-item-icon" height="16" version="1.1" viewBox="0 0 12 16" width="12"><path fill-rule="evenodd" d="M12 5l-8 8-4-4 1.5-1.5L4 10l6.5-6.5z"/></svg>
              <span class="select-menu-item-text css-truncate-target js-select-menu-filter-text">
                3062-functionaltestbase-changes
              </span>
            </a>
            <a class="select-menu-item js-navigation-item js-navigation-open "
               href="/ckan/ckan/blob/3077-exceptions-user-invite/ckan/config/routing.py"
               data-name="3077-exceptions-user-invite"
               data-skip-pjax="true"
               rel="nofollow">
              <svg aria-hidden="true" class="octicon octicon-check select-menu-item-icon" height="16" version="1.1" viewBox="0 0 12 16" width="12"><path fill-rule="evenodd" d="M12 5l-8 8-4-4 1.5-1.5L4 10l6.5-6.5z"/></svg>
              <span class="select-menu-item-text css-truncate-target js-select-menu-filter-text">
                3077-exceptions-user-invite
              </span>
            </a>
            <a class="select-menu-item js-navigation-item js-navigation-open "
               href="/ckan/ckan/blob/3078-member_list-shows-deleted/ckan/config/routing.py"
               data-name="3078-member_list-shows-deleted"
               data-skip-pjax="true"
               rel="nofollow">
              <svg aria-hidden="true" class="octicon octicon-check select-menu-item-icon" height="16" version="1.1" viewBox="0 0 12 16" width="12"><path fill-rule="evenodd" d="M12 5l-8 8-4-4 1.5-1.5L4 10l6.5-6.5z"/></svg>
              <span class="select-menu-item-text css-truncate-target js-select-menu-filter-text">
                3078-member_list-shows-deleted
              </span>
            </a>
            <a class="select-menu-item js-navigation-item js-navigation-open "
               href="/ckan/ckan/blob/3108-validation-errors-on-member-create/ckan/config/routing.py"
               data-name="3108-validation-errors-on-member-create"
               data-skip-pjax="true"
               rel="nofollow">
              <svg aria-hidden="true" class="octicon octicon-check select-menu-item-icon" height="16" version="1.1" viewBox="0 0 12 16" width="12"><path fill-rule="evenodd" d="M12 5l-8 8-4-4 1.5-1.5L4 10l6.5-6.5z"/></svg>
              <span class="select-menu-item-text css-truncate-target js-select-menu-filter-text">
                3108-validation-errors-on-member-create
              </span>
            </a>
            <a class="select-menu-item js-navigation-item js-navigation-open "
               href="/ckan/ckan/blob/3113-more-session-removal/ckan/config/routing.py"
               data-name="3113-more-session-removal"
               data-skip-pjax="true"
               rel="nofollow">
              <svg aria-hidden="true" class="octicon octicon-check select-menu-item-icon" height="16" version="1.1" viewBox="0 0 12 16" width="12"><path fill-rule="evenodd" d="M12 5l-8 8-4-4 1.5-1.5L4 10l6.5-6.5z"/></svg>
              <span class="select-menu-item-text css-truncate-target js-select-menu-filter-text">
                3113-more-session-removal
              </span>
            </a>
            <a class="select-menu-item js-navigation-item js-navigation-open "
               href="/ckan/ckan/blob/3116-middleware-refactor/ckan/config/routing.py"
               data-name="3116-middleware-refactor"
               data-skip-pjax="true"
               rel="nofollow">
              <svg aria-hidden="true" class="octicon octicon-check select-menu-item-icon" height="16" version="1.1" viewBox="0 0 12 16" width="12"><path fill-rule="evenodd" d="M12 5l-8 8-4-4 1.5-1.5L4 10l6.5-6.5z"/></svg>
              <span class="select-menu-item-text css-truncate-target js-select-menu-filter-text">
                3116-middleware-refactor
              </span>
            </a>
            <a class="select-menu-item js-navigation-item js-navigation-open "
               href="/ckan/ckan/blob/3117-site-url-nice/ckan/config/routing.py"
               data-name="3117-site-url-nice"
               data-skip-pjax="true"
               rel="nofollow">
              <svg aria-hidden="true" class="octicon octicon-check select-menu-item-icon" height="16" version="1.1" viewBox="0 0 12 16" width="12"><path fill-rule="evenodd" d="M12 5l-8 8-4-4 1.5-1.5L4 10l6.5-6.5z"/></svg>
              <span class="select-menu-item-text css-truncate-target js-select-menu-filter-text">
                3117-site-url-nice
              </span>
            </a>
            <a class="select-menu-item js-navigation-item js-navigation-open "
               href="/ckan/ckan/blob/3132-relationship-update-docs/ckan/config/routing.py"
               data-name="3132-relationship-update-docs"
               data-skip-pjax="true"
               rel="nofollow">
              <svg aria-hidden="true" class="octicon octicon-check select-menu-item-icon" height="16" version="1.1" viewBox="0 0 12 16" width="12"><path fill-rule="evenodd" d="M12 5l-8 8-4-4 1.5-1.5L4 10l6.5-6.5z"/></svg>
              <span class="select-menu-item-text css-truncate-target js-select-menu-filter-text">
                3132-relationship-update-docs
              </span>
            </a>
            <a class="select-menu-item js-navigation-item js-navigation-open "
               href="/ckan/ckan/blob/3148-remove-wsgiparty/ckan/config/routing.py"
               data-name="3148-remove-wsgiparty"
               data-skip-pjax="true"
               rel="nofollow">
              <svg aria-hidden="true" class="octicon octicon-check select-menu-item-icon" height="16" version="1.1" viewBox="0 0 12 16" width="12"><path fill-rule="evenodd" d="M12 5l-8 8-4-4 1.5-1.5L4 10l6.5-6.5z"/></svg>
              <span class="select-menu-item-text css-truncate-target js-select-menu-filter-text">
                3148-remove-wsgiparty
              </span>
            </a>
            <a class="select-menu-item js-navigation-item js-navigation-open "
               href="/ckan/ckan/blob/3167-followee_list-q/ckan/config/routing.py"
               data-name="3167-followee_list-q"
               data-skip-pjax="true"
               rel="nofollow">
              <svg aria-hidden="true" class="octicon octicon-check select-menu-item-icon" height="16" version="1.1" viewBox="0 0 12 16" width="12"><path fill-rule="evenodd" d="M12 5l-8 8-4-4 1.5-1.5L4 10l6.5-6.5z"/></svg>
              <span class="select-menu-item-text css-truncate-target js-select-menu-filter-text">
                3167-followee_list-q
              </span>
            </a>
            <a class="select-menu-item js-navigation-item js-navigation-open "
               href="/ckan/ckan/blob/3194-fix-redirects/ckan/config/routing.py"
               data-name="3194-fix-redirects"
               data-skip-pjax="true"
               rel="nofollow">
              <svg aria-hidden="true" class="octicon octicon-check select-menu-item-icon" height="16" version="1.1" viewBox="0 0 12 16" width="12"><path fill-rule="evenodd" d="M12 5l-8 8-4-4 1.5-1.5L4 10l6.5-6.5z"/></svg>
              <span class="select-menu-item-text css-truncate-target js-select-menu-filter-text">
                3194-fix-redirects
              </span>
            </a>
            <a class="select-menu-item js-navigation-item js-navigation-open "
               href="/ckan/ckan/blob/3196-common-session/ckan/config/routing.py"
               data-name="3196-common-session"
               data-skip-pjax="true"
               rel="nofollow">
              <svg aria-hidden="true" class="octicon octicon-check select-menu-item-icon" height="16" version="1.1" viewBox="0 0 12 16" width="12"><path fill-rule="evenodd" d="M12 5l-8 8-4-4 1.5-1.5L4 10l6.5-6.5z"/></svg>
              <span class="select-menu-item-text css-truncate-target js-select-menu-filter-text">
                3196-common-session
              </span>
            </a>
            <a class="select-menu-item js-navigation-item js-navigation-open "
               href="/ckan/ckan/blob/3196-common-url_for-tests/ckan/config/routing.py"
               data-name="3196-common-url_for-tests"
               data-skip-pjax="true"
               rel="nofollow">
              <svg aria-hidden="true" class="octicon octicon-check select-menu-item-icon" height="16" version="1.1" viewBox="0 0 12 16" width="12"><path fill-rule="evenodd" d="M12 5l-8 8-4-4 1.5-1.5L4 10l6.5-6.5z"/></svg>
              <span class="select-menu-item-text css-truncate-target js-select-menu-filter-text">
                3196-common-url_for-tests
              </span>
            </a>
            <a class="select-menu-item js-navigation-item js-navigation-open "
               href="/ckan/ckan/blob/3204-remove-simple_search/ckan/config/routing.py"
               data-name="3204-remove-simple_search"
               data-skip-pjax="true"
               rel="nofollow">
              <svg aria-hidden="true" class="octicon octicon-check select-menu-item-icon" height="16" version="1.1" viewBox="0 0 12 16" width="12"><path fill-rule="evenodd" d="M12 5l-8 8-4-4 1.5-1.5L4 10l6.5-6.5z"/></svg>
              <span class="select-menu-item-text css-truncate-target js-select-menu-filter-text">
                3204-remove-simple_search
              </span>
            </a>
            <a class="select-menu-item js-navigation-item js-navigation-open "
               href="/ckan/ckan/blob/3225-update-release-docs/ckan/config/routing.py"
               data-name="3225-update-release-docs"
               data-skip-pjax="true"
               rel="nofollow">
              <svg aria-hidden="true" class="octicon octicon-check select-menu-item-icon" height="16" version="1.1" viewBox="0 0 12 16" width="12"><path fill-rule="evenodd" d="M12 5l-8 8-4-4 1.5-1.5L4 10l6.5-6.5z"/></svg>
              <span class="select-menu-item-text css-truncate-target js-select-menu-filter-text">
                3225-update-release-docs
              </span>
            </a>
            <a class="select-menu-item js-navigation-item js-navigation-open "
               href="/ckan/ckan/blob/3229-api-blueprint/ckan/config/routing.py"
               data-name="3229-api-blueprint"
               data-skip-pjax="true"
               rel="nofollow">
              <svg aria-hidden="true" class="octicon octicon-check select-menu-item-icon" height="16" version="1.1" viewBox="0 0 12 16" width="12"><path fill-rule="evenodd" d="M12 5l-8 8-4-4 1.5-1.5L4 10l6.5-6.5z"/></svg>
              <span class="select-menu-item-text css-truncate-target js-select-menu-filter-text">
                3229-api-blueprint
              </span>
            </a>
            <a class="select-menu-item js-navigation-item js-navigation-open "
               href="/ckan/ckan/blob/3233-recline-view-config/ckan/config/routing.py"
               data-name="3233-recline-view-config"
               data-skip-pjax="true"
               rel="nofollow">
              <svg aria-hidden="true" class="octicon octicon-check select-menu-item-icon" height="16" version="1.1" viewBox="0 0 12 16" width="12"><path fill-rule="evenodd" d="M12 5l-8 8-4-4 1.5-1.5L4 10l6.5-6.5z"/></svg>
              <span class="select-menu-item-text css-truncate-target js-select-menu-filter-text">
                3233-recline-view-config
              </span>
            </a>
            <a class="select-menu-item js-navigation-item js-navigation-open "
               href="/ckan/ckan/blob/3237-architecture-diagram/ckan/config/routing.py"
               data-name="3237-architecture-diagram"
               data-skip-pjax="true"
               rel="nofollow">
              <svg aria-hidden="true" class="octicon octicon-check select-menu-item-icon" height="16" version="1.1" viewBox="0 0 12 16" width="12"><path fill-rule="evenodd" d="M12 5l-8 8-4-4 1.5-1.5L4 10l6.5-6.5z"/></svg>
              <span class="select-menu-item-text css-truncate-target js-select-menu-filter-text">
                3237-architecture-diagram
              </span>
            </a>
            <a class="select-menu-item js-navigation-item js-navigation-open "
               href="/ckan/ckan/blob/3245-datastore-active-race/ckan/config/routing.py"
               data-name="3245-datastore-active-race"
               data-skip-pjax="true"
               rel="nofollow">
              <svg aria-hidden="true" class="octicon octicon-check select-menu-item-icon" height="16" version="1.1" viewBox="0 0 12 16" width="12"><path fill-rule="evenodd" d="M12 5l-8 8-4-4 1.5-1.5L4 10l6.5-6.5z"/></svg>
              <span class="select-menu-item-text css-truncate-target js-select-menu-filter-text">
                3245-datastore-active-race
              </span>
            </a>
            <a class="select-menu-item js-navigation-item js-navigation-open "
               href="/ckan/ckan/blob/3282-bug-in-locale-list/ckan/config/routing.py"
               data-name="3282-bug-in-locale-list"
               data-skip-pjax="true"
               rel="nofollow">
              <svg aria-hidden="true" class="octicon octicon-check select-menu-item-icon" height="16" version="1.1" viewBox="0 0 12 16" width="12"><path fill-rule="evenodd" d="M12 5l-8 8-4-4 1.5-1.5L4 10l6.5-6.5z"/></svg>
              <span class="select-menu-item-text css-truncate-target js-select-menu-filter-text">
                3282-bug-in-locale-list
              </span>
            </a>
            <a class="select-menu-item js-navigation-item js-navigation-open "
               href="/ckan/ckan/blob/3316-polib-req/ckan/config/routing.py"
               data-name="3316-polib-req"
               data-skip-pjax="true"
               rel="nofollow">
              <svg aria-hidden="true" class="octicon octicon-check select-menu-item-icon" height="16" version="1.1" viewBox="0 0 12 16" width="12"><path fill-rule="evenodd" d="M12 5l-8 8-4-4 1.5-1.5L4 10l6.5-6.5z"/></svg>
              <span class="select-menu-item-text css-truncate-target js-select-menu-filter-text">
                3316-polib-req
              </span>
            </a>
            <a class="select-menu-item js-navigation-item js-navigation-open "
               href="/ckan/ckan/blob/3336-document-package/ckan/config/routing.py"
               data-name="3336-document-package"
               data-skip-pjax="true"
               rel="nofollow">
              <svg aria-hidden="true" class="octicon octicon-check select-menu-item-icon" height="16" version="1.1" viewBox="0 0 12 16" width="12"><path fill-rule="evenodd" d="M12 5l-8 8-4-4 1.5-1.5L4 10l6.5-6.5z"/></svg>
              <span class="select-menu-item-text css-truncate-target js-select-menu-filter-text">
                3336-document-package
              </span>
            </a>
            <a class="select-menu-item js-navigation-item js-navigation-open "
               href="/ckan/ckan/blob/3359-skip-job-fork-test/ckan/config/routing.py"
               data-name="3359-skip-job-fork-test"
               data-skip-pjax="true"
               rel="nofollow">
              <svg aria-hidden="true" class="octicon octicon-check select-menu-item-icon" height="16" version="1.1" viewBox="0 0 12 16" width="12"><path fill-rule="evenodd" d="M12 5l-8 8-4-4 1.5-1.5L4 10l6.5-6.5z"/></svg>
              <span class="select-menu-item-text css-truncate-target js-select-menu-filter-text">
                3359-skip-job-fork-test
              </span>
            </a>
            <a class="select-menu-item js-navigation-item js-navigation-open "
               href="/ckan/ckan/blob/3360-cli-fail-failing/ckan/config/routing.py"
               data-name="3360-cli-fail-failing"
               data-skip-pjax="true"
               rel="nofollow">
              <svg aria-hidden="true" class="octicon octicon-check select-menu-item-icon" height="16" version="1.1" viewBox="0 0 12 16" width="12"><path fill-rule="evenodd" d="M12 5l-8 8-4-4 1.5-1.5L4 10l6.5-6.5z"/></svg>
              <span class="select-menu-item-text css-truncate-target js-select-menu-filter-text">
                3360-cli-fail-failing
              </span>
            </a>
            <a class="select-menu-item js-navigation-item js-navigation-open "
               href="/ckan/ckan/blob/3366-tolerate-missing-system-info/ckan/config/routing.py"
               data-name="3366-tolerate-missing-system-info"
               data-skip-pjax="true"
               rel="nofollow">
              <svg aria-hidden="true" class="octicon octicon-check select-menu-item-icon" height="16" version="1.1" viewBox="0 0 12 16" width="12"><path fill-rule="evenodd" d="M12 5l-8 8-4-4 1.5-1.5L4 10l6.5-6.5z"/></svg>
              <span class="select-menu-item-text css-truncate-target js-select-menu-filter-text">
                3366-tolerate-missing-system-info
              </span>
            </a>
            <a class="select-menu-item js-navigation-item js-navigation-open "
               href="/ckan/ckan/blob/3384-datastore-cli/ckan/config/routing.py"
               data-name="3384-datastore-cli"
               data-skip-pjax="true"
               rel="nofollow">
              <svg aria-hidden="true" class="octicon octicon-check select-menu-item-icon" height="16" version="1.1" viewBox="0 0 12 16" width="12"><path fill-rule="evenodd" d="M12 5l-8 8-4-4 1.5-1.5L4 10l6.5-6.5z"/></svg>
              <span class="select-menu-item-text css-truncate-target js-select-menu-filter-text">
                3384-datastore-cli
              </span>
            </a>
            <a class="select-menu-item js-navigation-item js-navigation-open "
               href="/ckan/ckan/blob/3441-hide-user-list/ckan/config/routing.py"
               data-name="3441-hide-user-list"
               data-skip-pjax="true"
               rel="nofollow">
              <svg aria-hidden="true" class="octicon octicon-check select-menu-item-icon" height="16" version="1.1" viewBox="0 0 12 16" width="12"><path fill-rule="evenodd" d="M12 5l-8 8-4-4 1.5-1.5L4 10l6.5-6.5z"/></svg>
              <span class="select-menu-item-text css-truncate-target js-select-menu-filter-text">
                3441-hide-user-list
              </span>
            </a>
            <a class="select-menu-item js-navigation-item js-navigation-open "
               href="/ckan/ckan/blob/3475_metadata_modified_improvements/ckan/config/routing.py"
               data-name="3475_metadata_modified_improvements"
               data-skip-pjax="true"
               rel="nofollow">
              <svg aria-hidden="true" class="octicon octicon-check select-menu-item-icon" height="16" version="1.1" viewBox="0 0 12 16" width="12"><path fill-rule="evenodd" d="M12 5l-8 8-4-4 1.5-1.5L4 10l6.5-6.5z"/></svg>
              <span class="select-menu-item-text css-truncate-target js-select-menu-filter-text">
                3475_metadata_modified_improvements
              </span>
            </a>
            <a class="select-menu-item js-navigation-item js-navigation-open "
               href="/ckan/ckan/blob/3484_revision_ui_removal/ckan/config/routing.py"
               data-name="3484_revision_ui_removal"
               data-skip-pjax="true"
               rel="nofollow">
              <svg aria-hidden="true" class="octicon octicon-check select-menu-item-icon" height="16" version="1.1" viewBox="0 0 12 16" width="12"><path fill-rule="evenodd" d="M12 5l-8 8-4-4 1.5-1.5L4 10l6.5-6.5z"/></svg>
              <span class="select-menu-item-text css-truncate-target js-select-menu-filter-text">
                3484_revision_ui_removal
              </span>
            </a>
            <a class="select-menu-item js-navigation-item js-navigation-open "
               href="/ckan/ckan/blob/3539-fix-i18n-directory/ckan/config/routing.py"
               data-name="3539-fix-i18n-directory"
               data-skip-pjax="true"
               rel="nofollow">
              <svg aria-hidden="true" class="octicon octicon-check select-menu-item-icon" height="16" version="1.1" viewBox="0 0 12 16" width="12"><path fill-rule="evenodd" d="M12 5l-8 8-4-4 1.5-1.5L4 10l6.5-6.5z"/></svg>
              <span class="select-menu-item-text css-truncate-target js-select-menu-filter-text">
                3539-fix-i18n-directory
              </span>
            </a>
            <a class="select-menu-item js-navigation-item js-navigation-open "
               href="/ckan/ckan/blob/3644-activity-test-utcnow/ckan/config/routing.py"
               data-name="3644-activity-test-utcnow"
               data-skip-pjax="true"
               rel="nofollow">
              <svg aria-hidden="true" class="octicon octicon-check select-menu-item-icon" height="16" version="1.1" viewBox="0 0 12 16" width="12"><path fill-rule="evenodd" d="M12 5l-8 8-4-4 1.5-1.5L4 10l6.5-6.5z"/></svg>
              <span class="select-menu-item-text css-truncate-target js-select-menu-filter-text">
                3644-activity-test-utcnow
              </span>
            </a>
            <a class="select-menu-item js-navigation-item js-navigation-open "
               href="/ckan/ckan/blob/3669-datatables-schema/ckan/config/routing.py"
               data-name="3669-datatables-schema"
               data-skip-pjax="true"
               rel="nofollow">
              <svg aria-hidden="true" class="octicon octicon-check select-menu-item-icon" height="16" version="1.1" viewBox="0 0 12 16" width="12"><path fill-rule="evenodd" d="M12 5l-8 8-4-4 1.5-1.5L4 10l6.5-6.5z"/></svg>
              <span class="select-menu-item-text css-truncate-target js-select-menu-filter-text">
                3669-datatables-schema
              </span>
            </a>
            <a class="select-menu-item js-navigation-item js-navigation-open "
               href="/ckan/ckan/blob/3684-restrict-access/ckan/config/routing.py"
               data-name="3684-restrict-access"
               data-skip-pjax="true"
               rel="nofollow">
              <svg aria-hidden="true" class="octicon octicon-check select-menu-item-icon" height="16" version="1.1" viewBox="0 0 12 16" width="12"><path fill-rule="evenodd" d="M12 5l-8 8-4-4 1.5-1.5L4 10l6.5-6.5z"/></svg>
              <span class="select-menu-item-text css-truncate-target js-select-menu-filter-text">
                3684-restrict-access
              </span>
            </a>
            <a class="select-menu-item js-navigation-item js-navigation-open "
               href="/ckan/ckan/blob/3760-auto-test-request-context/ckan/config/routing.py"
               data-name="3760-auto-test-request-context"
               data-skip-pjax="true"
               rel="nofollow">
              <svg aria-hidden="true" class="octicon octicon-check select-menu-item-icon" height="16" version="1.1" viewBox="0 0 12 16" width="12"><path fill-rule="evenodd" d="M12 5l-8 8-4-4 1.5-1.5L4 10l6.5-6.5z"/></svg>
              <span class="select-menu-item-text css-truncate-target js-select-menu-filter-text">
                3760-auto-test-request-context
              </span>
            </a>
            <a class="select-menu-item js-navigation-item js-navigation-open "
               href="/ckan/ckan/blob/3760-context-in-cli/ckan/config/routing.py"
               data-name="3760-context-in-cli"
               data-skip-pjax="true"
               rel="nofollow">
              <svg aria-hidden="true" class="octicon octicon-check select-menu-item-icon" height="16" version="1.1" viewBox="0 0 12 16" width="12"><path fill-rule="evenodd" d="M12 5l-8 8-4-4 1.5-1.5L4 10l6.5-6.5z"/></svg>
              <span class="select-menu-item-text css-truncate-target js-select-menu-filter-text">
                3760-context-in-cli
              </span>
            </a>
            <a class="select-menu-item js-navigation-item js-navigation-open "
               href="/ckan/ckan/blob/3810-datastore-create-smaller-response/ckan/config/routing.py"
               data-name="3810-datastore-create-smaller-response"
               data-skip-pjax="true"
               rel="nofollow">
              <svg aria-hidden="true" class="octicon octicon-check select-menu-item-icon" height="16" version="1.1" viewBox="0 0 12 16" width="12"><path fill-rule="evenodd" d="M12 5l-8 8-4-4 1.5-1.5L4 10l6.5-6.5z"/></svg>
              <span class="select-menu-item-text css-truncate-target js-select-menu-filter-text">
                3810-datastore-create-smaller-response
              </span>
            </a>
            <a class="select-menu-item js-navigation-item js-navigation-open "
               href="/ckan/ckan/blob/3816-query-based-views/ckan/config/routing.py"
               data-name="3816-query-based-views"
               data-skip-pjax="true"
               rel="nofollow">
              <svg aria-hidden="true" class="octicon octicon-check select-menu-item-icon" height="16" version="1.1" viewBox="0 0 12 16" width="12"><path fill-rule="evenodd" d="M12 5l-8 8-4-4 1.5-1.5L4 10l6.5-6.5z"/></svg>
              <span class="select-menu-item-text css-truncate-target js-select-menu-filter-text">
                3816-query-based-views
              </span>
            </a>
            <a class="select-menu-item js-navigation-item js-navigation-open "
               href="/ckan/ckan/blob/add-wmts-format/ckan/config/routing.py"
               data-name="add-wmts-format"
               data-skip-pjax="true"
               rel="nofollow">
              <svg aria-hidden="true" class="octicon octicon-check select-menu-item-icon" height="16" version="1.1" viewBox="0 0 12 16" width="12"><path fill-rule="evenodd" d="M12 5l-8 8-4-4 1.5-1.5L4 10l6.5-6.5z"/></svg>
              <span class="select-menu-item-text css-truncate-target js-select-menu-filter-text">
                add-wmts-format
              </span>
            </a>
            <a class="select-menu-item js-navigation-item js-navigation-open "
               href="/ckan/ckan/blob/aslist-docs/ckan/config/routing.py"
               data-name="aslist-docs"
               data-skip-pjax="true"
               rel="nofollow">
              <svg aria-hidden="true" class="octicon octicon-check select-menu-item-icon" height="16" version="1.1" viewBox="0 0 12 16" width="12"><path fill-rule="evenodd" d="M12 5l-8 8-4-4 1.5-1.5L4 10l6.5-6.5z"/></svg>
              <span class="select-menu-item-text css-truncate-target js-select-menu-filter-text">
                aslist-docs
              </span>
            </a>
            <a class="select-menu-item js-navigation-item js-navigation-open "
               href="/ckan/ckan/blob/autofix/wrapped2_to3_fix/ckan/config/routing.py"
               data-name="autofix/wrapped2_to3_fix"
               data-skip-pjax="true"
               rel="nofollow">
              <svg aria-hidden="true" class="octicon octicon-check select-menu-item-icon" height="16" version="1.1" viewBox="0 0 12 16" width="12"><path fill-rule="evenodd" d="M12 5l-8 8-4-4 1.5-1.5L4 10l6.5-6.5z"/></svg>
              <span class="select-menu-item-text css-truncate-target js-select-menu-filter-text">
                autofix/wrapped2_to3_fix
              </span>
            </a>
            <a class="select-menu-item js-navigation-item js-navigation-open "
               href="/ckan/ckan/blob/avoid-ignored-file-confusion/ckan/config/routing.py"
               data-name="avoid-ignored-file-confusion"
               data-skip-pjax="true"
               rel="nofollow">
              <svg aria-hidden="true" class="octicon octicon-check select-menu-item-icon" height="16" version="1.1" viewBox="0 0 12 16" width="12"><path fill-rule="evenodd" d="M12 5l-8 8-4-4 1.5-1.5L4 10l6.5-6.5z"/></svg>
              <span class="select-menu-item-text css-truncate-target js-select-menu-filter-text">
                avoid-ignored-file-confusion
              </span>
            </a>
            <a class="select-menu-item js-navigation-item js-navigation-open "
               href="/ckan/ckan/blob/canada/ckan/config/routing.py"
               data-name="canada"
               data-skip-pjax="true"
               rel="nofollow">
              <svg aria-hidden="true" class="octicon octicon-check select-menu-item-icon" height="16" version="1.1" viewBox="0 0 12 16" width="12"><path fill-rule="evenodd" d="M12 5l-8 8-4-4 1.5-1.5L4 10l6.5-6.5z"/></svg>
              <span class="select-menu-item-text css-truncate-target js-select-menu-filter-text">
                canada
              </span>
            </a>
            <a class="select-menu-item js-navigation-item js-navigation-open "
               href="/ckan/ckan/blob/circleci-junit-output/ckan/config/routing.py"
               data-name="circleci-junit-output"
               data-skip-pjax="true"
               rel="nofollow">
              <svg aria-hidden="true" class="octicon octicon-check select-menu-item-icon" height="16" version="1.1" viewBox="0 0 12 16" width="12"><path fill-rule="evenodd" d="M12 5l-8 8-4-4 1.5-1.5L4 10l6.5-6.5z"/></svg>
              <span class="select-menu-item-text css-truncate-target js-select-menu-filter-text">
                circleci-junit-output
              </span>
            </a>
            <a class="select-menu-item js-navigation-item js-navigation-open "
               href="/ckan/ckan/blob/closed-organizations/ckan/config/routing.py"
               data-name="closed-organizations"
               data-skip-pjax="true"
               rel="nofollow">
              <svg aria-hidden="true" class="octicon octicon-check select-menu-item-icon" height="16" version="1.1" viewBox="0 0 12 16" width="12"><path fill-rule="evenodd" d="M12 5l-8 8-4-4 1.5-1.5L4 10l6.5-6.5z"/></svg>
              <span class="select-menu-item-text css-truncate-target js-select-menu-filter-text">
                closed-organizations
              </span>
            </a>
            <a class="select-menu-item js-navigation-item js-navigation-open "
               href="/ckan/ckan/blob/copyright-msg/ckan/config/routing.py"
               data-name="copyright-msg"
               data-skip-pjax="true"
               rel="nofollow">
              <svg aria-hidden="true" class="octicon octicon-check select-menu-item-icon" height="16" version="1.1" viewBox="0 0 12 16" width="12"><path fill-rule="evenodd" d="M12 5l-8 8-4-4 1.5-1.5L4 10l6.5-6.5z"/></svg>
              <span class="select-menu-item-text css-truncate-target js-select-menu-filter-text">
                copyright-msg
              </span>
            </a>
            <a class="select-menu-item js-navigation-item js-navigation-open "
               href="/ckan/ckan/blob/coveralls-exclude-libraries/ckan/config/routing.py"
               data-name="coveralls-exclude-libraries"
               data-skip-pjax="true"
               rel="nofollow">
              <svg aria-hidden="true" class="octicon octicon-check select-menu-item-icon" height="16" version="1.1" viewBox="0 0 12 16" width="12"><path fill-rule="evenodd" d="M12 5l-8 8-4-4 1.5-1.5L4 10l6.5-6.5z"/></svg>
              <span class="select-menu-item-text css-truncate-target js-select-menu-filter-text">
                coveralls-exclude-libraries
              </span>
            </a>
            <a class="select-menu-item js-navigation-item js-navigation-open "
               href="/ckan/ckan/blob/data-dict-flash/ckan/config/routing.py"
               data-name="data-dict-flash"
               data-skip-pjax="true"
               rel="nofollow">
              <svg aria-hidden="true" class="octicon octicon-check select-menu-item-icon" height="16" version="1.1" viewBox="0 0 12 16" width="12"><path fill-rule="evenodd" d="M12 5l-8 8-4-4 1.5-1.5L4 10l6.5-6.5z"/></svg>
              <span class="select-menu-item-text css-truncate-target js-select-menu-filter-text">
                data-dict-flash
              </span>
            </a>
            <a class="select-menu-item js-navigation-item js-navigation-open "
               href="/ckan/ckan/blob/datapusher-plugin/ckan/config/routing.py"
               data-name="datapusher-plugin"
               data-skip-pjax="true"
               rel="nofollow">
              <svg aria-hidden="true" class="octicon octicon-check select-menu-item-icon" height="16" version="1.1" viewBox="0 0 12 16" width="12"><path fill-rule="evenodd" d="M12 5l-8 8-4-4 1.5-1.5L4 10l6.5-6.5z"/></svg>
              <span class="select-menu-item-text css-truncate-target js-select-menu-filter-text">
                datapusher-plugin
              </span>
            </a>
            <a class="select-menu-item js-navigation-item js-navigation-open "
               href="/ckan/ckan/blob/datastore-auth-fixes/ckan/config/routing.py"
               data-name="datastore-auth-fixes"
               data-skip-pjax="true"
               rel="nofollow">
              <svg aria-hidden="true" class="octicon octicon-check select-menu-item-icon" height="16" version="1.1" viewBox="0 0 12 16" width="12"><path fill-rule="evenodd" d="M12 5l-8 8-4-4 1.5-1.5L4 10l6.5-6.5z"/></svg>
              <span class="select-menu-item-text css-truncate-target js-select-menu-filter-text">
                datastore-auth-fixes
              </span>
            </a>
            <a class="select-menu-item js-navigation-item js-navigation-open "
               href="/ckan/ckan/blob/datastore-db-docstrings/ckan/config/routing.py"
               data-name="datastore-db-docstrings"
               data-skip-pjax="true"
               rel="nofollow">
              <svg aria-hidden="true" class="octicon octicon-check select-menu-item-icon" height="16" version="1.1" viewBox="0 0 12 16" width="12"><path fill-rule="evenodd" d="M12 5l-8 8-4-4 1.5-1.5L4 10l6.5-6.5z"/></svg>
              <span class="select-menu-item-text css-truncate-target js-select-menu-filter-text">
                datastore-db-docstrings
              </span>
            </a>
            <a class="select-menu-item js-navigation-item js-navigation-open "
               href="/ckan/ckan/blob/datastore-doc/ckan/config/routing.py"
               data-name="datastore-doc"
               data-skip-pjax="true"
               rel="nofollow">
              <svg aria-hidden="true" class="octicon octicon-check select-menu-item-icon" height="16" version="1.1" viewBox="0 0 12 16" width="12"><path fill-rule="evenodd" d="M12 5l-8 8-4-4 1.5-1.5L4 10l6.5-6.5z"/></svg>
              <span class="select-menu-item-text css-truncate-target js-select-menu-filter-text">
                datastore-doc
              </span>
            </a>
            <a class="select-menu-item js-navigation-item js-navigation-open "
               href="/ckan/ckan/blob/deprecate-notify_after_commit/ckan/config/routing.py"
               data-name="deprecate-notify_after_commit"
               data-skip-pjax="true"
               rel="nofollow">
              <svg aria-hidden="true" class="octicon octicon-check select-menu-item-icon" height="16" version="1.1" viewBox="0 0 12 16" width="12"><path fill-rule="evenodd" d="M12 5l-8 8-4-4 1.5-1.5L4 10l6.5-6.5z"/></svg>
              <span class="select-menu-item-text css-truncate-target js-select-menu-filter-text">
                deprecate-notify_after_commit
              </span>
            </a>
            <a class="select-menu-item js-navigation-item js-navigation-open "
               href="/ckan/ckan/blob/dev-v2.6/ckan/config/routing.py"
               data-name="dev-v2.6"
               data-skip-pjax="true"
               rel="nofollow">
              <svg aria-hidden="true" class="octicon octicon-check select-menu-item-icon" height="16" version="1.1" viewBox="0 0 12 16" width="12"><path fill-rule="evenodd" d="M12 5l-8 8-4-4 1.5-1.5L4 10l6.5-6.5z"/></svg>
              <span class="select-menu-item-text css-truncate-target js-select-menu-filter-text">
                dev-v2.6
              </span>
            </a>
            <a class="select-menu-item js-navigation-item js-navigation-open "
               href="/ckan/ckan/blob/dev-v2.7/ckan/config/routing.py"
               data-name="dev-v2.7"
               data-skip-pjax="true"
               rel="nofollow">
              <svg aria-hidden="true" class="octicon octicon-check select-menu-item-icon" height="16" version="1.1" viewBox="0 0 12 16" width="12"><path fill-rule="evenodd" d="M12 5l-8 8-4-4 1.5-1.5L4 10l6.5-6.5z"/></svg>
              <span class="select-menu-item-text css-truncate-target js-select-menu-filter-text">
                dev-v2.7
              </span>
            </a>
            <a class="select-menu-item js-navigation-item js-navigation-open "
               href="/ckan/ckan/blob/dictization-error-unicode/ckan/config/routing.py"
               data-name="dictization-error-unicode"
               data-skip-pjax="true"
               rel="nofollow">
              <svg aria-hidden="true" class="octicon octicon-check select-menu-item-icon" height="16" version="1.1" viewBox="0 0 12 16" width="12"><path fill-rule="evenodd" d="M12 5l-8 8-4-4 1.5-1.5L4 10l6.5-6.5z"/></svg>
              <span class="select-menu-item-text css-truncate-target js-select-menu-filter-text">
                dictization-error-unicode
              </span>
            </a>
            <a class="select-menu-item js-navigation-item js-navigation-open "
               href="/ckan/ckan/blob/dictization-error-unicode2/ckan/config/routing.py"
               data-name="dictization-error-unicode2"
               data-skip-pjax="true"
               rel="nofollow">
              <svg aria-hidden="true" class="octicon octicon-check select-menu-item-icon" height="16" version="1.1" viewBox="0 0 12 16" width="12"><path fill-rule="evenodd" d="M12 5l-8 8-4-4 1.5-1.5L4 10l6.5-6.5z"/></svg>
              <span class="select-menu-item-text css-truncate-target js-select-menu-filter-text">
                dictization-error-unicode2
              </span>
            </a>
            <a class="select-menu-item js-navigation-item js-navigation-open "
               href="/ckan/ckan/blob/disable-datastore-sql/ckan/config/routing.py"
               data-name="disable-datastore-sql"
               data-skip-pjax="true"
               rel="nofollow">
              <svg aria-hidden="true" class="octicon octicon-check select-menu-item-icon" height="16" version="1.1" viewBox="0 0 12 16" width="12"><path fill-rule="evenodd" d="M12 5l-8 8-4-4 1.5-1.5L4 10l6.5-6.5z"/></svg>
              <span class="select-menu-item-text css-truncate-target js-select-menu-filter-text">
                disable-datastore-sql
              </span>
            </a>
            <a class="select-menu-item js-navigation-item js-navigation-open "
               href="/ckan/ckan/blob/doc-issues/ckan/config/routing.py"
               data-name="doc-issues"
               data-skip-pjax="true"
               rel="nofollow">
              <svg aria-hidden="true" class="octicon octicon-check select-menu-item-icon" height="16" version="1.1" viewBox="0 0 12 16" width="12"><path fill-rule="evenodd" d="M12 5l-8 8-4-4 1.5-1.5L4 10l6.5-6.5z"/></svg>
              <span class="select-menu-item-text css-truncate-target js-select-menu-filter-text">
                doc-issues
              </span>
            </a>
            <a class="select-menu-item js-navigation-item js-navigation-open "
               href="/ckan/ckan/blob/extension-test-branch/ckan/config/routing.py"
               data-name="extension-test-branch"
               data-skip-pjax="true"
               rel="nofollow">
              <svg aria-hidden="true" class="octicon octicon-check select-menu-item-icon" height="16" version="1.1" viewBox="0 0 12 16" width="12"><path fill-rule="evenodd" d="M12 5l-8 8-4-4 1.5-1.5L4 10l6.5-6.5z"/></svg>
              <span class="select-menu-item-text css-truncate-target js-select-menu-filter-text">
                extension-test-branch
              </span>
            </a>
            <a class="select-menu-item js-navigation-item js-navigation-open "
               href="/ckan/ckan/blob/feature-2330-make-api-read-actions-GETable/ckan/config/routing.py"
               data-name="feature-2330-make-api-read-actions-GETable"
               data-skip-pjax="true"
               rel="nofollow">
              <svg aria-hidden="true" class="octicon octicon-check select-menu-item-icon" height="16" version="1.1" viewBox="0 0 12 16" width="12"><path fill-rule="evenodd" d="M12 5l-8 8-4-4 1.5-1.5L4 10l6.5-6.5z"/></svg>
              <span class="select-menu-item-text css-truncate-target js-select-menu-filter-text">
                feature-2330-make-api-read-actions-GETable
              </span>
            </a>
            <a class="select-menu-item js-navigation-item js-navigation-open "
               href="/ckan/ckan/blob/file-upload-doc-file/ckan/config/routing.py"
               data-name="file-upload-doc-file"
               data-skip-pjax="true"
               rel="nofollow">
              <svg aria-hidden="true" class="octicon octicon-check select-menu-item-icon" height="16" version="1.1" viewBox="0 0 12 16" width="12"><path fill-rule="evenodd" d="M12 5l-8 8-4-4 1.5-1.5L4 10l6.5-6.5z"/></svg>
              <span class="select-menu-item-text css-truncate-target js-select-menu-filter-text">
                file-upload-doc-file
              </span>
            </a>
            <a class="select-menu-item js-navigation-item js-navigation-open "
               href="/ckan/ckan/blob/fix-2.2.1-tests/ckan/config/routing.py"
               data-name="fix-2.2.1-tests"
               data-skip-pjax="true"
               rel="nofollow">
              <svg aria-hidden="true" class="octicon octicon-check select-menu-item-icon" height="16" version="1.1" viewBox="0 0 12 16" width="12"><path fill-rule="evenodd" d="M12 5l-8 8-4-4 1.5-1.5L4 10l6.5-6.5z"/></svg>
              <span class="select-menu-item-text css-truncate-target js-select-menu-filter-text">
                fix-2.2.1-tests
              </span>
            </a>
            <a class="select-menu-item js-navigation-item js-navigation-open "
               href="/ckan/ckan/blob/fix-SA-warning/ckan/config/routing.py"
               data-name="fix-SA-warning"
               data-skip-pjax="true"
               rel="nofollow">
              <svg aria-hidden="true" class="octicon octicon-check select-menu-item-icon" height="16" version="1.1" viewBox="0 0 12 16" width="12"><path fill-rule="evenodd" d="M12 5l-8 8-4-4 1.5-1.5L4 10l6.5-6.5z"/></svg>
              <span class="select-menu-item-text css-truncate-target js-select-menu-filter-text">
                fix-SA-warning
              </span>
            </a>
            <a class="select-menu-item js-navigation-item js-navigation-open "
               href="/ckan/ckan/blob/fix-context-hacks/ckan/config/routing.py"
               data-name="fix-context-hacks"
               data-skip-pjax="true"
               rel="nofollow">
              <svg aria-hidden="true" class="octicon octicon-check select-menu-item-icon" height="16" version="1.1" viewBox="0 0 12 16" width="12"><path fill-rule="evenodd" d="M12 5l-8 8-4-4 1.5-1.5L4 10l6.5-6.5z"/></svg>
              <span class="select-menu-item-text css-truncate-target js-select-menu-filter-text">
                fix-context-hacks
              </span>
            </a>
            <a class="select-menu-item js-navigation-item js-navigation-open "
               href="/ckan/ckan/blob/fix-direct-import-doc-issue/ckan/config/routing.py"
               data-name="fix-direct-import-doc-issue"
               data-skip-pjax="true"
               rel="nofollow">
              <svg aria-hidden="true" class="octicon octicon-check select-menu-item-icon" height="16" version="1.1" viewBox="0 0 12 16" width="12"><path fill-rule="evenodd" d="M12 5l-8 8-4-4 1.5-1.5L4 10l6.5-6.5z"/></svg>
              <span class="select-menu-item-text css-truncate-target js-select-menu-filter-text">
                fix-direct-import-doc-issue
              </span>
            </a>
            <a class="select-menu-item js-navigation-item js-navigation-open "
               href="/ckan/ckan/blob/fix-filestore-docs/ckan/config/routing.py"
               data-name="fix-filestore-docs"
               data-skip-pjax="true"
               rel="nofollow">
              <svg aria-hidden="true" class="octicon octicon-check select-menu-item-icon" height="16" version="1.1" viewBox="0 0 12 16" width="12"><path fill-rule="evenodd" d="M12 5l-8 8-4-4 1.5-1.5L4 10l6.5-6.5z"/></svg>
              <span class="select-menu-item-text css-truncate-target js-select-menu-filter-text">
                fix-filestore-docs
              </span>
            </a>
            <a class="select-menu-item js-navigation-item js-navigation-open "
               href="/ckan/ckan/blob/fix-flask-docs/ckan/config/routing.py"
               data-name="fix-flask-docs"
               data-skip-pjax="true"
               rel="nofollow">
              <svg aria-hidden="true" class="octicon octicon-check select-menu-item-icon" height="16" version="1.1" viewBox="0 0 12 16" width="12"><path fill-rule="evenodd" d="M12 5l-8 8-4-4 1.5-1.5L4 10l6.5-6.5z"/></svg>
              <span class="select-menu-item-text css-truncate-target js-select-menu-filter-text">
                fix-flask-docs
              </span>
            </a>
            <a class="select-menu-item js-navigation-item js-navigation-open "
               href="/ckan/ckan/blob/fix-js-tests-and-circle/ckan/config/routing.py"
               data-name="fix-js-tests-and-circle"
               data-skip-pjax="true"
               rel="nofollow">
              <svg aria-hidden="true" class="octicon octicon-check select-menu-item-icon" height="16" version="1.1" viewBox="0 0 12 16" width="12"><path fill-rule="evenodd" d="M12 5l-8 8-4-4 1.5-1.5L4 10l6.5-6.5z"/></svg>
              <span class="select-menu-item-text css-truncate-target js-select-menu-filter-text">
                fix-js-tests-and-circle
              </span>
            </a>
            <a class="select-menu-item js-navigation-item js-navigation-open "
               href="/ckan/ckan/blob/fix-setup-classifiers/ckan/config/routing.py"
               data-name="fix-setup-classifiers"
               data-skip-pjax="true"
               rel="nofollow">
              <svg aria-hidden="true" class="octicon octicon-check select-menu-item-icon" height="16" version="1.1" viewBox="0 0 12 16" width="12"><path fill-rule="evenodd" d="M12 5l-8 8-4-4 1.5-1.5L4 10l6.5-6.5z"/></svg>
              <span class="select-menu-item-text css-truncate-target js-select-menu-filter-text">
                fix-setup-classifiers
              </span>
            </a>
            <a class="select-menu-item js-navigation-item js-navigation-open "
               href="/ckan/ckan/blob/fix-some-sphinx-warnings/ckan/config/routing.py"
               data-name="fix-some-sphinx-warnings"
               data-skip-pjax="true"
               rel="nofollow">
              <svg aria-hidden="true" class="octicon octicon-check select-menu-item-icon" height="16" version="1.1" viewBox="0 0 12 16" width="12"><path fill-rule="evenodd" d="M12 5l-8 8-4-4 1.5-1.5L4 10l6.5-6.5z"/></svg>
              <span class="select-menu-item-text css-truncate-target js-select-menu-filter-text">
                fix-some-sphinx-warnings
              </span>
            </a>
            <a class="select-menu-item js-navigation-item js-navigation-open "
               href="/ckan/ckan/blob/fix-submodule-error/ckan/config/routing.py"
               data-name="fix-submodule-error"
               data-skip-pjax="true"
               rel="nofollow">
              <svg aria-hidden="true" class="octicon octicon-check select-menu-item-icon" height="16" version="1.1" viewBox="0 0 12 16" width="12"><path fill-rule="evenodd" d="M12 5l-8 8-4-4 1.5-1.5L4 10l6.5-6.5z"/></svg>
              <span class="select-menu-item-text css-truncate-target js-select-menu-filter-text">
                fix-submodule-error
              </span>
            </a>
            <a class="select-menu-item js-navigation-item js-navigation-open "
               href="/ckan/ckan/blob/fix-tests-2.5.7/ckan/config/routing.py"
               data-name="fix-tests-2.5.7"
               data-skip-pjax="true"
               rel="nofollow">
              <svg aria-hidden="true" class="octicon octicon-check select-menu-item-icon" height="16" version="1.1" viewBox="0 0 12 16" width="12"><path fill-rule="evenodd" d="M12 5l-8 8-4-4 1.5-1.5L4 10l6.5-6.5z"/></svg>
              <span class="select-menu-item-text css-truncate-target js-select-menu-filter-text">
                fix-tests-2.5.7
              </span>
            </a>
            <a class="select-menu-item js-navigation-item js-navigation-open "
               href="/ckan/ckan/blob/fix-travis-breakage/ckan/config/routing.py"
               data-name="fix-travis-breakage"
               data-skip-pjax="true"
               rel="nofollow">
              <svg aria-hidden="true" class="octicon octicon-check select-menu-item-icon" height="16" version="1.1" viewBox="0 0 12 16" width="12"><path fill-rule="evenodd" d="M12 5l-8 8-4-4 1.5-1.5L4 10l6.5-6.5z"/></svg>
              <span class="select-menu-item-text css-truncate-target js-select-menu-filter-text">
                fix-travis-breakage
              </span>
            </a>
            <a class="select-menu-item js-navigation-item js-navigation-open "
               href="/ckan/ckan/blob/fix-travis-on-release-v2.0/ckan/config/routing.py"
               data-name="fix-travis-on-release-v2.0"
               data-skip-pjax="true"
               rel="nofollow">
              <svg aria-hidden="true" class="octicon octicon-check select-menu-item-icon" height="16" version="1.1" viewBox="0 0 12 16" width="12"><path fill-rule="evenodd" d="M12 5l-8 8-4-4 1.5-1.5L4 10l6.5-6.5z"/></svg>
              <span class="select-menu-item-text css-truncate-target js-select-menu-filter-text">
                fix-travis-on-release-v2.0
              </span>
            </a>
            <a class="select-menu-item js-navigation-item js-navigation-open "
               href="/ckan/ckan/blob/fix-travis/ckan/config/routing.py"
               data-name="fix-travis"
               data-skip-pjax="true"
               rel="nofollow">
              <svg aria-hidden="true" class="octicon octicon-check select-menu-item-icon" height="16" version="1.1" viewBox="0 0 12 16" width="12"><path fill-rule="evenodd" d="M12 5l-8 8-4-4 1.5-1.5L4 10l6.5-6.5z"/></svg>
              <span class="select-menu-item-text css-truncate-target js-select-menu-filter-text">
                fix-travis
              </span>
            </a>
            <a class="select-menu-item js-navigation-item js-navigation-open "
               href="/ckan/ckan/blob/fix-unicode-format-issues/ckan/config/routing.py"
               data-name="fix-unicode-format-issues"
               data-skip-pjax="true"
               rel="nofollow">
              <svg aria-hidden="true" class="octicon octicon-check select-menu-item-icon" height="16" version="1.1" viewBox="0 0 12 16" width="12"><path fill-rule="evenodd" d="M12 5l-8 8-4-4 1.5-1.5L4 10l6.5-6.5z"/></svg>
              <span class="select-menu-item-text css-truncate-target js-select-menu-filter-text">
                fix-unicode-format-issues
              </span>
            </a>
            <a class="select-menu-item js-navigation-item js-navigation-open "
               href="/ckan/ckan/blob/fix_group_activity_performance/ckan/config/routing.py"
               data-name="fix_group_activity_performance"
               data-skip-pjax="true"
               rel="nofollow">
              <svg aria-hidden="true" class="octicon octicon-check select-menu-item-icon" height="16" version="1.1" viewBox="0 0 12 16" width="12"><path fill-rule="evenodd" d="M12 5l-8 8-4-4 1.5-1.5L4 10l6.5-6.5z"/></svg>
              <span class="select-menu-item-text css-truncate-target js-select-menu-filter-text">
                fix_group_activity_performance
              </span>
            </a>
            <a class="select-menu-item js-navigation-item js-navigation-open "
               href="/ckan/ckan/blob/fix_template_error/ckan/config/routing.py"
               data-name="fix_template_error"
               data-skip-pjax="true"
               rel="nofollow">
              <svg aria-hidden="true" class="octicon octicon-check select-menu-item-icon" height="16" version="1.1" viewBox="0 0 12 16" width="12"><path fill-rule="evenodd" d="M12 5l-8 8-4-4 1.5-1.5L4 10l6.5-6.5z"/></svg>
              <span class="select-menu-item-text css-truncate-target js-select-menu-filter-text">
                fix_template_error
              </span>
            </a>
            <a class="select-menu-item js-navigation-item js-navigation-open "
               href="/ckan/ckan/blob/fixes-2.0-new/ckan/config/routing.py"
               data-name="fixes-2.0-new"
               data-skip-pjax="true"
               rel="nofollow">
              <svg aria-hidden="true" class="octicon octicon-check select-menu-item-icon" height="16" version="1.1" viewBox="0 0 12 16" width="12"><path fill-rule="evenodd" d="M12 5l-8 8-4-4 1.5-1.5L4 10l6.5-6.5z"/></svg>
              <span class="select-menu-item-text css-truncate-target js-select-menu-filter-text">
                fixes-2.0-new
              </span>
            </a>
            <a class="select-menu-item js-navigation-item js-navigation-open "
               href="/ckan/ckan/blob/fixes-for-2.0/ckan/config/routing.py"
               data-name="fixes-for-2.0"
               data-skip-pjax="true"
               rel="nofollow">
              <svg aria-hidden="true" class="octicon octicon-check select-menu-item-icon" height="16" version="1.1" viewBox="0 0 12 16" width="12"><path fill-rule="evenodd" d="M12 5l-8 8-4-4 1.5-1.5L4 10l6.5-6.5z"/></svg>
              <span class="select-menu-item-text css-truncate-target js-select-menu-filter-text">
                fixes-for-2.0
              </span>
            </a>
            <a class="select-menu-item js-navigation-item js-navigation-open "
               href="/ckan/ckan/blob/fixing-tests/ckan/config/routing.py"
               data-name="fixing-tests"
               data-skip-pjax="true"
               rel="nofollow">
              <svg aria-hidden="true" class="octicon octicon-check select-menu-item-icon" height="16" version="1.1" viewBox="0 0 12 16" width="12"><path fill-rule="evenodd" d="M12 5l-8 8-4-4 1.5-1.5L4 10l6.5-6.5z"/></svg>
              <span class="select-menu-item-text css-truncate-target js-select-menu-filter-text">
                fixing-tests
              </span>
            </a>
            <a class="select-menu-item js-navigation-item js-navigation-open "
               href="/ckan/ckan/blob/flask-poc/ckan/config/routing.py"
               data-name="flask-poc"
               data-skip-pjax="true"
               rel="nofollow">
              <svg aria-hidden="true" class="octicon octicon-check select-menu-item-icon" height="16" version="1.1" viewBox="0 0 12 16" width="12"><path fill-rule="evenodd" d="M12 5l-8 8-4-4 1.5-1.5L4 10l6.5-6.5z"/></svg>
              <span class="select-menu-item-text css-truncate-target js-select-menu-filter-text">
                flask-poc
              </span>
            </a>
            <a class="select-menu-item js-navigation-item js-navigation-open "
               href="/ckan/ckan/blob/flatten_schema_tidy/ckan/config/routing.py"
               data-name="flatten_schema_tidy"
               data-skip-pjax="true"
               rel="nofollow">
              <svg aria-hidden="true" class="octicon octicon-check select-menu-item-icon" height="16" version="1.1" viewBox="0 0 12 16" width="12"><path fill-rule="evenodd" d="M12 5l-8 8-4-4 1.5-1.5L4 10l6.5-6.5z"/></svg>
              <span class="select-menu-item-text css-truncate-target js-select-menu-filter-text">
                flatten_schema_tidy
              </span>
            </a>
            <a class="select-menu-item js-navigation-item js-navigation-open "
               href="/ckan/ckan/blob/formats_added/ckan/config/routing.py"
               data-name="formats_added"
               data-skip-pjax="true"
               rel="nofollow">
              <svg aria-hidden="true" class="octicon octicon-check select-menu-item-icon" height="16" version="1.1" viewBox="0 0 12 16" width="12"><path fill-rule="evenodd" d="M12 5l-8 8-4-4 1.5-1.5L4 10l6.5-6.5z"/></svg>
              <span class="select-menu-item-text css-truncate-target js-select-menu-filter-text">
                formats_added
              </span>
            </a>
            <a class="select-menu-item js-navigation-item js-navigation-open "
               href="/ckan/ckan/blob/formats/ckan/config/routing.py"
               data-name="formats"
               data-skip-pjax="true"
               rel="nofollow">
              <svg aria-hidden="true" class="octicon octicon-check select-menu-item-icon" height="16" version="1.1" viewBox="0 0 12 16" width="12"><path fill-rule="evenodd" d="M12 5l-8 8-4-4 1.5-1.5L4 10l6.5-6.5z"/></svg>
              <span class="select-menu-item-text css-truncate-target js-select-menu-filter-text">
                formats
              </span>
            </a>
            <a class="select-menu-item js-navigation-item js-navigation-open "
               href="/ckan/ckan/blob/forms/ckan/config/routing.py"
               data-name="forms"
               data-skip-pjax="true"
               rel="nofollow">
              <svg aria-hidden="true" class="octicon octicon-check select-menu-item-icon" height="16" version="1.1" viewBox="0 0 12 16" width="12"><path fill-rule="evenodd" d="M12 5l-8 8-4-4 1.5-1.5L4 10l6.5-6.5z"/></svg>
              <span class="select-menu-item-text css-truncate-target js-select-menu-filter-text">
                forms
              </span>
            </a>
            <a class="select-menu-item js-navigation-item js-navigation-open "
               href="/ckan/ckan/blob/frontend-testing/ckan/config/routing.py"
               data-name="frontend-testing"
               data-skip-pjax="true"
               rel="nofollow">
              <svg aria-hidden="true" class="octicon octicon-check select-menu-item-icon" height="16" version="1.1" viewBox="0 0 12 16" width="12"><path fill-rule="evenodd" d="M12 5l-8 8-4-4 1.5-1.5L4 10l6.5-6.5z"/></svg>
              <span class="select-menu-item-text css-truncate-target js-select-menu-filter-text">
                frontend-testing
              </span>
            </a>
            <a class="select-menu-item js-navigation-item js-navigation-open "
               href="/ckan/ckan/blob/get_package_groups_from_member_table_branched_off_2.0/ckan/config/routing.py"
               data-name="get_package_groups_from_member_table_branched_off_2.0"
               data-skip-pjax="true"
               rel="nofollow">
              <svg aria-hidden="true" class="octicon octicon-check select-menu-item-icon" height="16" version="1.1" viewBox="0 0 12 16" width="12"><path fill-rule="evenodd" d="M12 5l-8 8-4-4 1.5-1.5L4 10l6.5-6.5z"/></svg>
              <span class="select-menu-item-text css-truncate-target js-select-menu-filter-text">
                get_package_groups_from_member_table_branched_off_2.0
              </span>
            </a>
            <a class="select-menu-item js-navigation-item js-navigation-open "
               href="/ckan/ckan/blob/get_package_groups_from_member_table/ckan/config/routing.py"
               data-name="get_package_groups_from_member_table"
               data-skip-pjax="true"
               rel="nofollow">
              <svg aria-hidden="true" class="octicon octicon-check select-menu-item-icon" height="16" version="1.1" viewBox="0 0 12 16" width="12"><path fill-rule="evenodd" d="M12 5l-8 8-4-4 1.5-1.5L4 10l6.5-6.5z"/></svg>
              <span class="select-menu-item-text css-truncate-target js-select-menu-filter-text">
                get_package_groups_from_member_table
              </span>
            </a>
            <a class="select-menu-item js-navigation-item js-navigation-open "
               href="/ckan/ckan/blob/github-issue-template/ckan/config/routing.py"
               data-name="github-issue-template"
               data-skip-pjax="true"
               rel="nofollow">
              <svg aria-hidden="true" class="octicon octicon-check select-menu-item-icon" height="16" version="1.1" viewBox="0 0 12 16" width="12"><path fill-rule="evenodd" d="M12 5l-8 8-4-4 1.5-1.5L4 10l6.5-6.5z"/></svg>
              <span class="select-menu-item-text css-truncate-target js-select-menu-filter-text">
                github-issue-template
              </span>
            </a>
            <a class="select-menu-item js-navigation-item js-navigation-open "
               href="/ckan/ckan/blob/groundrace/ckan/config/routing.py"
               data-name="groundrace"
               data-skip-pjax="true"
               rel="nofollow">
              <svg aria-hidden="true" class="octicon octicon-check select-menu-item-icon" height="16" version="1.1" viewBox="0 0 12 16" width="12"><path fill-rule="evenodd" d="M12 5l-8 8-4-4 1.5-1.5L4 10l6.5-6.5z"/></svg>
              <span class="select-menu-item-text css-truncate-target js-select-menu-filter-text">
                groundrace
              </span>
            </a>
            <a class="select-menu-item js-navigation-item js-navigation-open "
               href="/ckan/ckan/blob/iauthenticator-not-experimental/ckan/config/routing.py"
               data-name="iauthenticator-not-experimental"
               data-skip-pjax="true"
               rel="nofollow">
              <svg aria-hidden="true" class="octicon octicon-check select-menu-item-icon" height="16" version="1.1" viewBox="0 0 12 16" width="12"><path fill-rule="evenodd" d="M12 5l-8 8-4-4 1.5-1.5L4 10l6.5-6.5z"/></svg>
              <span class="select-menu-item-text css-truncate-target js-select-menu-filter-text">
                iauthenticator-not-experimental
              </span>
            </a>
            <a class="select-menu-item js-navigation-item js-navigation-open "
               href="/ckan/ckan/blob/icon-tip/ckan/config/routing.py"
               data-name="icon-tip"
               data-skip-pjax="true"
               rel="nofollow">
              <svg aria-hidden="true" class="octicon octicon-check select-menu-item-icon" height="16" version="1.1" viewBox="0 0 12 16" width="12"><path fill-rule="evenodd" d="M12 5l-8 8-4-4 1.5-1.5L4 10l6.5-6.5z"/></svg>
              <span class="select-menu-item-text css-truncate-target js-select-menu-filter-text">
                icon-tip
              </span>
            </a>
            <a class="select-menu-item js-navigation-item js-navigation-open "
               href="/ckan/ckan/blob/idatasetform-fixes-branched-off-release-v2.0/ckan/config/routing.py"
               data-name="idatasetform-fixes-branched-off-release-v2.0"
               data-skip-pjax="true"
               rel="nofollow">
              <svg aria-hidden="true" class="octicon octicon-check select-menu-item-icon" height="16" version="1.1" viewBox="0 0 12 16" width="12"><path fill-rule="evenodd" d="M12 5l-8 8-4-4 1.5-1.5L4 10l6.5-6.5z"/></svg>
              <span class="select-menu-item-text css-truncate-target js-select-menu-filter-text">
                idatasetform-fixes-branched-off-release-v2.0
              </span>
            </a>
            <a class="select-menu-item js-navigation-item js-navigation-open "
               href="/ckan/ckan/blob/idatasetform-fixes/ckan/config/routing.py"
               data-name="idatasetform-fixes"
               data-skip-pjax="true"
               rel="nofollow">
              <svg aria-hidden="true" class="octicon octicon-check select-menu-item-icon" height="16" version="1.1" viewBox="0 0 12 16" width="12"><path fill-rule="evenodd" d="M12 5l-8 8-4-4 1.5-1.5L4 10l6.5-6.5z"/></svg>
              <span class="select-menu-item-text css-truncate-target js-select-menu-filter-text">
                idatasetform-fixes
              </span>
            </a>
            <a class="select-menu-item js-navigation-item js-navigation-open "
               href="/ckan/ckan/blob/idatasetform-package-schemas-simplification/ckan/config/routing.py"
               data-name="idatasetform-package-schemas-simplification"
               data-skip-pjax="true"
               rel="nofollow">
              <svg aria-hidden="true" class="octicon octicon-check select-menu-item-icon" height="16" version="1.1" viewBox="0 0 12 16" width="12"><path fill-rule="evenodd" d="M12 5l-8 8-4-4 1.5-1.5L4 10l6.5-6.5z"/></svg>
              <span class="select-menu-item-text css-truncate-target js-select-menu-filter-text">
                idatasetform-package-schemas-simplification
              </span>
            </a>
            <a class="select-menu-item js-navigation-item js-navigation-open "
               href="/ckan/ckan/blob/ie-versions/ckan/config/routing.py"
               data-name="ie-versions"
               data-skip-pjax="true"
               rel="nofollow">
              <svg aria-hidden="true" class="octicon octicon-check select-menu-item-icon" height="16" version="1.1" viewBox="0 0 12 16" width="12"><path fill-rule="evenodd" d="M12 5l-8 8-4-4 1.5-1.5L4 10l6.5-6.5z"/></svg>
              <span class="select-menu-item-text css-truncate-target js-select-menu-filter-text">
                ie-versions
              </span>
            </a>
            <a class="select-menu-item js-navigation-item js-navigation-open "
               href="/ckan/ckan/blob/improve-ckanext-template/ckan/config/routing.py"
               data-name="improve-ckanext-template"
               data-skip-pjax="true"
               rel="nofollow">
              <svg aria-hidden="true" class="octicon octicon-check select-menu-item-icon" height="16" version="1.1" viewBox="0 0 12 16" width="12"><path fill-rule="evenodd" d="M12 5l-8 8-4-4 1.5-1.5L4 10l6.5-6.5z"/></svg>
              <span class="select-menu-item-text css-truncate-target js-select-menu-filter-text">
                improve-ckanext-template
              </span>
            </a>
            <a class="select-menu-item js-navigation-item js-navigation-open "
               href="/ckan/ckan/blob/improve-datapusher-error-messages/ckan/config/routing.py"
               data-name="improve-datapusher-error-messages"
               data-skip-pjax="true"
               rel="nofollow">
              <svg aria-hidden="true" class="octicon octicon-check select-menu-item-icon" height="16" version="1.1" viewBox="0 0 12 16" width="12"><path fill-rule="evenodd" d="M12 5l-8 8-4-4 1.5-1.5L4 10l6.5-6.5z"/></svg>
              <span class="select-menu-item-text css-truncate-target js-select-menu-filter-text">
                improve-datapusher-error-messages
              </span>
            </a>
            <a class="select-menu-item js-navigation-item js-navigation-open "
               href="/ckan/ckan/blob/installing-docs-title-fixes/ckan/config/routing.py"
               data-name="installing-docs-title-fixes"
               data-skip-pjax="true"
               rel="nofollow">
              <svg aria-hidden="true" class="octicon octicon-check select-menu-item-icon" height="16" version="1.1" viewBox="0 0 12 16" width="12"><path fill-rule="evenodd" d="M12 5l-8 8-4-4 1.5-1.5L4 10l6.5-6.5z"/></svg>
              <span class="select-menu-item-text css-truncate-target js-select-menu-filter-text">
                installing-docs-title-fixes
              </span>
            </a>
            <a class="select-menu-item js-navigation-item js-navigation-open "
               href="/ckan/ckan/blob/internal-tracking-cleanup/ckan/config/routing.py"
               data-name="internal-tracking-cleanup"
               data-skip-pjax="true"
               rel="nofollow">
              <svg aria-hidden="true" class="octicon octicon-check select-menu-item-icon" height="16" version="1.1" viewBox="0 0 12 16" width="12"><path fill-rule="evenodd" d="M12 5l-8 8-4-4 1.5-1.5L4 10l6.5-6.5z"/></svg>
              <span class="select-menu-item-text css-truncate-target js-select-menu-filter-text">
                internal-tracking-cleanup
              </span>
            </a>
            <a class="select-menu-item js-navigation-item js-navigation-open "
               href="/ckan/ckan/blob/kata-csc-2125-add-organization-autocomplete/ckan/config/routing.py"
               data-name="kata-csc-2125-add-organization-autocomplete"
               data-skip-pjax="true"
               rel="nofollow">
              <svg aria-hidden="true" class="octicon octicon-check select-menu-item-icon" height="16" version="1.1" viewBox="0 0 12 16" width="12"><path fill-rule="evenodd" d="M12 5l-8 8-4-4 1.5-1.5L4 10l6.5-6.5z"/></svg>
              <span class="select-menu-item-text css-truncate-target js-select-menu-filter-text">
                kata-csc-2125-add-organization-autocomplete
              </span>
            </a>
            <a class="select-menu-item js-navigation-item js-navigation-open "
               href="/ckan/ckan/blob/latest-okfn-sphinx-theme/ckan/config/routing.py"
               data-name="latest-okfn-sphinx-theme"
               data-skip-pjax="true"
               rel="nofollow">
              <svg aria-hidden="true" class="octicon octicon-check select-menu-item-icon" height="16" version="1.1" viewBox="0 0 12 16" width="12"><path fill-rule="evenodd" d="M12 5l-8 8-4-4 1.5-1.5L4 10l6.5-6.5z"/></svg>
              <span class="select-menu-item-text css-truncate-target js-select-menu-filter-text">
                latest-okfn-sphinx-theme
              </span>
            </a>
            <a class="select-menu-item js-navigation-item js-navigation-open "
               href="/ckan/ckan/blob/license-118n/ckan/config/routing.py"
               data-name="license-118n"
               data-skip-pjax="true"
               rel="nofollow">
              <svg aria-hidden="true" class="octicon octicon-check select-menu-item-icon" height="16" version="1.1" viewBox="0 0 12 16" width="12"><path fill-rule="evenodd" d="M12 5l-8 8-4-4 1.5-1.5L4 10l6.5-6.5z"/></svg>
              <span class="select-menu-item-text css-truncate-target js-select-menu-filter-text">
                license-118n
              </span>
            </a>
            <a class="select-menu-item js-navigation-item js-navigation-open "
               href="/ckan/ckan/blob/local-storage-url-bug/ckan/config/routing.py"
               data-name="local-storage-url-bug"
               data-skip-pjax="true"
               rel="nofollow">
              <svg aria-hidden="true" class="octicon octicon-check select-menu-item-icon" height="16" version="1.1" viewBox="0 0 12 16" width="12"><path fill-rule="evenodd" d="M12 5l-8 8-4-4 1.5-1.5L4 10l6.5-6.5z"/></svg>
              <span class="select-menu-item-text css-truncate-target js-select-menu-filter-text">
                local-storage-url-bug
              </span>
            </a>
            <a class="select-menu-item js-navigation-item js-navigation-open "
               href="/ckan/ckan/blob/markdown-fix/ckan/config/routing.py"
               data-name="markdown-fix"
               data-skip-pjax="true"
               rel="nofollow">
              <svg aria-hidden="true" class="octicon octicon-check select-menu-item-icon" height="16" version="1.1" viewBox="0 0 12 16" width="12"><path fill-rule="evenodd" d="M12 5l-8 8-4-4 1.5-1.5L4 10l6.5-6.5z"/></svg>
              <span class="select-menu-item-text css-truncate-target js-select-menu-filter-text">
                markdown-fix
              </span>
            </a>
            <a class="select-menu-item js-navigation-item js-navigation-open selected"
               href="/ckan/ckan/blob/master/ckan/config/routing.py"
               data-name="master"
               data-skip-pjax="true"
               rel="nofollow">
              <svg aria-hidden="true" class="octicon octicon-check select-menu-item-icon" height="16" version="1.1" viewBox="0 0 12 16" width="12"><path fill-rule="evenodd" d="M12 5l-8 8-4-4 1.5-1.5L4 10l6.5-6.5z"/></svg>
              <span class="select-menu-item-text css-truncate-target js-select-menu-filter-text">
                master
              </span>
            </a>
            <a class="select-menu-item js-navigation-item js-navigation-open "
               href="/ckan/ckan/blob/metastable/ckan/config/routing.py"
               data-name="metastable"
               data-skip-pjax="true"
               rel="nofollow">
              <svg aria-hidden="true" class="octicon octicon-check select-menu-item-icon" height="16" version="1.1" viewBox="0 0 12 16" width="12"><path fill-rule="evenodd" d="M12 5l-8 8-4-4 1.5-1.5L4 10l6.5-6.5z"/></svg>
              <span class="select-menu-item-text css-truncate-target js-select-menu-filter-text">
                metastable
              </span>
            </a>
            <a class="select-menu-item js-navigation-item js-navigation-open "
               href="/ckan/ckan/blob/minor-activity-doc-tweaks/ckan/config/routing.py"
               data-name="minor-activity-doc-tweaks"
               data-skip-pjax="true"
               rel="nofollow">
              <svg aria-hidden="true" class="octicon octicon-check select-menu-item-icon" height="16" version="1.1" viewBox="0 0 12 16" width="12"><path fill-rule="evenodd" d="M12 5l-8 8-4-4 1.5-1.5L4 10l6.5-6.5z"/></svg>
              <span class="select-menu-item-text css-truncate-target js-select-menu-filter-text">
                minor-activity-doc-tweaks
              </span>
            </a>
            <a class="select-menu-item js-navigation-item js-navigation-open "
               href="/ckan/ckan/blob/minor-docs-fix/ckan/config/routing.py"
               data-name="minor-docs-fix"
               data-skip-pjax="true"
               rel="nofollow">
              <svg aria-hidden="true" class="octicon octicon-check select-menu-item-icon" height="16" version="1.1" viewBox="0 0 12 16" width="12"><path fill-rule="evenodd" d="M12 5l-8 8-4-4 1.5-1.5L4 10l6.5-6.5z"/></svg>
              <span class="select-menu-item-text css-truncate-target js-select-menu-filter-text">
                minor-docs-fix
              </span>
            </a>
            <a class="select-menu-item js-navigation-item js-navigation-open "
               href="/ckan/ckan/blob/mstantoncook-docs-solr-ubuntu-14.04-fix/ckan/config/routing.py"
               data-name="mstantoncook-docs-solr-ubuntu-14.04-fix"
               data-skip-pjax="true"
               rel="nofollow">
              <svg aria-hidden="true" class="octicon octicon-check select-menu-item-icon" height="16" version="1.1" viewBox="0 0 12 16" width="12"><path fill-rule="evenodd" d="M12 5l-8 8-4-4 1.5-1.5L4 10l6.5-6.5z"/></svg>
              <span class="select-menu-item-text css-truncate-target js-select-menu-filter-text">
                mstantoncook-docs-solr-ubuntu-14.04-fix
              </span>
            </a>
            <a class="select-menu-item js-navigation-item js-navigation-open "
               href="/ckan/ckan/blob/multiline-datapusher-output/ckan/config/routing.py"
               data-name="multiline-datapusher-output"
               data-skip-pjax="true"
               rel="nofollow">
              <svg aria-hidden="true" class="octicon octicon-check select-menu-item-icon" height="16" version="1.1" viewBox="0 0 12 16" width="12"><path fill-rule="evenodd" d="M12 5l-8 8-4-4 1.5-1.5L4 10l6.5-6.5z"/></svg>
              <span class="select-menu-item-text css-truncate-target js-select-menu-filter-text">
                multiline-datapusher-output
              </span>
            </a>
            <a class="select-menu-item js-navigation-item js-navigation-open "
               href="/ckan/ckan/blob/multilingual-plugin-crashes-paster-commands/ckan/config/routing.py"
               data-name="multilingual-plugin-crashes-paster-commands"
               data-skip-pjax="true"
               rel="nofollow">
              <svg aria-hidden="true" class="octicon octicon-check select-menu-item-icon" height="16" version="1.1" viewBox="0 0 12 16" width="12"><path fill-rule="evenodd" d="M12 5l-8 8-4-4 1.5-1.5L4 10l6.5-6.5z"/></svg>
              <span class="select-menu-item-text css-truncate-target js-select-menu-filter-text">
                multilingual-plugin-crashes-paster-commands
              </span>
            </a>
            <a class="select-menu-item js-navigation-item js-navigation-open "
               href="/ckan/ckan/blob/multilingual-schema-update/ckan/config/routing.py"
               data-name="multilingual-schema-update"
               data-skip-pjax="true"
               rel="nofollow">
              <svg aria-hidden="true" class="octicon octicon-check select-menu-item-icon" height="16" version="1.1" viewBox="0 0 12 16" width="12"><path fill-rule="evenodd" d="M12 5l-8 8-4-4 1.5-1.5L4 10l6.5-6.5z"/></svg>
              <span class="select-menu-item-text css-truncate-target js-select-menu-filter-text">
                multilingual-schema-update
              </span>
            </a>
            <a class="select-menu-item js-navigation-item js-navigation-open "
               href="/ckan/ckan/blob/munge-asserts/ckan/config/routing.py"
               data-name="munge-asserts"
               data-skip-pjax="true"
               rel="nofollow">
              <svg aria-hidden="true" class="octicon octicon-check select-menu-item-icon" height="16" version="1.1" viewBox="0 0 12 16" width="12"><path fill-rule="evenodd" d="M12 5l-8 8-4-4 1.5-1.5L4 10l6.5-6.5z"/></svg>
              <span class="select-menu-item-text css-truncate-target js-select-menu-filter-text">
                munge-asserts
              </span>
            </a>
            <a class="select-menu-item js-navigation-item js-navigation-open "
               href="/ckan/ckan/blob/munge-improve/ckan/config/routing.py"
               data-name="munge-improve"
               data-skip-pjax="true"
               rel="nofollow">
              <svg aria-hidden="true" class="octicon octicon-check select-menu-item-icon" height="16" version="1.1" viewBox="0 0 12 16" width="12"><path fill-rule="evenodd" d="M12 5l-8 8-4-4 1.5-1.5L4 10l6.5-6.5z"/></svg>
              <span class="select-menu-item-text css-truncate-target js-select-menu-filter-text">
                munge-improve
              </span>
            </a>
            <a class="select-menu-item js-navigation-item js-navigation-open "
               href="/ckan/ckan/blob/name-validator-exception-for-preexisting-usernames/ckan/config/routing.py"
               data-name="name-validator-exception-for-preexisting-usernames"
               data-skip-pjax="true"
               rel="nofollow">
              <svg aria-hidden="true" class="octicon octicon-check select-menu-item-icon" height="16" version="1.1" viewBox="0 0 12 16" width="12"><path fill-rule="evenodd" d="M12 5l-8 8-4-4 1.5-1.5L4 10l6.5-6.5z"/></svg>
              <span class="select-menu-item-text css-truncate-target js-select-menu-filter-text">
                name-validator-exception-for-preexisting-usernames
              </span>
            </a>
            <a class="select-menu-item js-navigation-item js-navigation-open "
               href="/ckan/ckan/blob/new-rtd-default-docs-theme/ckan/config/routing.py"
               data-name="new-rtd-default-docs-theme"
               data-skip-pjax="true"
               rel="nofollow">
              <svg aria-hidden="true" class="octicon octicon-check select-menu-item-icon" height="16" version="1.1" viewBox="0 0 12 16" width="12"><path fill-rule="evenodd" d="M12 5l-8 8-4-4 1.5-1.5L4 10l6.5-6.5z"/></svg>
              <span class="select-menu-item-text css-truncate-target js-select-menu-filter-text">
                new-rtd-default-docs-theme
              </span>
            </a>
            <a class="select-menu-item js-navigation-item js-navigation-open "
               href="/ckan/ckan/blob/nicer-validation-errors/ckan/config/routing.py"
               data-name="nicer-validation-errors"
               data-skip-pjax="true"
               rel="nofollow">
              <svg aria-hidden="true" class="octicon octicon-check select-menu-item-icon" height="16" version="1.1" viewBox="0 0 12 16" width="12"><path fill-rule="evenodd" d="M12 5l-8 8-4-4 1.5-1.5L4 10l6.5-6.5z"/></svg>
              <span class="select-menu-item-text css-truncate-target js-select-menu-filter-text">
                nicer-validation-errors
              </span>
            </a>
            <a class="select-menu-item js-navigation-item js-navigation-open "
               href="/ckan/ckan/blob/noisy-logging/ckan/config/routing.py"
               data-name="noisy-logging"
               data-skip-pjax="true"
               rel="nofollow">
              <svg aria-hidden="true" class="octicon octicon-check select-menu-item-icon" height="16" version="1.1" viewBox="0 0 12 16" width="12"><path fill-rule="evenodd" d="M12 5l-8 8-4-4 1.5-1.5L4 10l6.5-6.5z"/></svg>
              <span class="select-menu-item-text css-truncate-target js-select-menu-filter-text">
                noisy-logging
              </span>
            </a>
            <a class="select-menu-item js-navigation-item js-navigation-open "
               href="/ckan/ckan/blob/notification-errors/ckan/config/routing.py"
               data-name="notification-errors"
               data-skip-pjax="true"
               rel="nofollow">
              <svg aria-hidden="true" class="octicon octicon-check select-menu-item-icon" height="16" version="1.1" viewBox="0 0 12 16" width="12"><path fill-rule="evenodd" d="M12 5l-8 8-4-4 1.5-1.5L4 10l6.5-6.5z"/></svg>
              <span class="select-menu-item-text css-truncate-target js-select-menu-filter-text">
                notification-errors
              </span>
            </a>
            <a class="select-menu-item js-navigation-item js-navigation-open "
               href="/ckan/ckan/blob/okf-summit-2013-example-tests/ckan/config/routing.py"
               data-name="okf-summit-2013-example-tests"
               data-skip-pjax="true"
               rel="nofollow">
              <svg aria-hidden="true" class="octicon octicon-check select-menu-item-icon" height="16" version="1.1" viewBox="0 0 12 16" width="12"><path fill-rule="evenodd" d="M12 5l-8 8-4-4 1.5-1.5L4 10l6.5-6.5z"/></svg>
              <span class="select-menu-item-text css-truncate-target js-select-menu-filter-text">
                okf-summit-2013-example-tests
              </span>
            </a>
            <a class="select-menu-item js-navigation-item js-navigation-open "
               href="/ckan/ckan/blob/open-id-removal/ckan/config/routing.py"
               data-name="open-id-removal"
               data-skip-pjax="true"
               rel="nofollow">
              <svg aria-hidden="true" class="octicon octicon-check select-menu-item-icon" height="16" version="1.1" viewBox="0 0 12 16" width="12"><path fill-rule="evenodd" d="M12 5l-8 8-4-4 1.5-1.5L4 10l6.5-6.5z"/></svg>
              <span class="select-menu-item-text css-truncate-target js-select-menu-filter-text">
                open-id-removal
              </span>
            </a>
            <a class="select-menu-item js-navigation-item js-navigation-open "
               href="/ckan/ckan/blob/organizations-in-core/ckan/config/routing.py"
               data-name="organizations-in-core"
               data-skip-pjax="true"
               rel="nofollow">
              <svg aria-hidden="true" class="octicon octicon-check select-menu-item-icon" height="16" version="1.1" viewBox="0 0 12 16" width="12"><path fill-rule="evenodd" d="M12 5l-8 8-4-4 1.5-1.5L4 10l6.5-6.5z"/></svg>
              <span class="select-menu-item-text css-truncate-target js-select-menu-filter-text">
                organizations-in-core
              </span>
            </a>
            <a class="select-menu-item js-navigation-item js-navigation-open "
               href="/ckan/ckan/blob/pep8-lib-helpers/ckan/config/routing.py"
               data-name="pep8-lib-helpers"
               data-skip-pjax="true"
               rel="nofollow">
              <svg aria-hidden="true" class="octicon octicon-check select-menu-item-icon" height="16" version="1.1" viewBox="0 0 12 16" width="12"><path fill-rule="evenodd" d="M12 5l-8 8-4-4 1.5-1.5L4 10l6.5-6.5z"/></svg>
              <span class="select-menu-item-text css-truncate-target js-select-menu-filter-text">
                pep8-lib-helpers
              </span>
            </a>
            <a class="select-menu-item js-navigation-item js-navigation-open "
               href="/ckan/ckan/blob/pep8-tidy/ckan/config/routing.py"
               data-name="pep8-tidy"
               data-skip-pjax="true"
               rel="nofollow">
              <svg aria-hidden="true" class="octicon octicon-check select-menu-item-icon" height="16" version="1.1" viewBox="0 0 12 16" width="12"><path fill-rule="evenodd" d="M12 5l-8 8-4-4 1.5-1.5L4 10l6.5-6.5z"/></svg>
              <span class="select-menu-item-text css-truncate-target js-select-menu-filter-text">
                pep8-tidy
              </span>
            </a>
            <a class="select-menu-item js-navigation-item js-navigation-open "
               href="/ckan/ckan/blob/pluginsfull/ckan/config/routing.py"
               data-name="pluginsfull"
               data-skip-pjax="true"
               rel="nofollow">
              <svg aria-hidden="true" class="octicon octicon-check select-menu-item-icon" height="16" version="1.1" viewBox="0 0 12 16" width="12"><path fill-rule="evenodd" d="M12 5l-8 8-4-4 1.5-1.5L4 10l6.5-6.5z"/></svg>
              <span class="select-menu-item-text css-truncate-target js-select-menu-filter-text">
                pluginsfull
              </span>
            </a>
            <a class="select-menu-item js-navigation-item js-navigation-open "
               href="/ckan/ckan/blob/poc-flask-views.blueprint/ckan/config/routing.py"
               data-name="poc-flask-views.blueprint"
               data-skip-pjax="true"
               rel="nofollow">
              <svg aria-hidden="true" class="octicon octicon-check select-menu-item-icon" height="16" version="1.1" viewBox="0 0 12 16" width="12"><path fill-rule="evenodd" d="M12 5l-8 8-4-4 1.5-1.5L4 10l6.5-6.5z"/></svg>
              <span class="select-menu-item-text css-truncate-target js-select-menu-filter-text">
                poc-flask-views.blueprint
              </span>
            </a>
            <a class="select-menu-item js-navigation-item js-navigation-open "
               href="/ckan/ckan/blob/poc-flask-views.c/ckan/config/routing.py"
               data-name="poc-flask-views.c"
               data-skip-pjax="true"
               rel="nofollow">
              <svg aria-hidden="true" class="octicon octicon-check select-menu-item-icon" height="16" version="1.1" viewBox="0 0 12 16" width="12"><path fill-rule="evenodd" d="M12 5l-8 8-4-4 1.5-1.5L4 10l6.5-6.5z"/></svg>
              <span class="select-menu-item-text css-truncate-target js-select-menu-filter-text">
                poc-flask-views.c
              </span>
            </a>
            <a class="select-menu-item js-navigation-item js-navigation-open "
               href="/ckan/ckan/blob/poc-flask-views.common-url_for-take-2-tests/ckan/config/routing.py"
               data-name="poc-flask-views.common-url_for-take-2-tests"
               data-skip-pjax="true"
               rel="nofollow">
              <svg aria-hidden="true" class="octicon octicon-check select-menu-item-icon" height="16" version="1.1" viewBox="0 0 12 16" width="12"><path fill-rule="evenodd" d="M12 5l-8 8-4-4 1.5-1.5L4 10l6.5-6.5z"/></svg>
              <span class="select-menu-item-text css-truncate-target js-select-menu-filter-text">
                poc-flask-views.common-url_for-take-2-tests
              </span>
            </a>
            <a class="select-menu-item js-navigation-item js-navigation-open "
               href="/ckan/ckan/blob/poc-flask-views.common-url_for-take-2/ckan/config/routing.py"
               data-name="poc-flask-views.common-url_for-take-2"
               data-skip-pjax="true"
               rel="nofollow">
              <svg aria-hidden="true" class="octicon octicon-check select-menu-item-icon" height="16" version="1.1" viewBox="0 0 12 16" width="12"><path fill-rule="evenodd" d="M12 5l-8 8-4-4 1.5-1.5L4 10l6.5-6.5z"/></svg>
              <span class="select-menu-item-text css-truncate-target js-select-menu-filter-text">
                poc-flask-views.common-url_for-take-2
              </span>
            </a>
            <a class="select-menu-item js-navigation-item js-navigation-open "
               href="/ckan/ckan/blob/poc-flask-views.config/ckan/config/routing.py"
               data-name="poc-flask-views.config"
               data-skip-pjax="true"
               rel="nofollow">
              <svg aria-hidden="true" class="octicon octicon-check select-menu-item-icon" height="16" version="1.1" viewBox="0 0 12 16" width="12"><path fill-rule="evenodd" d="M12 5l-8 8-4-4 1.5-1.5L4 10l6.5-6.5z"/></svg>
              <span class="select-menu-item-text css-truncate-target js-select-menu-filter-text">
                poc-flask-views.config
              </span>
            </a>
            <a class="select-menu-item js-navigation-item js-navigation-open "
               href="/ckan/ckan/blob/poc-flask-views.middleware/ckan/config/routing.py"
               data-name="poc-flask-views.middleware"
               data-skip-pjax="true"
               rel="nofollow">
              <svg aria-hidden="true" class="octicon octicon-check select-menu-item-icon" height="16" version="1.1" viewBox="0 0 12 16" width="12"><path fill-rule="evenodd" d="M12 5l-8 8-4-4 1.5-1.5L4 10l6.5-6.5z"/></svg>
              <span class="select-menu-item-text css-truncate-target js-select-menu-filter-text">
                poc-flask-views.middleware
              </span>
            </a>
            <a class="select-menu-item js-navigation-item js-navigation-open "
               href="/ckan/ckan/blob/poc-flask-views/ckan/config/routing.py"
               data-name="poc-flask-views"
               data-skip-pjax="true"
               rel="nofollow">
              <svg aria-hidden="true" class="octicon octicon-check select-menu-item-icon" height="16" version="1.1" viewBox="0 0 12 16" width="12"><path fill-rule="evenodd" d="M12 5l-8 8-4-4 1.5-1.5L4 10l6.5-6.5z"/></svg>
              <span class="select-menu-item-text css-truncate-target js-select-menu-filter-text">
                poc-flask-views
              </span>
            </a>
            <a class="select-menu-item js-navigation-item js-navigation-open "
               href="/ckan/ckan/blob/purge_solr/ckan/config/routing.py"
               data-name="purge_solr"
               data-skip-pjax="true"
               rel="nofollow">
              <svg aria-hidden="true" class="octicon octicon-check select-menu-item-icon" height="16" version="1.1" viewBox="0 0 12 16" width="12"><path fill-rule="evenodd" d="M12 5l-8 8-4-4 1.5-1.5L4 10l6.5-6.5z"/></svg>
              <span class="select-menu-item-text css-truncate-target js-select-menu-filter-text">
                purge_solr
              </span>
            </a>
            <a class="select-menu-item js-navigation-item js-navigation-open "
               href="/ckan/ckan/blob/raise-better/ckan/config/routing.py"
               data-name="raise-better"
               data-skip-pjax="true"
               rel="nofollow">
              <svg aria-hidden="true" class="octicon octicon-check select-menu-item-icon" height="16" version="1.1" viewBox="0 0 12 16" width="12"><path fill-rule="evenodd" d="M12 5l-8 8-4-4 1.5-1.5L4 10l6.5-6.5z"/></svg>
              <span class="select-menu-item-text css-truncate-target js-select-menu-filter-text">
                raise-better
              </span>
            </a>
            <a class="select-menu-item js-navigation-item js-navigation-open "
               href="/ckan/ckan/blob/rdf-template-fix/ckan/config/routing.py"
               data-name="rdf-template-fix"
               data-skip-pjax="true"
               rel="nofollow">
              <svg aria-hidden="true" class="octicon octicon-check select-menu-item-icon" height="16" version="1.1" viewBox="0 0 12 16" width="12"><path fill-rule="evenodd" d="M12 5l-8 8-4-4 1.5-1.5L4 10l6.5-6.5z"/></svg>
              <span class="select-menu-item-text css-truncate-target js-select-menu-filter-text">
                rdf-template-fix
              </span>
            </a>
            <a class="select-menu-item js-navigation-item js-navigation-open "
               href="/ckan/ckan/blob/reactivate-solr-sorting-test/ckan/config/routing.py"
               data-name="reactivate-solr-sorting-test"
               data-skip-pjax="true"
               rel="nofollow">
              <svg aria-hidden="true" class="octicon octicon-check select-menu-item-icon" height="16" version="1.1" viewBox="0 0 12 16" width="12"><path fill-rule="evenodd" d="M12 5l-8 8-4-4 1.5-1.5L4 10l6.5-6.5z"/></svg>
              <span class="select-menu-item-text css-truncate-target js-select-menu-filter-text">
                reactivate-solr-sorting-test
              </span>
            </a>
            <a class="select-menu-item js-navigation-item js-navigation-open "
               href="/ckan/ckan/blob/refactor-1282-js-wui-cruft/ckan/config/routing.py"
               data-name="refactor-1282-js-wui-cruft"
               data-skip-pjax="true"
               rel="nofollow">
              <svg aria-hidden="true" class="octicon octicon-check select-menu-item-icon" height="16" version="1.1" viewBox="0 0 12 16" width="12"><path fill-rule="evenodd" d="M12 5l-8 8-4-4 1.5-1.5L4 10l6.5-6.5z"/></svg>
              <span class="select-menu-item-text css-truncate-target js-select-menu-filter-text">
                refactor-1282-js-wui-cruft
              </span>
            </a>
            <a class="select-menu-item js-navigation-item js-navigation-open "
               href="/ckan/ckan/blob/refactor-dashboard-tests/ckan/config/routing.py"
               data-name="refactor-dashboard-tests"
               data-skip-pjax="true"
               rel="nofollow">
              <svg aria-hidden="true" class="octicon octicon-check select-menu-item-icon" height="16" version="1.1" viewBox="0 0 12 16" width="12"><path fill-rule="evenodd" d="M12 5l-8 8-4-4 1.5-1.5L4 10l6.5-6.5z"/></svg>
              <span class="select-menu-item-text css-truncate-target js-select-menu-filter-text">
                refactor-dashboard-tests
              </span>
            </a>
            <a class="select-menu-item js-navigation-item js-navigation-open "
               href="/ckan/ckan/blob/related-list-test-failure/ckan/config/routing.py"
               data-name="related-list-test-failure"
               data-skip-pjax="true"
               rel="nofollow">
              <svg aria-hidden="true" class="octicon octicon-check select-menu-item-icon" height="16" version="1.1" viewBox="0 0 12 16" width="12"><path fill-rule="evenodd" d="M12 5l-8 8-4-4 1.5-1.5L4 10l6.5-6.5z"/></svg>
              <span class="select-menu-item-text css-truncate-target js-select-menu-filter-text">
                related-list-test-failure
              </span>
            </a>
            <a class="select-menu-item js-navigation-item js-navigation-open "
               href="/ckan/ckan/blob/related-title-fix/ckan/config/routing.py"
               data-name="related-title-fix"
               data-skip-pjax="true"
               rel="nofollow">
              <svg aria-hidden="true" class="octicon octicon-check select-menu-item-icon" height="16" version="1.1" viewBox="0 0 12 16" width="12"><path fill-rule="evenodd" d="M12 5l-8 8-4-4 1.5-1.5L4 10l6.5-6.5z"/></svg>
              <span class="select-menu-item-text css-truncate-target js-select-menu-filter-text">
                related-title-fix
              </span>
            </a>
            <a class="select-menu-item js-navigation-item js-navigation-open "
               href="/ckan/ckan/blob/release-datagov-saml2/ckan/config/routing.py"
               data-name="release-datagov-saml2"
               data-skip-pjax="true"
               rel="nofollow">
              <svg aria-hidden="true" class="octicon octicon-check select-menu-item-icon" height="16" version="1.1" viewBox="0 0 12 16" width="12"><path fill-rule="evenodd" d="M12 5l-8 8-4-4 1.5-1.5L4 10l6.5-6.5z"/></svg>
              <span class="select-menu-item-text css-truncate-target js-select-menu-filter-text">
                release-datagov-saml2
              </span>
            </a>
            <a class="select-menu-item js-navigation-item js-navigation-open "
               href="/ckan/ckan/blob/release-datagov/ckan/config/routing.py"
               data-name="release-datagov"
               data-skip-pjax="true"
               rel="nofollow">
              <svg aria-hidden="true" class="octicon octicon-check select-menu-item-icon" height="16" version="1.1" viewBox="0 0 12 16" width="12"><path fill-rule="evenodd" d="M12 5l-8 8-4-4 1.5-1.5L4 10l6.5-6.5z"/></svg>
              <span class="select-menu-item-text css-truncate-target js-select-menu-filter-text">
                release-datagov
              </span>
            </a>
            <a class="select-menu-item js-navigation-item js-navigation-open "
               href="/ckan/ckan/blob/release-dgu1/ckan/config/routing.py"
               data-name="release-dgu1"
               data-skip-pjax="true"
               rel="nofollow">
              <svg aria-hidden="true" class="octicon octicon-check select-menu-item-icon" height="16" version="1.1" viewBox="0 0 12 16" width="12"><path fill-rule="evenodd" d="M12 5l-8 8-4-4 1.5-1.5L4 10l6.5-6.5z"/></svg>
              <span class="select-menu-item-text css-truncate-target js-select-menu-filter-text">
                release-dgu1
              </span>
            </a>
            <a class="select-menu-item js-navigation-item js-navigation-open "
               href="/ckan/ckan/blob/release-learnings/ckan/config/routing.py"
               data-name="release-learnings"
               data-skip-pjax="true"
               rel="nofollow">
              <svg aria-hidden="true" class="octicon octicon-check select-menu-item-icon" height="16" version="1.1" viewBox="0 0 12 16" width="12"><path fill-rule="evenodd" d="M12 5l-8 8-4-4 1.5-1.5L4 10l6.5-6.5z"/></svg>
              <span class="select-menu-item-text css-truncate-target js-select-menu-filter-text">
                release-learnings
              </span>
            </a>
            <a class="select-menu-item js-navigation-item js-navigation-open "
               href="/ckan/ckan/blob/release-process/ckan/config/routing.py"
               data-name="release-process"
               data-skip-pjax="true"
               rel="nofollow">
              <svg aria-hidden="true" class="octicon octicon-check select-menu-item-icon" height="16" version="1.1" viewBox="0 0 12 16" width="12"><path fill-rule="evenodd" d="M12 5l-8 8-4-4 1.5-1.5L4 10l6.5-6.5z"/></svg>
              <span class="select-menu-item-text css-truncate-target js-select-menu-filter-text">
                release-process
              </span>
            </a>
            <a class="select-menu-item js-navigation-item js-navigation-open "
               href="/ckan/ckan/blob/release-test-2.1-with-1149/ckan/config/routing.py"
               data-name="release-test-2.1-with-1149"
               data-skip-pjax="true"
               rel="nofollow">
              <svg aria-hidden="true" class="octicon octicon-check select-menu-item-icon" height="16" version="1.1" viewBox="0 0 12 16" width="12"><path fill-rule="evenodd" d="M12 5l-8 8-4-4 1.5-1.5L4 10l6.5-6.5z"/></svg>
              <span class="select-menu-item-text css-truncate-target js-select-menu-filter-text">
                release-test-2.1-with-1149
              </span>
            </a>
            <a class="select-menu-item js-navigation-item js-navigation-open "
               href="/ckan/ckan/blob/release-v1.3.1/ckan/config/routing.py"
               data-name="release-v1.3.1"
               data-skip-pjax="true"
               rel="nofollow">
              <svg aria-hidden="true" class="octicon octicon-check select-menu-item-icon" height="16" version="1.1" viewBox="0 0 12 16" width="12"><path fill-rule="evenodd" d="M12 5l-8 8-4-4 1.5-1.5L4 10l6.5-6.5z"/></svg>
              <span class="select-menu-item-text css-truncate-target js-select-menu-filter-text">
                release-v1.3.1
              </span>
            </a>
            <a class="select-menu-item js-navigation-item js-navigation-open "
               href="/ckan/ckan/blob/release-v1.3.2/ckan/config/routing.py"
               data-name="release-v1.3.2"
               data-skip-pjax="true"
               rel="nofollow">
              <svg aria-hidden="true" class="octicon octicon-check select-menu-item-icon" height="16" version="1.1" viewBox="0 0 12 16" width="12"><path fill-rule="evenodd" d="M12 5l-8 8-4-4 1.5-1.5L4 10l6.5-6.5z"/></svg>
              <span class="select-menu-item-text css-truncate-target js-select-menu-filter-text">
                release-v1.3.2
              </span>
            </a>
            <a class="select-menu-item js-navigation-item js-navigation-open "
               href="/ckan/ckan/blob/release-v1.3.3/ckan/config/routing.py"
               data-name="release-v1.3.3"
               data-skip-pjax="true"
               rel="nofollow">
              <svg aria-hidden="true" class="octicon octicon-check select-menu-item-icon" height="16" version="1.1" viewBox="0 0 12 16" width="12"><path fill-rule="evenodd" d="M12 5l-8 8-4-4 1.5-1.5L4 10l6.5-6.5z"/></svg>
              <span class="select-menu-item-text css-truncate-target js-select-menu-filter-text">
                release-v1.3.3
              </span>
            </a>
            <a class="select-menu-item js-navigation-item js-navigation-open "
               href="/ckan/ckan/blob/release-v1.3.4/ckan/config/routing.py"
               data-name="release-v1.3.4"
               data-skip-pjax="true"
               rel="nofollow">
              <svg aria-hidden="true" class="octicon octicon-check select-menu-item-icon" height="16" version="1.1" viewBox="0 0 12 16" width="12"><path fill-rule="evenodd" d="M12 5l-8 8-4-4 1.5-1.5L4 10l6.5-6.5z"/></svg>
              <span class="select-menu-item-text css-truncate-target js-select-menu-filter-text">
                release-v1.3.4
              </span>
            </a>
            <a class="select-menu-item js-navigation-item js-navigation-open "
               href="/ckan/ckan/blob/release-v1.3.4.1/ckan/config/routing.py"
               data-name="release-v1.3.4.1"
               data-skip-pjax="true"
               rel="nofollow">
              <svg aria-hidden="true" class="octicon octicon-check select-menu-item-icon" height="16" version="1.1" viewBox="0 0 12 16" width="12"><path fill-rule="evenodd" d="M12 5l-8 8-4-4 1.5-1.5L4 10l6.5-6.5z"/></svg>
              <span class="select-menu-item-text css-truncate-target js-select-menu-filter-text">
                release-v1.3.4.1
              </span>
            </a>
            <a class="select-menu-item js-navigation-item js-navigation-open "
               href="/ckan/ckan/blob/release-v1.3.5/ckan/config/routing.py"
               data-name="release-v1.3.5"
               data-skip-pjax="true"
               rel="nofollow">
              <svg aria-hidden="true" class="octicon octicon-check select-menu-item-icon" height="16" version="1.1" viewBox="0 0 12 16" width="12"><path fill-rule="evenodd" d="M12 5l-8 8-4-4 1.5-1.5L4 10l6.5-6.5z"/></svg>
              <span class="select-menu-item-text css-truncate-target js-select-menu-filter-text">
                release-v1.3.5
              </span>
            </a>
            <a class="select-menu-item js-navigation-item js-navigation-open "
               href="/ckan/ckan/blob/release-v1.4/ckan/config/routing.py"
               data-name="release-v1.4"
               data-skip-pjax="true"
               rel="nofollow">
              <svg aria-hidden="true" class="octicon octicon-check select-menu-item-icon" height="16" version="1.1" viewBox="0 0 12 16" width="12"><path fill-rule="evenodd" d="M12 5l-8 8-4-4 1.5-1.5L4 10l6.5-6.5z"/></svg>
              <span class="select-menu-item-text css-truncate-target js-select-menu-filter-text">
                release-v1.4
              </span>
            </a>
            <a class="select-menu-item js-navigation-item js-navigation-open "
               href="/ckan/ckan/blob/release-v1.4.1/ckan/config/routing.py"
               data-name="release-v1.4.1"
               data-skip-pjax="true"
               rel="nofollow">
              <svg aria-hidden="true" class="octicon octicon-check select-menu-item-icon" height="16" version="1.1" viewBox="0 0 12 16" width="12"><path fill-rule="evenodd" d="M12 5l-8 8-4-4 1.5-1.5L4 10l6.5-6.5z"/></svg>
              <span class="select-menu-item-text css-truncate-target js-select-menu-filter-text">
                release-v1.4.1
              </span>
            </a>
            <a class="select-menu-item js-navigation-item js-navigation-open "
               href="/ckan/ckan/blob/release-v1.4.2/ckan/config/routing.py"
               data-name="release-v1.4.2"
               data-skip-pjax="true"
               rel="nofollow">
              <svg aria-hidden="true" class="octicon octicon-check select-menu-item-icon" height="16" version="1.1" viewBox="0 0 12 16" width="12"><path fill-rule="evenodd" d="M12 5l-8 8-4-4 1.5-1.5L4 10l6.5-6.5z"/></svg>
              <span class="select-menu-item-text css-truncate-target js-select-menu-filter-text">
                release-v1.4.2
              </span>
            </a>
            <a class="select-menu-item js-navigation-item js-navigation-open "
               href="/ckan/ckan/blob/release-v1.4.3/ckan/config/routing.py"
               data-name="release-v1.4.3"
               data-skip-pjax="true"
               rel="nofollow">
              <svg aria-hidden="true" class="octicon octicon-check select-menu-item-icon" height="16" version="1.1" viewBox="0 0 12 16" width="12"><path fill-rule="evenodd" d="M12 5l-8 8-4-4 1.5-1.5L4 10l6.5-6.5z"/></svg>
              <span class="select-menu-item-text css-truncate-target js-select-menu-filter-text">
                release-v1.4.3
              </span>
            </a>
            <a class="select-menu-item js-navigation-item js-navigation-open "
               href="/ckan/ckan/blob/release-v1.4.3.1/ckan/config/routing.py"
               data-name="release-v1.4.3.1"
               data-skip-pjax="true"
               rel="nofollow">
              <svg aria-hidden="true" class="octicon octicon-check select-menu-item-icon" height="16" version="1.1" viewBox="0 0 12 16" width="12"><path fill-rule="evenodd" d="M12 5l-8 8-4-4 1.5-1.5L4 10l6.5-6.5z"/></svg>
              <span class="select-menu-item-text css-truncate-target js-select-menu-filter-text">
                release-v1.4.3.1
              </span>
            </a>
            <a class="select-menu-item js-navigation-item js-navigation-open "
               href="/ckan/ckan/blob/release-v1.4.3.2/ckan/config/routing.py"
               data-name="release-v1.4.3.2"
               data-skip-pjax="true"
               rel="nofollow">
              <svg aria-hidden="true" class="octicon octicon-check select-menu-item-icon" height="16" version="1.1" viewBox="0 0 12 16" width="12"><path fill-rule="evenodd" d="M12 5l-8 8-4-4 1.5-1.5L4 10l6.5-6.5z"/></svg>
              <span class="select-menu-item-text css-truncate-target js-select-menu-filter-text">
                release-v1.4.3.2
              </span>
            </a>
            <a class="select-menu-item js-navigation-item js-navigation-open "
               href="/ckan/ckan/blob/release-v1.5/ckan/config/routing.py"
               data-name="release-v1.5"
               data-skip-pjax="true"
               rel="nofollow">
              <svg aria-hidden="true" class="octicon octicon-check select-menu-item-icon" height="16" version="1.1" viewBox="0 0 12 16" width="12"><path fill-rule="evenodd" d="M12 5l-8 8-4-4 1.5-1.5L4 10l6.5-6.5z"/></svg>
              <span class="select-menu-item-text css-truncate-target js-select-menu-filter-text">
                release-v1.5
              </span>
            </a>
            <a class="select-menu-item js-navigation-item js-navigation-open "
               href="/ckan/ckan/blob/release-v1.5.1c-fixes-iati/ckan/config/routing.py"
               data-name="release-v1.5.1c-fixes-iati"
               data-skip-pjax="true"
               rel="nofollow">
              <svg aria-hidden="true" class="octicon octicon-check select-menu-item-icon" height="16" version="1.1" viewBox="0 0 12 16" width="12"><path fill-rule="evenodd" d="M12 5l-8 8-4-4 1.5-1.5L4 10l6.5-6.5z"/></svg>
              <span class="select-menu-item-text css-truncate-target js-select-menu-filter-text">
                release-v1.5.1c-fixes-iati
              </span>
            </a>
            <a class="select-menu-item js-navigation-item js-navigation-open "
               href="/ckan/ckan/blob/release-v1.5.1c/ckan/config/routing.py"
               data-name="release-v1.5.1c"
               data-skip-pjax="true"
               rel="nofollow">
              <svg aria-hidden="true" class="octicon octicon-check select-menu-item-icon" height="16" version="1.1" viewBox="0 0 12 16" width="12"><path fill-rule="evenodd" d="M12 5l-8 8-4-4 1.5-1.5L4 10l6.5-6.5z"/></svg>
              <span class="select-menu-item-text css-truncate-target js-select-menu-filter-text">
                release-v1.5.1c
              </span>
            </a>
            <a class="select-menu-item js-navigation-item js-navigation-open "
               href="/ckan/ckan/blob/release-v1.5.1/ckan/config/routing.py"
               data-name="release-v1.5.1"
               data-skip-pjax="true"
               rel="nofollow">
              <svg aria-hidden="true" class="octicon octicon-check select-menu-item-icon" height="16" version="1.1" viewBox="0 0 12 16" width="12"><path fill-rule="evenodd" d="M12 5l-8 8-4-4 1.5-1.5L4 10l6.5-6.5z"/></svg>
              <span class="select-menu-item-text css-truncate-target js-select-menu-filter-text">
                release-v1.5.1
              </span>
            </a>
            <a class="select-menu-item js-navigation-item js-navigation-open "
               href="/ckan/ckan/blob/release-v1.6/ckan/config/routing.py"
               data-name="release-v1.6"
               data-skip-pjax="true"
               rel="nofollow">
              <svg aria-hidden="true" class="octicon octicon-check select-menu-item-icon" height="16" version="1.1" viewBox="0 0 12 16" width="12"><path fill-rule="evenodd" d="M12 5l-8 8-4-4 1.5-1.5L4 10l6.5-6.5z"/></svg>
              <span class="select-menu-item-text css-truncate-target js-select-menu-filter-text">
                release-v1.6
              </span>
            </a>
            <a class="select-menu-item js-navigation-item js-navigation-open "
               href="/ckan/ckan/blob/release-v1.6.1/ckan/config/routing.py"
               data-name="release-v1.6.1"
               data-skip-pjax="true"
               rel="nofollow">
              <svg aria-hidden="true" class="octicon octicon-check select-menu-item-icon" height="16" version="1.1" viewBox="0 0 12 16" width="12"><path fill-rule="evenodd" d="M12 5l-8 8-4-4 1.5-1.5L4 10l6.5-6.5z"/></svg>
              <span class="select-menu-item-text css-truncate-target js-select-menu-filter-text">
                release-v1.6.1
              </span>
            </a>
            <a class="select-menu-item js-navigation-item js-navigation-open "
               href="/ckan/ckan/blob/release-v1.7/ckan/config/routing.py"
               data-name="release-v1.7"
               data-skip-pjax="true"
               rel="nofollow">
              <svg aria-hidden="true" class="octicon octicon-check select-menu-item-icon" height="16" version="1.1" viewBox="0 0 12 16" width="12"><path fill-rule="evenodd" d="M12 5l-8 8-4-4 1.5-1.5L4 10l6.5-6.5z"/></svg>
              <span class="select-menu-item-text css-truncate-target js-select-menu-filter-text">
                release-v1.7
              </span>
            </a>
            <a class="select-menu-item js-navigation-item js-navigation-open "
               href="/ckan/ckan/blob/release-v1.7.1-ecportal/ckan/config/routing.py"
               data-name="release-v1.7.1-ecportal"
               data-skip-pjax="true"
               rel="nofollow">
              <svg aria-hidden="true" class="octicon octicon-check select-menu-item-icon" height="16" version="1.1" viewBox="0 0 12 16" width="12"><path fill-rule="evenodd" d="M12 5l-8 8-4-4 1.5-1.5L4 10l6.5-6.5z"/></svg>
              <span class="select-menu-item-text css-truncate-target js-select-menu-filter-text">
                release-v1.7.1-ecportal
              </span>
            </a>
            <a class="select-menu-item js-navigation-item js-navigation-open "
               href="/ckan/ckan/blob/release-v1.7.1/ckan/config/routing.py"
               data-name="release-v1.7.1"
               data-skip-pjax="true"
               rel="nofollow">
              <svg aria-hidden="true" class="octicon octicon-check select-menu-item-icon" height="16" version="1.1" viewBox="0 0 12 16" width="12"><path fill-rule="evenodd" d="M12 5l-8 8-4-4 1.5-1.5L4 10l6.5-6.5z"/></svg>
              <span class="select-menu-item-text css-truncate-target js-select-menu-filter-text">
                release-v1.7.1
              </span>
            </a>
            <a class="select-menu-item js-navigation-item js-navigation-open "
               href="/ckan/ckan/blob/release-v1.7.2/ckan/config/routing.py"
               data-name="release-v1.7.2"
               data-skip-pjax="true"
               rel="nofollow">
              <svg aria-hidden="true" class="octicon octicon-check select-menu-item-icon" height="16" version="1.1" viewBox="0 0 12 16" width="12"><path fill-rule="evenodd" d="M12 5l-8 8-4-4 1.5-1.5L4 10l6.5-6.5z"/></svg>
              <span class="select-menu-item-text css-truncate-target js-select-menu-filter-text">
                release-v1.7.2
              </span>
            </a>
            <a class="select-menu-item js-navigation-item js-navigation-open "
               href="/ckan/ckan/blob/release-v1.7.3/ckan/config/routing.py"
               data-name="release-v1.7.3"
               data-skip-pjax="true"
               rel="nofollow">
              <svg aria-hidden="true" class="octicon octicon-check select-menu-item-icon" height="16" version="1.1" viewBox="0 0 12 16" width="12"><path fill-rule="evenodd" d="M12 5l-8 8-4-4 1.5-1.5L4 10l6.5-6.5z"/></svg>
              <span class="select-menu-item-text css-truncate-target js-select-menu-filter-text">
                release-v1.7.3
              </span>
            </a>
            <a class="select-menu-item js-navigation-item js-navigation-open "
               href="/ckan/ckan/blob/release-v1.7.4/ckan/config/routing.py"
               data-name="release-v1.7.4"
               data-skip-pjax="true"
               rel="nofollow">
              <svg aria-hidden="true" class="octicon octicon-check select-menu-item-icon" height="16" version="1.1" viewBox="0 0 12 16" width="12"><path fill-rule="evenodd" d="M12 5l-8 8-4-4 1.5-1.5L4 10l6.5-6.5z"/></svg>
              <span class="select-menu-item-text css-truncate-target js-select-menu-filter-text">
                release-v1.7.4
              </span>
            </a>
            <a class="select-menu-item js-navigation-item js-navigation-open "
               href="/ckan/ckan/blob/release-v1.8-new-datastore/ckan/config/routing.py"
               data-name="release-v1.8-new-datastore"
               data-skip-pjax="true"
               rel="nofollow">
              <svg aria-hidden="true" class="octicon octicon-check select-menu-item-icon" height="16" version="1.1" viewBox="0 0 12 16" width="12"><path fill-rule="evenodd" d="M12 5l-8 8-4-4 1.5-1.5L4 10l6.5-6.5z"/></svg>
              <span class="select-menu-item-text css-truncate-target js-select-menu-filter-text">
                release-v1.8-new-datastore
              </span>
            </a>
            <a class="select-menu-item js-navigation-item js-navigation-open "
               href="/ckan/ckan/blob/release-v1.8/ckan/config/routing.py"
               data-name="release-v1.8"
               data-skip-pjax="true"
               rel="nofollow">
              <svg aria-hidden="true" class="octicon octicon-check select-menu-item-icon" height="16" version="1.1" viewBox="0 0 12 16" width="12"><path fill-rule="evenodd" d="M12 5l-8 8-4-4 1.5-1.5L4 10l6.5-6.5z"/></svg>
              <span class="select-menu-item-text css-truncate-target js-select-menu-filter-text">
                release-v1.8
              </span>
            </a>
            <a class="select-menu-item js-navigation-item js-navigation-open "
               href="/ckan/ckan/blob/release-v1.8.1-ecportal/ckan/config/routing.py"
               data-name="release-v1.8.1-ecportal"
               data-skip-pjax="true"
               rel="nofollow">
              <svg aria-hidden="true" class="octicon octicon-check select-menu-item-icon" height="16" version="1.1" viewBox="0 0 12 16" width="12"><path fill-rule="evenodd" d="M12 5l-8 8-4-4 1.5-1.5L4 10l6.5-6.5z"/></svg>
              <span class="select-menu-item-text css-truncate-target js-select-menu-filter-text">
                release-v1.8.1-ecportal
              </span>
            </a>
            <a class="select-menu-item js-navigation-item js-navigation-open "
               href="/ckan/ckan/blob/release-v1.8.1/ckan/config/routing.py"
               data-name="release-v1.8.1"
               data-skip-pjax="true"
               rel="nofollow">
              <svg aria-hidden="true" class="octicon octicon-check select-menu-item-icon" height="16" version="1.1" viewBox="0 0 12 16" width="12"><path fill-rule="evenodd" d="M12 5l-8 8-4-4 1.5-1.5L4 10l6.5-6.5z"/></svg>
              <span class="select-menu-item-text css-truncate-target js-select-menu-filter-text">
                release-v1.8.1
              </span>
            </a>
            <a class="select-menu-item js-navigation-item js-navigation-open "
               href="/ckan/ckan/blob/release-v1.8.2/ckan/config/routing.py"
               data-name="release-v1.8.2"
               data-skip-pjax="true"
               rel="nofollow">
              <svg aria-hidden="true" class="octicon octicon-check select-menu-item-icon" height="16" version="1.1" viewBox="0 0 12 16" width="12"><path fill-rule="evenodd" d="M12 5l-8 8-4-4 1.5-1.5L4 10l6.5-6.5z"/></svg>
              <span class="select-menu-item-text css-truncate-target js-select-menu-filter-text">
                release-v1.8.2
              </span>
            </a>
            <a class="select-menu-item js-navigation-item js-navigation-open "
               href="/ckan/ckan/blob/release-v2.0-latest/ckan/config/routing.py"
               data-name="release-v2.0-latest"
               data-skip-pjax="true"
               rel="nofollow">
              <svg aria-hidden="true" class="octicon octicon-check select-menu-item-icon" height="16" version="1.1" viewBox="0 0 12 16" width="12"><path fill-rule="evenodd" d="M12 5l-8 8-4-4 1.5-1.5L4 10l6.5-6.5z"/></svg>
              <span class="select-menu-item-text css-truncate-target js-select-menu-filter-text">
                release-v2.0-latest
              </span>
            </a>
            <a class="select-menu-item js-navigation-item js-navigation-open "
               href="/ckan/ckan/blob/release-v2.0/ckan/config/routing.py"
               data-name="release-v2.0"
               data-skip-pjax="true"
               rel="nofollow">
              <svg aria-hidden="true" class="octicon octicon-check select-menu-item-icon" height="16" version="1.1" viewBox="0 0 12 16" width="12"><path fill-rule="evenodd" d="M12 5l-8 8-4-4 1.5-1.5L4 10l6.5-6.5z"/></svg>
              <span class="select-menu-item-text css-truncate-target js-select-menu-filter-text">
                release-v2.0
              </span>
            </a>
            <a class="select-menu-item js-navigation-item js-navigation-open "
               href="/ckan/ckan/blob/release-v2.0.1/ckan/config/routing.py"
               data-name="release-v2.0.1"
               data-skip-pjax="true"
               rel="nofollow">
              <svg aria-hidden="true" class="octicon octicon-check select-menu-item-icon" height="16" version="1.1" viewBox="0 0 12 16" width="12"><path fill-rule="evenodd" d="M12 5l-8 8-4-4 1.5-1.5L4 10l6.5-6.5z"/></svg>
              <span class="select-menu-item-text css-truncate-target js-select-menu-filter-text">
                release-v2.0.1
              </span>
            </a>
            <a class="select-menu-item js-navigation-item js-navigation-open "
               href="/ckan/ckan/blob/release-v2.0.2/ckan/config/routing.py"
               data-name="release-v2.0.2"
               data-skip-pjax="true"
               rel="nofollow">
              <svg aria-hidden="true" class="octicon octicon-check select-menu-item-icon" height="16" version="1.1" viewBox="0 0 12 16" width="12"><path fill-rule="evenodd" d="M12 5l-8 8-4-4 1.5-1.5L4 10l6.5-6.5z"/></svg>
              <span class="select-menu-item-text css-truncate-target js-select-menu-filter-text">
                release-v2.0.2
              </span>
            </a>
            <a class="select-menu-item js-navigation-item js-navigation-open "
               href="/ckan/ckan/blob/release-v2.0.3/ckan/config/routing.py"
               data-name="release-v2.0.3"
               data-skip-pjax="true"
               rel="nofollow">
              <svg aria-hidden="true" class="octicon octicon-check select-menu-item-icon" height="16" version="1.1" viewBox="0 0 12 16" width="12"><path fill-rule="evenodd" d="M12 5l-8 8-4-4 1.5-1.5L4 10l6.5-6.5z"/></svg>
              <span class="select-menu-item-text css-truncate-target js-select-menu-filter-text">
                release-v2.0.3
              </span>
            </a>
            <a class="select-menu-item js-navigation-item js-navigation-open "
               href="/ckan/ckan/blob/release-v2.0.4/ckan/config/routing.py"
               data-name="release-v2.0.4"
               data-skip-pjax="true"
               rel="nofollow">
              <svg aria-hidden="true" class="octicon octicon-check select-menu-item-icon" height="16" version="1.1" viewBox="0 0 12 16" width="12"><path fill-rule="evenodd" d="M12 5l-8 8-4-4 1.5-1.5L4 10l6.5-6.5z"/></svg>
              <span class="select-menu-item-text css-truncate-target js-select-menu-filter-text">
                release-v2.0.4
              </span>
            </a>
            <a class="select-menu-item js-navigation-item js-navigation-open "
               href="/ckan/ckan/blob/release-v2.0.5/ckan/config/routing.py"
               data-name="release-v2.0.5"
               data-skip-pjax="true"
               rel="nofollow">
              <svg aria-hidden="true" class="octicon octicon-check select-menu-item-icon" height="16" version="1.1" viewBox="0 0 12 16" width="12"><path fill-rule="evenodd" d="M12 5l-8 8-4-4 1.5-1.5L4 10l6.5-6.5z"/></svg>
              <span class="select-menu-item-text css-truncate-target js-select-menu-filter-text">
                release-v2.0.5
              </span>
            </a>
            <a class="select-menu-item js-navigation-item js-navigation-open "
               href="/ckan/ckan/blob/release-v2.0.6/ckan/config/routing.py"
               data-name="release-v2.0.6"
               data-skip-pjax="true"
               rel="nofollow">
              <svg aria-hidden="true" class="octicon octicon-check select-menu-item-icon" height="16" version="1.1" viewBox="0 0 12 16" width="12"><path fill-rule="evenodd" d="M12 5l-8 8-4-4 1.5-1.5L4 10l6.5-6.5z"/></svg>
              <span class="select-menu-item-text css-truncate-target js-select-menu-filter-text">
                release-v2.0.6
              </span>
            </a>
            <a class="select-menu-item js-navigation-item js-navigation-open "
               href="/ckan/ckan/blob/release-v2.0.7/ckan/config/routing.py"
               data-name="release-v2.0.7"
               data-skip-pjax="true"
               rel="nofollow">
              <svg aria-hidden="true" class="octicon octicon-check select-menu-item-icon" height="16" version="1.1" viewBox="0 0 12 16" width="12"><path fill-rule="evenodd" d="M12 5l-8 8-4-4 1.5-1.5L4 10l6.5-6.5z"/></svg>
              <span class="select-menu-item-text css-truncate-target js-select-menu-filter-text">
                release-v2.0.7
              </span>
            </a>
            <a class="select-menu-item js-navigation-item js-navigation-open "
               href="/ckan/ckan/blob/release-v2.0.8/ckan/config/routing.py"
               data-name="release-v2.0.8"
               data-skip-pjax="true"
               rel="nofollow">
              <svg aria-hidden="true" class="octicon octicon-check select-menu-item-icon" height="16" version="1.1" viewBox="0 0 12 16" width="12"><path fill-rule="evenodd" d="M12 5l-8 8-4-4 1.5-1.5L4 10l6.5-6.5z"/></svg>
              <span class="select-menu-item-text css-truncate-target js-select-menu-filter-text">
                release-v2.0.8
              </span>
            </a>
            <a class="select-menu-item js-navigation-item js-navigation-open "
               href="/ckan/ckan/blob/release-v2.0.9/ckan/config/routing.py"
               data-name="release-v2.0.9"
               data-skip-pjax="true"
               rel="nofollow">
              <svg aria-hidden="true" class="octicon octicon-check select-menu-item-icon" height="16" version="1.1" viewBox="0 0 12 16" width="12"><path fill-rule="evenodd" d="M12 5l-8 8-4-4 1.5-1.5L4 10l6.5-6.5z"/></svg>
              <span class="select-menu-item-text css-truncate-target js-select-menu-filter-text">
                release-v2.0.9
              </span>
            </a>
            <a class="select-menu-item js-navigation-item js-navigation-open "
               href="/ckan/ckan/blob/release-v2.1-latest/ckan/config/routing.py"
               data-name="release-v2.1-latest"
               data-skip-pjax="true"
               rel="nofollow">
              <svg aria-hidden="true" class="octicon octicon-check select-menu-item-icon" height="16" version="1.1" viewBox="0 0 12 16" width="12"><path fill-rule="evenodd" d="M12 5l-8 8-4-4 1.5-1.5L4 10l6.5-6.5z"/></svg>
              <span class="select-menu-item-text css-truncate-target js-select-menu-filter-text">
                release-v2.1-latest
              </span>
            </a>
            <a class="select-menu-item js-navigation-item js-navigation-open "
               href="/ckan/ckan/blob/release-v2.1/ckan/config/routing.py"
               data-name="release-v2.1"
               data-skip-pjax="true"
               rel="nofollow">
              <svg aria-hidden="true" class="octicon octicon-check select-menu-item-icon" height="16" version="1.1" viewBox="0 0 12 16" width="12"><path fill-rule="evenodd" d="M12 5l-8 8-4-4 1.5-1.5L4 10l6.5-6.5z"/></svg>
              <span class="select-menu-item-text css-truncate-target js-select-menu-filter-text">
                release-v2.1
              </span>
            </a>
            <a class="select-menu-item js-navigation-item js-navigation-open "
               href="/ckan/ckan/blob/release-v2.1.1/ckan/config/routing.py"
               data-name="release-v2.1.1"
               data-skip-pjax="true"
               rel="nofollow">
              <svg aria-hidden="true" class="octicon octicon-check select-menu-item-icon" height="16" version="1.1" viewBox="0 0 12 16" width="12"><path fill-rule="evenodd" d="M12 5l-8 8-4-4 1.5-1.5L4 10l6.5-6.5z"/></svg>
              <span class="select-menu-item-text css-truncate-target js-select-menu-filter-text">
                release-v2.1.1
              </span>
            </a>
            <a class="select-menu-item js-navigation-item js-navigation-open "
               href="/ckan/ckan/blob/release-v2.1.2/ckan/config/routing.py"
               data-name="release-v2.1.2"
               data-skip-pjax="true"
               rel="nofollow">
              <svg aria-hidden="true" class="octicon octicon-check select-menu-item-icon" height="16" version="1.1" viewBox="0 0 12 16" width="12"><path fill-rule="evenodd" d="M12 5l-8 8-4-4 1.5-1.5L4 10l6.5-6.5z"/></svg>
              <span class="select-menu-item-text css-truncate-target js-select-menu-filter-text">
                release-v2.1.2
              </span>
            </a>
            <a class="select-menu-item js-navigation-item js-navigation-open "
               href="/ckan/ckan/blob/release-v2.1.3/ckan/config/routing.py"
               data-name="release-v2.1.3"
               data-skip-pjax="true"
               rel="nofollow">
              <svg aria-hidden="true" class="octicon octicon-check select-menu-item-icon" height="16" version="1.1" viewBox="0 0 12 16" width="12"><path fill-rule="evenodd" d="M12 5l-8 8-4-4 1.5-1.5L4 10l6.5-6.5z"/></svg>
              <span class="select-menu-item-text css-truncate-target js-select-menu-filter-text">
                release-v2.1.3
              </span>
            </a>
            <a class="select-menu-item js-navigation-item js-navigation-open "
               href="/ckan/ckan/blob/release-v2.1.4/ckan/config/routing.py"
               data-name="release-v2.1.4"
               data-skip-pjax="true"
               rel="nofollow">
              <svg aria-hidden="true" class="octicon octicon-check select-menu-item-icon" height="16" version="1.1" viewBox="0 0 12 16" width="12"><path fill-rule="evenodd" d="M12 5l-8 8-4-4 1.5-1.5L4 10l6.5-6.5z"/></svg>
              <span class="select-menu-item-text css-truncate-target js-select-menu-filter-text">
                release-v2.1.4
              </span>
            </a>
            <a class="select-menu-item js-navigation-item js-navigation-open "
               href="/ckan/ckan/blob/release-v2.1.5/ckan/config/routing.py"
               data-name="release-v2.1.5"
               data-skip-pjax="true"
               rel="nofollow">
              <svg aria-hidden="true" class="octicon octicon-check select-menu-item-icon" height="16" version="1.1" viewBox="0 0 12 16" width="12"><path fill-rule="evenodd" d="M12 5l-8 8-4-4 1.5-1.5L4 10l6.5-6.5z"/></svg>
              <span class="select-menu-item-text css-truncate-target js-select-menu-filter-text">
                release-v2.1.5
              </span>
            </a>
            <a class="select-menu-item js-navigation-item js-navigation-open "
               href="/ckan/ckan/blob/release-v2.1.6/ckan/config/routing.py"
               data-name="release-v2.1.6"
               data-skip-pjax="true"
               rel="nofollow">
              <svg aria-hidden="true" class="octicon octicon-check select-menu-item-icon" height="16" version="1.1" viewBox="0 0 12 16" width="12"><path fill-rule="evenodd" d="M12 5l-8 8-4-4 1.5-1.5L4 10l6.5-6.5z"/></svg>
              <span class="select-menu-item-text css-truncate-target js-select-menu-filter-text">
                release-v2.1.6
              </span>
            </a>
            <a class="select-menu-item js-navigation-item js-navigation-open "
               href="/ckan/ckan/blob/release-v2.1.7/ckan/config/routing.py"
               data-name="release-v2.1.7"
               data-skip-pjax="true"
               rel="nofollow">
              <svg aria-hidden="true" class="octicon octicon-check select-menu-item-icon" height="16" version="1.1" viewBox="0 0 12 16" width="12"><path fill-rule="evenodd" d="M12 5l-8 8-4-4 1.5-1.5L4 10l6.5-6.5z"/></svg>
              <span class="select-menu-item-text css-truncate-target js-select-menu-filter-text">
                release-v2.1.7
              </span>
            </a>
            <a class="select-menu-item js-navigation-item js-navigation-open "
               href="/ckan/ckan/blob/release-v2.2-latest/ckan/config/routing.py"
               data-name="release-v2.2-latest"
               data-skip-pjax="true"
               rel="nofollow">
              <svg aria-hidden="true" class="octicon octicon-check select-menu-item-icon" height="16" version="1.1" viewBox="0 0 12 16" width="12"><path fill-rule="evenodd" d="M12 5l-8 8-4-4 1.5-1.5L4 10l6.5-6.5z"/></svg>
              <span class="select-menu-item-text css-truncate-target js-select-menu-filter-text">
                release-v2.2-latest
              </span>
            </a>
            <a class="select-menu-item js-navigation-item js-navigation-open "
               href="/ckan/ckan/blob/release-v2.2/ckan/config/routing.py"
               data-name="release-v2.2"
               data-skip-pjax="true"
               rel="nofollow">
              <svg aria-hidden="true" class="octicon octicon-check select-menu-item-icon" height="16" version="1.1" viewBox="0 0 12 16" width="12"><path fill-rule="evenodd" d="M12 5l-8 8-4-4 1.5-1.5L4 10l6.5-6.5z"/></svg>
              <span class="select-menu-item-text css-truncate-target js-select-menu-filter-text">
                release-v2.2
              </span>
            </a>
            <a class="select-menu-item js-navigation-item js-navigation-open "
               href="/ckan/ckan/blob/release-v2.2.1-ckanext-sgdata/ckan/config/routing.py"
               data-name="release-v2.2.1-ckanext-sgdata"
               data-skip-pjax="true"
               rel="nofollow">
              <svg aria-hidden="true" class="octicon octicon-check select-menu-item-icon" height="16" version="1.1" viewBox="0 0 12 16" width="12"><path fill-rule="evenodd" d="M12 5l-8 8-4-4 1.5-1.5L4 10l6.5-6.5z"/></svg>
              <span class="select-menu-item-text css-truncate-target js-select-menu-filter-text">
                release-v2.2.1-ckanext-sgdata
              </span>
            </a>
            <a class="select-menu-item js-navigation-item js-navigation-open "
               href="/ckan/ckan/blob/release-v2.2.1/ckan/config/routing.py"
               data-name="release-v2.2.1"
               data-skip-pjax="true"
               rel="nofollow">
              <svg aria-hidden="true" class="octicon octicon-check select-menu-item-icon" height="16" version="1.1" viewBox="0 0 12 16" width="12"><path fill-rule="evenodd" d="M12 5l-8 8-4-4 1.5-1.5L4 10l6.5-6.5z"/></svg>
              <span class="select-menu-item-text css-truncate-target js-select-menu-filter-text">
                release-v2.2.1
              </span>
            </a>
            <a class="select-menu-item js-navigation-item js-navigation-open "
               href="/ckan/ckan/blob/release-v2.2.2-fix-travis/ckan/config/routing.py"
               data-name="release-v2.2.2-fix-travis"
               data-skip-pjax="true"
               rel="nofollow">
              <svg aria-hidden="true" class="octicon octicon-check select-menu-item-icon" height="16" version="1.1" viewBox="0 0 12 16" width="12"><path fill-rule="evenodd" d="M12 5l-8 8-4-4 1.5-1.5L4 10l6.5-6.5z"/></svg>
              <span class="select-menu-item-text css-truncate-target js-select-menu-filter-text">
                release-v2.2.2-fix-travis
              </span>
            </a>
            <a class="select-menu-item js-navigation-item js-navigation-open "
               href="/ckan/ckan/blob/release-v2.2.2/ckan/config/routing.py"
               data-name="release-v2.2.2"
               data-skip-pjax="true"
               rel="nofollow">
              <svg aria-hidden="true" class="octicon octicon-check select-menu-item-icon" height="16" version="1.1" viewBox="0 0 12 16" width="12"><path fill-rule="evenodd" d="M12 5l-8 8-4-4 1.5-1.5L4 10l6.5-6.5z"/></svg>
              <span class="select-menu-item-text css-truncate-target js-select-menu-filter-text">
                release-v2.2.2
              </span>
            </a>
            <a class="select-menu-item js-navigation-item js-navigation-open "
               href="/ckan/ckan/blob/release-v2.2.3/ckan/config/routing.py"
               data-name="release-v2.2.3"
               data-skip-pjax="true"
               rel="nofollow">
              <svg aria-hidden="true" class="octicon octicon-check select-menu-item-icon" height="16" version="1.1" viewBox="0 0 12 16" width="12"><path fill-rule="evenodd" d="M12 5l-8 8-4-4 1.5-1.5L4 10l6.5-6.5z"/></svg>
              <span class="select-menu-item-text css-truncate-target js-select-menu-filter-text">
                release-v2.2.3
              </span>
            </a>
            <a class="select-menu-item js-navigation-item js-navigation-open "
               href="/ckan/ckan/blob/release-v2.2.4/ckan/config/routing.py"
               data-name="release-v2.2.4"
               data-skip-pjax="true"
               rel="nofollow">
              <svg aria-hidden="true" class="octicon octicon-check select-menu-item-icon" height="16" version="1.1" viewBox="0 0 12 16" width="12"><path fill-rule="evenodd" d="M12 5l-8 8-4-4 1.5-1.5L4 10l6.5-6.5z"/></svg>
              <span class="select-menu-item-text css-truncate-target js-select-menu-filter-text">
                release-v2.2.4
              </span>
            </a>
            <a class="select-menu-item js-navigation-item js-navigation-open "
               href="/ckan/ckan/blob/release-v2.2.5/ckan/config/routing.py"
               data-name="release-v2.2.5"
               data-skip-pjax="true"
               rel="nofollow">
              <svg aria-hidden="true" class="octicon octicon-check select-menu-item-icon" height="16" version="1.1" viewBox="0 0 12 16" width="12"><path fill-rule="evenodd" d="M12 5l-8 8-4-4 1.5-1.5L4 10l6.5-6.5z"/></svg>
              <span class="select-menu-item-text css-truncate-target js-select-menu-filter-text">
                release-v2.2.5
              </span>
            </a>
            <a class="select-menu-item js-navigation-item js-navigation-open "
               href="/ckan/ckan/blob/release-v2.3-latest/ckan/config/routing.py"
               data-name="release-v2.3-latest"
               data-skip-pjax="true"
               rel="nofollow">
              <svg aria-hidden="true" class="octicon octicon-check select-menu-item-icon" height="16" version="1.1" viewBox="0 0 12 16" width="12"><path fill-rule="evenodd" d="M12 5l-8 8-4-4 1.5-1.5L4 10l6.5-6.5z"/></svg>
              <span class="select-menu-item-text css-truncate-target js-select-menu-filter-text">
                release-v2.3-latest
              </span>
            </a>
            <a class="select-menu-item js-navigation-item js-navigation-open "
               href="/ckan/ckan/blob/release-v2.3/ckan/config/routing.py"
               data-name="release-v2.3"
               data-skip-pjax="true"
               rel="nofollow">
              <svg aria-hidden="true" class="octicon octicon-check select-menu-item-icon" height="16" version="1.1" viewBox="0 0 12 16" width="12"><path fill-rule="evenodd" d="M12 5l-8 8-4-4 1.5-1.5L4 10l6.5-6.5z"/></svg>
              <span class="select-menu-item-text css-truncate-target js-select-menu-filter-text">
                release-v2.3
              </span>
            </a>
            <a class="select-menu-item js-navigation-item js-navigation-open "
               href="/ckan/ckan/blob/release-v2.3.1/ckan/config/routing.py"
               data-name="release-v2.3.1"
               data-skip-pjax="true"
               rel="nofollow">
              <svg aria-hidden="true" class="octicon octicon-check select-menu-item-icon" height="16" version="1.1" viewBox="0 0 12 16" width="12"><path fill-rule="evenodd" d="M12 5l-8 8-4-4 1.5-1.5L4 10l6.5-6.5z"/></svg>
              <span class="select-menu-item-text css-truncate-target js-select-menu-filter-text">
                release-v2.3.1
              </span>
            </a>
            <a class="select-menu-item js-navigation-item js-navigation-open "
               href="/ckan/ckan/blob/release-v2.3.2/ckan/config/routing.py"
               data-name="release-v2.3.2"
               data-skip-pjax="true"
               rel="nofollow">
              <svg aria-hidden="true" class="octicon octicon-check select-menu-item-icon" height="16" version="1.1" viewBox="0 0 12 16" width="12"><path fill-rule="evenodd" d="M12 5l-8 8-4-4 1.5-1.5L4 10l6.5-6.5z"/></svg>
              <span class="select-menu-item-text css-truncate-target js-select-menu-filter-text">
                release-v2.3.2
              </span>
            </a>
            <a class="select-menu-item js-navigation-item js-navigation-open "
               href="/ckan/ckan/blob/release-v2.3.3/ckan/config/routing.py"
               data-name="release-v2.3.3"
               data-skip-pjax="true"
               rel="nofollow">
              <svg aria-hidden="true" class="octicon octicon-check select-menu-item-icon" height="16" version="1.1" viewBox="0 0 12 16" width="12"><path fill-rule="evenodd" d="M12 5l-8 8-4-4 1.5-1.5L4 10l6.5-6.5z"/></svg>
              <span class="select-menu-item-text css-truncate-target js-select-menu-filter-text">
                release-v2.3.3
              </span>
            </a>
            <a class="select-menu-item js-navigation-item js-navigation-open "
               href="/ckan/ckan/blob/release-v2.3.4/ckan/config/routing.py"
               data-name="release-v2.3.4"
               data-skip-pjax="true"
               rel="nofollow">
              <svg aria-hidden="true" class="octicon octicon-check select-menu-item-icon" height="16" version="1.1" viewBox="0 0 12 16" width="12"><path fill-rule="evenodd" d="M12 5l-8 8-4-4 1.5-1.5L4 10l6.5-6.5z"/></svg>
              <span class="select-menu-item-text css-truncate-target js-select-menu-filter-text">
                release-v2.3.4
              </span>
            </a>
            <a class="select-menu-item js-navigation-item js-navigation-open "
               href="/ckan/ckan/blob/release-v2.3.5/ckan/config/routing.py"
               data-name="release-v2.3.5"
               data-skip-pjax="true"
               rel="nofollow">
              <svg aria-hidden="true" class="octicon octicon-check select-menu-item-icon" height="16" version="1.1" viewBox="0 0 12 16" width="12"><path fill-rule="evenodd" d="M12 5l-8 8-4-4 1.5-1.5L4 10l6.5-6.5z"/></svg>
              <span class="select-menu-item-text css-truncate-target js-select-menu-filter-text">
                release-v2.3.5
              </span>
            </a>
            <a class="select-menu-item js-navigation-item js-navigation-open "
               href="/ckan/ckan/blob/release-v2.4-latest/ckan/config/routing.py"
               data-name="release-v2.4-latest"
               data-skip-pjax="true"
               rel="nofollow">
              <svg aria-hidden="true" class="octicon octicon-check select-menu-item-icon" height="16" version="1.1" viewBox="0 0 12 16" width="12"><path fill-rule="evenodd" d="M12 5l-8 8-4-4 1.5-1.5L4 10l6.5-6.5z"/></svg>
              <span class="select-menu-item-text css-truncate-target js-select-menu-filter-text">
                release-v2.4-latest
              </span>
            </a>
            <a class="select-menu-item js-navigation-item js-navigation-open "
               href="/ckan/ckan/blob/release-v2.4.0/ckan/config/routing.py"
               data-name="release-v2.4.0"
               data-skip-pjax="true"
               rel="nofollow">
              <svg aria-hidden="true" class="octicon octicon-check select-menu-item-icon" height="16" version="1.1" viewBox="0 0 12 16" width="12"><path fill-rule="evenodd" d="M12 5l-8 8-4-4 1.5-1.5L4 10l6.5-6.5z"/></svg>
              <span class="select-menu-item-text css-truncate-target js-select-menu-filter-text">
                release-v2.4.0
              </span>
            </a>
            <a class="select-menu-item js-navigation-item js-navigation-open "
               href="/ckan/ckan/blob/release-v2.4.1/ckan/config/routing.py"
               data-name="release-v2.4.1"
               data-skip-pjax="true"
               rel="nofollow">
              <svg aria-hidden="true" class="octicon octicon-check select-menu-item-icon" height="16" version="1.1" viewBox="0 0 12 16" width="12"><path fill-rule="evenodd" d="M12 5l-8 8-4-4 1.5-1.5L4 10l6.5-6.5z"/></svg>
              <span class="select-menu-item-text css-truncate-target js-select-menu-filter-text">
                release-v2.4.1
              </span>
            </a>
            <a class="select-menu-item js-navigation-item js-navigation-open "
               href="/ckan/ckan/blob/release-v2.4.2/ckan/config/routing.py"
               data-name="release-v2.4.2"
               data-skip-pjax="true"
               rel="nofollow">
              <svg aria-hidden="true" class="octicon octicon-check select-menu-item-icon" height="16" version="1.1" viewBox="0 0 12 16" width="12"><path fill-rule="evenodd" d="M12 5l-8 8-4-4 1.5-1.5L4 10l6.5-6.5z"/></svg>
              <span class="select-menu-item-text css-truncate-target js-select-menu-filter-text">
                release-v2.4.2
              </span>
            </a>
            <a class="select-menu-item js-navigation-item js-navigation-open "
               href="/ckan/ckan/blob/release-v2.4.3/ckan/config/routing.py"
               data-name="release-v2.4.3"
               data-skip-pjax="true"
               rel="nofollow">
              <svg aria-hidden="true" class="octicon octicon-check select-menu-item-icon" height="16" version="1.1" viewBox="0 0 12 16" width="12"><path fill-rule="evenodd" d="M12 5l-8 8-4-4 1.5-1.5L4 10l6.5-6.5z"/></svg>
              <span class="select-menu-item-text css-truncate-target js-select-menu-filter-text">
                release-v2.4.3
              </span>
            </a>
            <a class="select-menu-item js-navigation-item js-navigation-open "
               href="/ckan/ckan/blob/release-v2.4.4/ckan/config/routing.py"
               data-name="release-v2.4.4"
               data-skip-pjax="true"
               rel="nofollow">
              <svg aria-hidden="true" class="octicon octicon-check select-menu-item-icon" height="16" version="1.1" viewBox="0 0 12 16" width="12"><path fill-rule="evenodd" d="M12 5l-8 8-4-4 1.5-1.5L4 10l6.5-6.5z"/></svg>
              <span class="select-menu-item-text css-truncate-target js-select-menu-filter-text">
                release-v2.4.4
              </span>
            </a>
            <a class="select-menu-item js-navigation-item js-navigation-open "
               href="/ckan/ckan/blob/release-v2.4.5/ckan/config/routing.py"
               data-name="release-v2.4.5"
               data-skip-pjax="true"
               rel="nofollow">
              <svg aria-hidden="true" class="octicon octicon-check select-menu-item-icon" height="16" version="1.1" viewBox="0 0 12 16" width="12"><path fill-rule="evenodd" d="M12 5l-8 8-4-4 1.5-1.5L4 10l6.5-6.5z"/></svg>
              <span class="select-menu-item-text css-truncate-target js-select-menu-filter-text">
                release-v2.4.5
              </span>
            </a>
            <a class="select-menu-item js-navigation-item js-navigation-open "
               href="/ckan/ckan/blob/release-v2.4.6/ckan/config/routing.py"
               data-name="release-v2.4.6"
               data-skip-pjax="true"
               rel="nofollow">
              <svg aria-hidden="true" class="octicon octicon-check select-menu-item-icon" height="16" version="1.1" viewBox="0 0 12 16" width="12"><path fill-rule="evenodd" d="M12 5l-8 8-4-4 1.5-1.5L4 10l6.5-6.5z"/></svg>
              <span class="select-menu-item-text css-truncate-target js-select-menu-filter-text">
                release-v2.4.6
              </span>
            </a>
            <a class="select-menu-item js-navigation-item js-navigation-open "
               href="/ckan/ckan/blob/release-v2.4.7/ckan/config/routing.py"
               data-name="release-v2.4.7"
               data-skip-pjax="true"
               rel="nofollow">
              <svg aria-hidden="true" class="octicon octicon-check select-menu-item-icon" height="16" version="1.1" viewBox="0 0 12 16" width="12"><path fill-rule="evenodd" d="M12 5l-8 8-4-4 1.5-1.5L4 10l6.5-6.5z"/></svg>
              <span class="select-menu-item-text css-truncate-target js-select-menu-filter-text">
                release-v2.4.7
              </span>
            </a>
            <a class="select-menu-item js-navigation-item js-navigation-open "
               href="/ckan/ckan/blob/release-v2.4.8/ckan/config/routing.py"
               data-name="release-v2.4.8"
               data-skip-pjax="true"
               rel="nofollow">
              <svg aria-hidden="true" class="octicon octicon-check select-menu-item-icon" height="16" version="1.1" viewBox="0 0 12 16" width="12"><path fill-rule="evenodd" d="M12 5l-8 8-4-4 1.5-1.5L4 10l6.5-6.5z"/></svg>
              <span class="select-menu-item-text css-truncate-target js-select-menu-filter-text">
                release-v2.4.8
              </span>
            </a>
            <a class="select-menu-item js-navigation-item js-navigation-open "
               href="/ckan/ckan/blob/release-v2.4.9/ckan/config/routing.py"
               data-name="release-v2.4.9"
               data-skip-pjax="true"
               rel="nofollow">
              <svg aria-hidden="true" class="octicon octicon-check select-menu-item-icon" height="16" version="1.1" viewBox="0 0 12 16" width="12"><path fill-rule="evenodd" d="M12 5l-8 8-4-4 1.5-1.5L4 10l6.5-6.5z"/></svg>
              <span class="select-menu-item-text css-truncate-target js-select-menu-filter-text">
                release-v2.4.9
              </span>
            </a>
            <a class="select-menu-item js-navigation-item js-navigation-open "
               href="/ckan/ckan/blob/release-v2.5-latest/ckan/config/routing.py"
               data-name="release-v2.5-latest"
               data-skip-pjax="true"
               rel="nofollow">
              <svg aria-hidden="true" class="octicon octicon-check select-menu-item-icon" height="16" version="1.1" viewBox="0 0 12 16" width="12"><path fill-rule="evenodd" d="M12 5l-8 8-4-4 1.5-1.5L4 10l6.5-6.5z"/></svg>
              <span class="select-menu-item-text css-truncate-target js-select-menu-filter-text">
                release-v2.5-latest
              </span>
            </a>
            <a class="select-menu-item js-navigation-item js-navigation-open "
               href="/ckan/ckan/blob/release-v2.5.0/ckan/config/routing.py"
               data-name="release-v2.5.0"
               data-skip-pjax="true"
               rel="nofollow">
              <svg aria-hidden="true" class="octicon octicon-check select-menu-item-icon" height="16" version="1.1" viewBox="0 0 12 16" width="12"><path fill-rule="evenodd" d="M12 5l-8 8-4-4 1.5-1.5L4 10l6.5-6.5z"/></svg>
              <span class="select-menu-item-text css-truncate-target js-select-menu-filter-text">
                release-v2.5.0
              </span>
            </a>
            <a class="select-menu-item js-navigation-item js-navigation-open "
               href="/ckan/ckan/blob/release-v2.5.1/ckan/config/routing.py"
               data-name="release-v2.5.1"
               data-skip-pjax="true"
               rel="nofollow">
              <svg aria-hidden="true" class="octicon octicon-check select-menu-item-icon" height="16" version="1.1" viewBox="0 0 12 16" width="12"><path fill-rule="evenodd" d="M12 5l-8 8-4-4 1.5-1.5L4 10l6.5-6.5z"/></svg>
              <span class="select-menu-item-text css-truncate-target js-select-menu-filter-text">
                release-v2.5.1
              </span>
            </a>
            <a class="select-menu-item js-navigation-item js-navigation-open "
               href="/ckan/ckan/blob/release-v2.5.2/ckan/config/routing.py"
               data-name="release-v2.5.2"
               data-skip-pjax="true"
               rel="nofollow">
              <svg aria-hidden="true" class="octicon octicon-check select-menu-item-icon" height="16" version="1.1" viewBox="0 0 12 16" width="12"><path fill-rule="evenodd" d="M12 5l-8 8-4-4 1.5-1.5L4 10l6.5-6.5z"/></svg>
              <span class="select-menu-item-text css-truncate-target js-select-menu-filter-text">
                release-v2.5.2
              </span>
            </a>
            <a class="select-menu-item js-navigation-item js-navigation-open "
               href="/ckan/ckan/blob/release-v2.5.3/ckan/config/routing.py"
               data-name="release-v2.5.3"
               data-skip-pjax="true"
               rel="nofollow">
              <svg aria-hidden="true" class="octicon octicon-check select-menu-item-icon" height="16" version="1.1" viewBox="0 0 12 16" width="12"><path fill-rule="evenodd" d="M12 5l-8 8-4-4 1.5-1.5L4 10l6.5-6.5z"/></svg>
              <span class="select-menu-item-text css-truncate-target js-select-menu-filter-text">
                release-v2.5.3
              </span>
            </a>
            <a class="select-menu-item js-navigation-item js-navigation-open "
               href="/ckan/ckan/blob/release-v2.5.4/ckan/config/routing.py"
               data-name="release-v2.5.4"
               data-skip-pjax="true"
               rel="nofollow">
              <svg aria-hidden="true" class="octicon octicon-check select-menu-item-icon" height="16" version="1.1" viewBox="0 0 12 16" width="12"><path fill-rule="evenodd" d="M12 5l-8 8-4-4 1.5-1.5L4 10l6.5-6.5z"/></svg>
              <span class="select-menu-item-text css-truncate-target js-select-menu-filter-text">
                release-v2.5.4
              </span>
            </a>
            <a class="select-menu-item js-navigation-item js-navigation-open "
               href="/ckan/ckan/blob/release-v2.5.5/ckan/config/routing.py"
               data-name="release-v2.5.5"
               data-skip-pjax="true"
               rel="nofollow">
              <svg aria-hidden="true" class="octicon octicon-check select-menu-item-icon" height="16" version="1.1" viewBox="0 0 12 16" width="12"><path fill-rule="evenodd" d="M12 5l-8 8-4-4 1.5-1.5L4 10l6.5-6.5z"/></svg>
              <span class="select-menu-item-text css-truncate-target js-select-menu-filter-text">
                release-v2.5.5
              </span>
            </a>
            <a class="select-menu-item js-navigation-item js-navigation-open "
               href="/ckan/ckan/blob/release-v2.5.6/ckan/config/routing.py"
               data-name="release-v2.5.6"
               data-skip-pjax="true"
               rel="nofollow">
              <svg aria-hidden="true" class="octicon octicon-check select-menu-item-icon" height="16" version="1.1" viewBox="0 0 12 16" width="12"><path fill-rule="evenodd" d="M12 5l-8 8-4-4 1.5-1.5L4 10l6.5-6.5z"/></svg>
              <span class="select-menu-item-text css-truncate-target js-select-menu-filter-text">
                release-v2.5.6
              </span>
            </a>
            <a class="select-menu-item js-navigation-item js-navigation-open "
               href="/ckan/ckan/blob/release-v2.5.7/ckan/config/routing.py"
               data-name="release-v2.5.7"
               data-skip-pjax="true"
               rel="nofollow">
              <svg aria-hidden="true" class="octicon octicon-check select-menu-item-icon" height="16" version="1.1" viewBox="0 0 12 16" width="12"><path fill-rule="evenodd" d="M12 5l-8 8-4-4 1.5-1.5L4 10l6.5-6.5z"/></svg>
              <span class="select-menu-item-text css-truncate-target js-select-menu-filter-text">
                release-v2.5.7
              </span>
            </a>
            <a class="select-menu-item js-navigation-item js-navigation-open "
               href="/ckan/ckan/blob/release-v2.6-latest/ckan/config/routing.py"
               data-name="release-v2.6-latest"
               data-skip-pjax="true"
               rel="nofollow">
              <svg aria-hidden="true" class="octicon octicon-check select-menu-item-icon" height="16" version="1.1" viewBox="0 0 12 16" width="12"><path fill-rule="evenodd" d="M12 5l-8 8-4-4 1.5-1.5L4 10l6.5-6.5z"/></svg>
              <span class="select-menu-item-text css-truncate-target js-select-menu-filter-text">
                release-v2.6-latest
              </span>
            </a>
            <a class="select-menu-item js-navigation-item js-navigation-open "
               href="/ckan/ckan/blob/remove-authz/ckan/config/routing.py"
               data-name="remove-authz"
               data-skip-pjax="true"
               rel="nofollow">
              <svg aria-hidden="true" class="octicon octicon-check select-menu-item-icon" height="16" version="1.1" viewBox="0 0 12 16" width="12"><path fill-rule="evenodd" d="M12 5l-8 8-4-4 1.5-1.5L4 10l6.5-6.5z"/></svg>
              <span class="select-menu-item-text css-truncate-target js-select-menu-filter-text">
                remove-authz
              </span>
            </a>
            <a class="select-menu-item js-navigation-item js-navigation-open "
               href="/ckan/ckan/blob/remove-ckan-abbreviation-explanations/ckan/config/routing.py"
               data-name="remove-ckan-abbreviation-explanations"
               data-skip-pjax="true"
               rel="nofollow">
              <svg aria-hidden="true" class="octicon octicon-check select-menu-item-icon" height="16" version="1.1" viewBox="0 0 12 16" width="12"><path fill-rule="evenodd" d="M12 5l-8 8-4-4 1.5-1.5L4 10l6.5-6.5z"/></svg>
              <span class="select-menu-item-text css-truncate-target js-select-menu-filter-text">
                remove-ckan-abbreviation-explanations
              </span>
            </a>
            <a class="select-menu-item js-navigation-item js-navigation-open "
               href="/ckan/ckan/blob/remove-dumper/ckan/config/routing.py"
               data-name="remove-dumper"
               data-skip-pjax="true"
               rel="nofollow">
              <svg aria-hidden="true" class="octicon octicon-check select-menu-item-icon" height="16" version="1.1" viewBox="0 0 12 16" width="12"><path fill-rule="evenodd" d="M12 5l-8 8-4-4 1.5-1.5L4 10l6.5-6.5z"/></svg>
              <span class="select-menu-item-text css-truncate-target js-select-menu-filter-text">
                remove-dumper
              </span>
            </a>
            <a class="select-menu-item js-navigation-item js-navigation-open "
               href="/ckan/ckan/blob/remove-duplicate-debug-from-ini-file/ckan/config/routing.py"
               data-name="remove-duplicate-debug-from-ini-file"
               data-skip-pjax="true"
               rel="nofollow">
              <svg aria-hidden="true" class="octicon octicon-check select-menu-item-icon" height="16" version="1.1" viewBox="0 0 12 16" width="12"><path fill-rule="evenodd" d="M12 5l-8 8-4-4 1.5-1.5L4 10l6.5-6.5z"/></svg>
              <span class="select-menu-item-text css-truncate-target js-select-menu-filter-text">
                remove-duplicate-debug-from-ini-file
              </span>
            </a>
            <a class="select-menu-item js-navigation-item js-navigation-open "
               href="/ckan/ckan/blob/remove-migrate-versions-on-clean/ckan/config/routing.py"
               data-name="remove-migrate-versions-on-clean"
               data-skip-pjax="true"
               rel="nofollow">
              <svg aria-hidden="true" class="octicon octicon-check select-menu-item-icon" height="16" version="1.1" viewBox="0 0 12 16" width="12"><path fill-rule="evenodd" d="M12 5l-8 8-4-4 1.5-1.5L4 10l6.5-6.5z"/></svg>
              <span class="select-menu-item-text css-truncate-target js-select-menu-filter-text">
                remove-migrate-versions-on-clean
              </span>
            </a>
            <a class="select-menu-item js-navigation-item js-navigation-open "
               href="/ckan/ckan/blob/remove-python-2.5-statement/ckan/config/routing.py"
               data-name="remove-python-2.5-statement"
               data-skip-pjax="true"
               rel="nofollow">
              <svg aria-hidden="true" class="octicon octicon-check select-menu-item-icon" height="16" version="1.1" viewBox="0 0 12 16" width="12"><path fill-rule="evenodd" d="M12 5l-8 8-4-4 1.5-1.5L4 10l6.5-6.5z"/></svg>
              <span class="select-menu-item-text css-truncate-target js-select-menu-filter-text">
                remove-python-2.5-statement
              </span>
            </a>
            <a class="select-menu-item js-navigation-item js-navigation-open "
               href="/ckan/ckan/blob/remove-routes-submapper/ckan/config/routing.py"
               data-name="remove-routes-submapper"
               data-skip-pjax="true"
               rel="nofollow">
              <svg aria-hidden="true" class="octicon octicon-check select-menu-item-icon" height="16" version="1.1" viewBox="0 0 12 16" width="12"><path fill-rule="evenodd" d="M12 5l-8 8-4-4 1.5-1.5L4 10l6.5-6.5z"/></svg>
              <span class="select-menu-item-text css-truncate-target js-select-menu-filter-text">
                remove-routes-submapper
              </span>
            </a>
            <a class="select-menu-item js-navigation-item js-navigation-open "
               href="/ckan/ckan/blob/remove-webstore-fields/ckan/config/routing.py"
               data-name="remove-webstore-fields"
               data-skip-pjax="true"
               rel="nofollow">
              <svg aria-hidden="true" class="octicon octicon-check select-menu-item-icon" height="16" version="1.1" viewBox="0 0 12 16" width="12"><path fill-rule="evenodd" d="M12 5l-8 8-4-4 1.5-1.5L4 10l6.5-6.5z"/></svg>
              <span class="select-menu-item-text css-truncate-target js-select-menu-filter-text">
                remove-webstore-fields
              </span>
            </a>
            <a class="select-menu-item js-navigation-item js-navigation-open "
               href="/ckan/ckan/blob/replace-markdown-lib/ckan/config/routing.py"
               data-name="replace-markdown-lib"
               data-skip-pjax="true"
               rel="nofollow">
              <svg aria-hidden="true" class="octicon octicon-check select-menu-item-icon" height="16" version="1.1" viewBox="0 0 12 16" width="12"><path fill-rule="evenodd" d="M12 5l-8 8-4-4 1.5-1.5L4 10l6.5-6.5z"/></svg>
              <span class="select-menu-item-text css-truncate-target js-select-menu-filter-text">
                replace-markdown-lib
              </span>
            </a>
            <a class="select-menu-item js-navigation-item js-navigation-open "
               href="/ckan/ckan/blob/repo-change/ckan/config/routing.py"
               data-name="repo-change"
               data-skip-pjax="true"
               rel="nofollow">
              <svg aria-hidden="true" class="octicon octicon-check select-menu-item-icon" height="16" version="1.1" viewBox="0 0 12 16" width="12"><path fill-rule="evenodd" d="M12 5l-8 8-4-4 1.5-1.5L4 10l6.5-6.5z"/></svg>
              <span class="select-menu-item-text css-truncate-target js-select-menu-filter-text">
                repo-change
              </span>
            </a>
            <a class="select-menu-item js-navigation-item js-navigation-open "
               href="/ckan/ckan/blob/req-test/ckan/config/routing.py"
               data-name="req-test"
               data-skip-pjax="true"
               rel="nofollow">
              <svg aria-hidden="true" class="octicon octicon-check select-menu-item-icon" height="16" version="1.1" viewBox="0 0 12 16" width="12"><path fill-rule="evenodd" d="M12 5l-8 8-4-4 1.5-1.5L4 10l6.5-6.5z"/></svg>
              <span class="select-menu-item-text css-truncate-target js-select-menu-filter-text">
                req-test
              </span>
            </a>
            <a class="select-menu-item js-navigation-item js-navigation-open "
               href="/ckan/ckan/blob/reqs-docs/ckan/config/routing.py"
               data-name="reqs-docs"
               data-skip-pjax="true"
               rel="nofollow">
              <svg aria-hidden="true" class="octicon octicon-check select-menu-item-icon" height="16" version="1.1" viewBox="0 0 12 16" width="12"><path fill-rule="evenodd" d="M12 5l-8 8-4-4 1.5-1.5L4 10l6.5-6.5z"/></svg>
              <span class="select-menu-item-text css-truncate-target js-select-menu-filter-text">
                reqs-docs
              </span>
            </a>
            <a class="select-menu-item js-navigation-item js-navigation-open "
               href="/ckan/ckan/blob/resource_update-use-package_update/ckan/config/routing.py"
               data-name="resource_update-use-package_update"
               data-skip-pjax="true"
               rel="nofollow">
              <svg aria-hidden="true" class="octicon octicon-check select-menu-item-icon" height="16" version="1.1" viewBox="0 0 12 16" width="12"><path fill-rule="evenodd" d="M12 5l-8 8-4-4 1.5-1.5L4 10l6.5-6.5z"/></svg>
              <span class="select-menu-item-text css-truncate-target js-select-menu-filter-text">
                resource_update-use-package_update
              </span>
            </a>
            <a class="select-menu-item js-navigation-item js-navigation-open "
               href="/ckan/ckan/blob/responsive-2.2/ckan/config/routing.py"
               data-name="responsive-2.2"
               data-skip-pjax="true"
               rel="nofollow">
              <svg aria-hidden="true" class="octicon octicon-check select-menu-item-icon" height="16" version="1.1" viewBox="0 0 12 16" width="12"><path fill-rule="evenodd" d="M12 5l-8 8-4-4 1.5-1.5L4 10l6.5-6.5z"/></svg>
              <span class="select-menu-item-text css-truncate-target js-select-menu-filter-text">
                responsive-2.2
              </span>
            </a>
            <a class="select-menu-item js-navigation-item js-navigation-open "
               href="/ckan/ckan/blob/revert-2698-2697-like-query-autocomplete/ckan/config/routing.py"
               data-name="revert-2698-2697-like-query-autocomplete"
               data-skip-pjax="true"
               rel="nofollow">
              <svg aria-hidden="true" class="octicon octicon-check select-menu-item-icon" height="16" version="1.1" viewBox="0 0 12 16" width="12"><path fill-rule="evenodd" d="M12 5l-8 8-4-4 1.5-1.5L4 10l6.5-6.5z"/></svg>
              <span class="select-menu-item-text css-truncate-target js-select-menu-filter-text">
                revert-2698-2697-like-query-autocomplete
              </span>
            </a>
            <a class="select-menu-item js-navigation-item js-navigation-open "
               href="/ckan/ckan/blob/revision-list-limit/ckan/config/routing.py"
               data-name="revision-list-limit"
               data-skip-pjax="true"
               rel="nofollow">
              <svg aria-hidden="true" class="octicon octicon-check select-menu-item-icon" height="16" version="1.1" viewBox="0 0 12 16" width="12"><path fill-rule="evenodd" d="M12 5l-8 8-4-4 1.5-1.5L4 10l6.5-6.5z"/></svg>
              <span class="select-menu-item-text css-truncate-target js-select-menu-filter-text">
                revision-list-limit
              </span>
            </a>
            <a class="select-menu-item js-navigation-item js-navigation-open "
               href="/ckan/ckan/blob/ross-broken-ecportal-fixes/ckan/config/routing.py"
               data-name="ross-broken-ecportal-fixes"
               data-skip-pjax="true"
               rel="nofollow">
              <svg aria-hidden="true" class="octicon octicon-check select-menu-item-icon" height="16" version="1.1" viewBox="0 0 12 16" width="12"><path fill-rule="evenodd" d="M12 5l-8 8-4-4 1.5-1.5L4 10l6.5-6.5z"/></svg>
              <span class="select-menu-item-text css-truncate-target js-select-menu-filter-text">
                ross-broken-ecportal-fixes
              </span>
            </a>
            <a class="select-menu-item js-navigation-item js-navigation-open "
               href="/ckan/ckan/blob/rq/ckan/config/routing.py"
               data-name="rq"
               data-skip-pjax="true"
               rel="nofollow">
              <svg aria-hidden="true" class="octicon octicon-check select-menu-item-icon" height="16" version="1.1" viewBox="0 0 12 16" width="12"><path fill-rule="evenodd" d="M12 5l-8 8-4-4 1.5-1.5L4 10l6.5-6.5z"/></svg>
              <span class="select-menu-item-text css-truncate-target js-select-menu-filter-text">
                rq
              </span>
            </a>
            <a class="select-menu-item js-navigation-item js-navigation-open "
               href="/ckan/ckan/blob/search_form_id/ckan/config/routing.py"
               data-name="search_form_id"
               data-skip-pjax="true"
               rel="nofollow">
              <svg aria-hidden="true" class="octicon octicon-check select-menu-item-icon" height="16" version="1.1" viewBox="0 0 12 16" width="12"><path fill-rule="evenodd" d="M12 5l-8 8-4-4 1.5-1.5L4 10l6.5-6.5z"/></svg>
              <span class="select-menu-item-text css-truncate-target js-select-menu-filter-text">
                search_form_id
              </span>
            </a>
            <a class="select-menu-item js-navigation-item js-navigation-open "
               href="/ckan/ckan/blob/search_user_context/ckan/config/routing.py"
               data-name="search_user_context"
               data-skip-pjax="true"
               rel="nofollow">
              <svg aria-hidden="true" class="octicon octicon-check select-menu-item-icon" height="16" version="1.1" viewBox="0 0 12 16" width="12"><path fill-rule="evenodd" d="M12 5l-8 8-4-4 1.5-1.5L4 10l6.5-6.5z"/></svg>
              <span class="select-menu-item-text css-truncate-target js-select-menu-filter-text">
                search_user_context
              </span>
            </a>
            <a class="select-menu-item js-navigation-item js-navigation-open "
               href="/ckan/ckan/blob/site-url-clarification/ckan/config/routing.py"
               data-name="site-url-clarification"
               data-skip-pjax="true"
               rel="nofollow">
              <svg aria-hidden="true" class="octicon octicon-check select-menu-item-icon" height="16" version="1.1" viewBox="0 0 12 16" width="12"><path fill-rule="evenodd" d="M12 5l-8 8-4-4 1.5-1.5L4 10l6.5-6.5z"/></svg>
              <span class="select-menu-item-text css-truncate-target js-select-menu-filter-text">
                site-url-clarification
              </span>
            </a>
            <a class="select-menu-item js-navigation-item js-navigation-open "
               href="/ckan/ckan/blob/solr-docs-reorg/ckan/config/routing.py"
               data-name="solr-docs-reorg"
               data-skip-pjax="true"
               rel="nofollow">
              <svg aria-hidden="true" class="octicon octicon-check select-menu-item-icon" height="16" version="1.1" viewBox="0 0 12 16" width="12"><path fill-rule="evenodd" d="M12 5l-8 8-4-4 1.5-1.5L4 10l6.5-6.5z"/></svg>
              <span class="select-menu-item-text css-truncate-target js-select-menu-filter-text">
                solr-docs-reorg
              </span>
            </a>
            <a class="select-menu-item js-navigation-item js-navigation-open "
               href="/ckan/ckan/blob/sort-exception/ckan/config/routing.py"
               data-name="sort-exception"
               data-skip-pjax="true"
               rel="nofollow">
              <svg aria-hidden="true" class="octicon octicon-check select-menu-item-icon" height="16" version="1.1" viewBox="0 0 12 16" width="12"><path fill-rule="evenodd" d="M12 5l-8 8-4-4 1.5-1.5L4 10l6.5-6.5z"/></svg>
              <span class="select-menu-item-text css-truncate-target js-select-menu-filter-text">
                sort-exception
              </span>
            </a>
            <a class="select-menu-item js-navigation-item js-navigation-open "
               href="/ckan/ckan/blob/sort-exception2/ckan/config/routing.py"
               data-name="sort-exception2"
               data-skip-pjax="true"
               rel="nofollow">
              <svg aria-hidden="true" class="octicon octicon-check select-menu-item-icon" height="16" version="1.1" viewBox="0 0 12 16" width="12"><path fill-rule="evenodd" d="M12 5l-8 8-4-4 1.5-1.5L4 10l6.5-6.5z"/></svg>
              <span class="select-menu-item-text css-truncate-target js-select-menu-filter-text">
                sort-exception2
              </span>
            </a>
            <a class="select-menu-item js-navigation-item js-navigation-open "
               href="/ckan/ckan/blob/source-install-docs-reorg/ckan/config/routing.py"
               data-name="source-install-docs-reorg"
               data-skip-pjax="true"
               rel="nofollow">
              <svg aria-hidden="true" class="octicon octicon-check select-menu-item-icon" height="16" version="1.1" viewBox="0 0 12 16" width="12"><path fill-rule="evenodd" d="M12 5l-8 8-4-4 1.5-1.5L4 10l6.5-6.5z"/></svg>
              <span class="select-menu-item-text css-truncate-target js-select-menu-filter-text">
                source-install-docs-reorg
              </span>
            </a>
            <a class="select-menu-item js-navigation-item js-navigation-open "
               href="/ckan/ckan/blob/sql-params/ckan/config/routing.py"
               data-name="sql-params"
               data-skip-pjax="true"
               rel="nofollow">
              <svg aria-hidden="true" class="octicon octicon-check select-menu-item-icon" height="16" version="1.1" viewBox="0 0 12 16" width="12"><path fill-rule="evenodd" d="M12 5l-8 8-4-4 1.5-1.5L4 10l6.5-6.5z"/></svg>
              <span class="select-menu-item-text css-truncate-target js-select-menu-filter-text">
                sql-params
              </span>
            </a>
            <a class="select-menu-item js-navigation-item js-navigation-open "
               href="/ckan/ckan/blob/sss-2014-sk-translation/ckan/config/routing.py"
               data-name="sss-2014-sk-translation"
               data-skip-pjax="true"
               rel="nofollow">
              <svg aria-hidden="true" class="octicon octicon-check select-menu-item-icon" height="16" version="1.1" viewBox="0 0 12 16" width="12"><path fill-rule="evenodd" d="M12 5l-8 8-4-4 1.5-1.5L4 10l6.5-6.5z"/></svg>
              <span class="select-menu-item-text css-truncate-target js-select-menu-filter-text">
                sss-2014-sk-translation
              </span>
            </a>
            <a class="select-menu-item js-navigation-item js-navigation-open "
               href="/ckan/ckan/blob/stable/ckan/config/routing.py"
               data-name="stable"
               data-skip-pjax="true"
               rel="nofollow">
              <svg aria-hidden="true" class="octicon octicon-check select-menu-item-icon" height="16" version="1.1" viewBox="0 0 12 16" width="12"><path fill-rule="evenodd" d="M12 5l-8 8-4-4 1.5-1.5L4 10l6.5-6.5z"/></svg>
              <span class="select-menu-item-text css-truncate-target js-select-menu-filter-text">
                stable
              </span>
            </a>
            <a class="select-menu-item js-navigation-item js-navigation-open "
               href="/ckan/ckan/blob/start-cli-cleanup/ckan/config/routing.py"
               data-name="start-cli-cleanup"
               data-skip-pjax="true"
               rel="nofollow">
              <svg aria-hidden="true" class="octicon octicon-check select-menu-item-icon" height="16" version="1.1" viewBox="0 0 12 16" width="12"><path fill-rule="evenodd" d="M12 5l-8 8-4-4 1.5-1.5L4 10l6.5-6.5z"/></svg>
              <span class="select-menu-item-text css-truncate-target js-select-menu-filter-text">
                start-cli-cleanup
              </span>
            </a>
            <a class="select-menu-item js-navigation-item js-navigation-open "
               href="/ckan/ckan/blob/supervisor-typo/ckan/config/routing.py"
               data-name="supervisor-typo"
               data-skip-pjax="true"
               rel="nofollow">
              <svg aria-hidden="true" class="octicon octicon-check select-menu-item-icon" height="16" version="1.1" viewBox="0 0 12 16" width="12"><path fill-rule="evenodd" d="M12 5l-8 8-4-4 1.5-1.5L4 10l6.5-6.5z"/></svg>
              <span class="select-menu-item-text css-truncate-target js-select-menu-filter-text">
                supervisor-typo
              </span>
            </a>
            <a class="select-menu-item js-navigation-item js-navigation-open "
               href="/ckan/ckan/blob/support-env-vars-in-make-config/ckan/config/routing.py"
               data-name="support-env-vars-in-make-config"
               data-skip-pjax="true"
               rel="nofollow">
              <svg aria-hidden="true" class="octicon octicon-check select-menu-item-icon" height="16" version="1.1" viewBox="0 0 12 16" width="12"><path fill-rule="evenodd" d="M12 5l-8 8-4-4 1.5-1.5L4 10l6.5-6.5z"/></svg>
              <span class="select-menu-item-text css-truncate-target js-select-menu-filter-text">
                support-env-vars-in-make-config
              </span>
            </a>
            <a class="select-menu-item js-navigation-item js-navigation-open "
               href="/ckan/ckan/blob/task-2437-add-coding-standards-to-ckan-docs/ckan/config/routing.py"
               data-name="task-2437-add-coding-standards-to-ckan-docs"
               data-skip-pjax="true"
               rel="nofollow">
              <svg aria-hidden="true" class="octicon octicon-check select-menu-item-icon" height="16" version="1.1" viewBox="0 0 12 16" width="12"><path fill-rule="evenodd" d="M12 5l-8 8-4-4 1.5-1.5L4 10l6.5-6.5z"/></svg>
              <span class="select-menu-item-text css-truncate-target js-select-menu-filter-text">
                task-2437-add-coding-standards-to-ckan-docs
              </span>
            </a>
            <a class="select-menu-item js-navigation-item js-navigation-open "
               href="/ckan/ckan/blob/test-cli-autodoc/ckan/config/routing.py"
               data-name="test-cli-autodoc"
               data-skip-pjax="true"
               rel="nofollow">
              <svg aria-hidden="true" class="octicon octicon-check select-menu-item-icon" height="16" version="1.1" viewBox="0 0 12 16" width="12"><path fill-rule="evenodd" d="M12 5l-8 8-4-4 1.5-1.5L4 10l6.5-6.5z"/></svg>
              <span class="select-menu-item-text css-truncate-target js-select-menu-filter-text">
                test-cli-autodoc
              </span>
            </a>
            <a class="select-menu-item js-navigation-item js-navigation-open "
               href="/ckan/ckan/blob/tmp-fixing-build/ckan/config/routing.py"
               data-name="tmp-fixing-build"
               data-skip-pjax="true"
               rel="nofollow">
              <svg aria-hidden="true" class="octicon octicon-check select-menu-item-icon" height="16" version="1.1" viewBox="0 0 12 16" width="12"><path fill-rule="evenodd" d="M12 5l-8 8-4-4 1.5-1.5L4 10l6.5-6.5z"/></svg>
              <span class="select-menu-item-text css-truncate-target js-select-menu-filter-text">
                tmp-fixing-build
              </span>
            </a>
            <a class="select-menu-item js-navigation-item js-navigation-open "
               href="/ckan/ckan/blob/tmp-implement-group-purging-branched-off-2.0-for-datagm/ckan/config/routing.py"
               data-name="tmp-implement-group-purging-branched-off-2.0-for-datagm"
               data-skip-pjax="true"
               rel="nofollow">
              <svg aria-hidden="true" class="octicon octicon-check select-menu-item-icon" height="16" version="1.1" viewBox="0 0 12 16" width="12"><path fill-rule="evenodd" d="M12 5l-8 8-4-4 1.5-1.5L4 10l6.5-6.5z"/></svg>
              <span class="select-menu-item-text css-truncate-target js-select-menu-filter-text">
                tmp-implement-group-purging-branched-off-2.0-for-datagm
              </span>
            </a>
            <a class="select-menu-item js-navigation-item js-navigation-open "
               href="/ckan/ckan/blob/toolkit-import-fix/ckan/config/routing.py"
               data-name="toolkit-import-fix"
               data-skip-pjax="true"
               rel="nofollow">
              <svg aria-hidden="true" class="octicon octicon-check select-menu-item-icon" height="16" version="1.1" viewBox="0 0 12 16" width="12"><path fill-rule="evenodd" d="M12 5l-8 8-4-4 1.5-1.5L4 10l6.5-6.5z"/></svg>
              <span class="select-menu-item-text css-truncate-target js-select-menu-filter-text">
                toolkit-import-fix
              </span>
            </a>
            <a class="select-menu-item js-navigation-item js-navigation-open "
               href="/ckan/ckan/blob/tracking-fix-for-1.8/ckan/config/routing.py"
               data-name="tracking-fix-for-1.8"
               data-skip-pjax="true"
               rel="nofollow">
              <svg aria-hidden="true" class="octicon octicon-check select-menu-item-icon" height="16" version="1.1" viewBox="0 0 12 16" width="12"><path fill-rule="evenodd" d="M12 5l-8 8-4-4 1.5-1.5L4 10l6.5-6.5z"/></svg>
              <span class="select-menu-item-text css-truncate-target js-select-menu-filter-text">
                tracking-fix-for-1.8
              </span>
            </a>
            <a class="select-menu-item js-navigation-item js-navigation-open "
               href="/ckan/ckan/blob/tracking-fixes-branched-off-2.0/ckan/config/routing.py"
               data-name="tracking-fixes-branched-off-2.0"
               data-skip-pjax="true"
               rel="nofollow">
              <svg aria-hidden="true" class="octicon octicon-check select-menu-item-icon" height="16" version="1.1" viewBox="0 0 12 16" width="12"><path fill-rule="evenodd" d="M12 5l-8 8-4-4 1.5-1.5L4 10l6.5-6.5z"/></svg>
              <span class="select-menu-item-text css-truncate-target js-select-menu-filter-text">
                tracking-fixes-branched-off-2.0
              </span>
            </a>
            <a class="select-menu-item js-navigation-item js-navigation-open "
               href="/ckan/ckan/blob/tracking-patch/ckan/config/routing.py"
               data-name="tracking-patch"
               data-skip-pjax="true"
               rel="nofollow">
              <svg aria-hidden="true" class="octicon octicon-check select-menu-item-icon" height="16" version="1.1" viewBox="0 0 12 16" width="12"><path fill-rule="evenodd" d="M12 5l-8 8-4-4 1.5-1.5L4 10l6.5-6.5z"/></svg>
              <span class="select-menu-item-text css-truncate-target js-select-menu-filter-text">
                tracking-patch
              </span>
            </a>
            <a class="select-menu-item js-navigation-item js-navigation-open "
               href="/ckan/ckan/blob/travis-2.4.9/ckan/config/routing.py"
               data-name="travis-2.4.9"
               data-skip-pjax="true"
               rel="nofollow">
              <svg aria-hidden="true" class="octicon octicon-check select-menu-item-icon" height="16" version="1.1" viewBox="0 0 12 16" width="12"><path fill-rule="evenodd" d="M12 5l-8 8-4-4 1.5-1.5L4 10l6.5-6.5z"/></svg>
              <span class="select-menu-item-text css-truncate-target js-select-menu-filter-text">
                travis-2.4.9
              </span>
            </a>
            <a class="select-menu-item js-navigation-item js-navigation-open "
               href="/ckan/ckan/blob/travis-cleanup/ckan/config/routing.py"
               data-name="travis-cleanup"
               data-skip-pjax="true"
               rel="nofollow">
              <svg aria-hidden="true" class="octicon octicon-check select-menu-item-icon" height="16" version="1.1" viewBox="0 0 12 16" width="12"><path fill-rule="evenodd" d="M12 5l-8 8-4-4 1.5-1.5L4 10l6.5-6.5z"/></svg>
              <span class="select-menu-item-text css-truncate-target js-select-menu-filter-text">
                travis-cleanup
              </span>
            </a>
            <a class="select-menu-item js-navigation-item js-navigation-open "
               href="/ckan/ckan/blob/travis-docker/ckan/config/routing.py"
               data-name="travis-docker"
               data-skip-pjax="true"
               rel="nofollow">
              <svg aria-hidden="true" class="octicon octicon-check select-menu-item-icon" height="16" version="1.1" viewBox="0 0 12 16" width="12"><path fill-rule="evenodd" d="M12 5l-8 8-4-4 1.5-1.5L4 10l6.5-6.5z"/></svg>
              <span class="select-menu-item-text css-truncate-target js-select-menu-filter-text">
                travis-docker
              </span>
            </a>
            <a class="select-menu-item js-navigation-item js-navigation-open "
               href="/ckan/ckan/blob/travis-image-change/ckan/config/routing.py"
               data-name="travis-image-change"
               data-skip-pjax="true"
               rel="nofollow">
              <svg aria-hidden="true" class="octicon octicon-check select-menu-item-icon" height="16" version="1.1" viewBox="0 0 12 16" width="12"><path fill-rule="evenodd" d="M12 5l-8 8-4-4 1.5-1.5L4 10l6.5-6.5z"/></svg>
              <span class="select-menu-item-text css-truncate-target js-select-menu-filter-text">
                travis-image-change
              </span>
            </a>
            <a class="select-menu-item js-navigation-item js-navigation-open "
               href="/ckan/ckan/blob/travis-python-2.6/ckan/config/routing.py"
               data-name="travis-python-2.6"
               data-skip-pjax="true"
               rel="nofollow">
              <svg aria-hidden="true" class="octicon octicon-check select-menu-item-icon" height="16" version="1.1" viewBox="0 0 12 16" width="12"><path fill-rule="evenodd" d="M12 5l-8 8-4-4 1.5-1.5L4 10l6.5-6.5z"/></svg>
              <span class="select-menu-item-text css-truncate-target js-select-menu-filter-text">
                travis-python-2.6
              </span>
            </a>
            <a class="select-menu-item js-navigation-item js-navigation-open "
               href="/ckan/ckan/blob/travis-test-2.1/ckan/config/routing.py"
               data-name="travis-test-2.1"
               data-skip-pjax="true"
               rel="nofollow">
              <svg aria-hidden="true" class="octicon octicon-check select-menu-item-icon" height="16" version="1.1" viewBox="0 0 12 16" width="12"><path fill-rule="evenodd" d="M12 5l-8 8-4-4 1.5-1.5L4 10l6.5-6.5z"/></svg>
              <span class="select-menu-item-text css-truncate-target js-select-menu-filter-text">
                travis-test-2.1
              </span>
            </a>
            <a class="select-menu-item js-navigation-item js-navigation-open "
               href="/ckan/ckan/blob/travis.py/ckan/config/routing.py"
               data-name="travis.py"
               data-skip-pjax="true"
               rel="nofollow">
              <svg aria-hidden="true" class="octicon octicon-check select-menu-item-icon" height="16" version="1.1" viewBox="0 0 12 16" width="12"><path fill-rule="evenodd" d="M12 5l-8 8-4-4 1.5-1.5L4 10l6.5-6.5z"/></svg>
              <span class="select-menu-item-text css-truncate-target js-select-menu-filter-text">
                travis.py
              </span>
            </a>
            <a class="select-menu-item js-navigation-item js-navigation-open "
               href="/ckan/ckan/blob/typo-constriants/ckan/config/routing.py"
               data-name="typo-constriants"
               data-skip-pjax="true"
               rel="nofollow">
              <svg aria-hidden="true" class="octicon octicon-check select-menu-item-icon" height="16" version="1.1" viewBox="0 0 12 16" width="12"><path fill-rule="evenodd" d="M12 5l-8 8-4-4 1.5-1.5L4 10l6.5-6.5z"/></svg>
              <span class="select-menu-item-text css-truncate-target js-select-menu-filter-text">
                typo-constriants
              </span>
            </a>
            <a class="select-menu-item js-navigation-item js-navigation-open "
               href="/ckan/ckan/blob/ubuntu-16.04/ckan/config/routing.py"
               data-name="ubuntu-16.04"
               data-skip-pjax="true"
               rel="nofollow">
              <svg aria-hidden="true" class="octicon octicon-check select-menu-item-icon" height="16" version="1.1" viewBox="0 0 12 16" width="12"><path fill-rule="evenodd" d="M12 5l-8 8-4-4 1.5-1.5L4 10l6.5-6.5z"/></svg>
              <span class="select-menu-item-text css-truncate-target js-select-menu-filter-text">
                ubuntu-16.04
              </span>
            </a>
            <a class="select-menu-item js-navigation-item js-navigation-open "
               href="/ckan/ckan/blob/ultrastable/ckan/config/routing.py"
               data-name="ultrastable"
               data-skip-pjax="true"
               rel="nofollow">
              <svg aria-hidden="true" class="octicon octicon-check select-menu-item-icon" height="16" version="1.1" viewBox="0 0 12 16" width="12"><path fill-rule="evenodd" d="M12 5l-8 8-4-4 1.5-1.5L4 10l6.5-6.5z"/></svg>
              <span class="select-menu-item-text css-truncate-target js-select-menu-filter-text">
                ultrastable
              </span>
            </a>
            <a class="select-menu-item js-navigation-item js-navigation-open "
               href="/ckan/ckan/blob/unicode_user_names/ckan/config/routing.py"
               data-name="unicode_user_names"
               data-skip-pjax="true"
               rel="nofollow">
              <svg aria-hidden="true" class="octicon octicon-check select-menu-item-icon" height="16" version="1.1" viewBox="0 0 12 16" width="12"><path fill-rule="evenodd" d="M12 5l-8 8-4-4 1.5-1.5L4 10l6.5-6.5z"/></svg>
              <span class="select-menu-item-text css-truncate-target js-select-menu-filter-text">
                unicode_user_names
              </span>
            </a>
            <a class="select-menu-item js-navigation-item js-navigation-open "
               href="/ckan/ckan/blob/update-changeloge-for-2.0/ckan/config/routing.py"
               data-name="update-changeloge-for-2.0"
               data-skip-pjax="true"
               rel="nofollow">
              <svg aria-hidden="true" class="octicon octicon-check select-menu-item-icon" height="16" version="1.1" viewBox="0 0 12 16" width="12"><path fill-rule="evenodd" d="M12 5l-8 8-4-4 1.5-1.5L4 10l6.5-6.5z"/></svg>
              <span class="select-menu-item-text css-truncate-target js-select-menu-filter-text">
                update-changeloge-for-2.0
              </span>
            </a>
            <a class="select-menu-item js-navigation-item js-navigation-open "
               href="/ckan/ckan/blob/update-copyright/ckan/config/routing.py"
               data-name="update-copyright"
               data-skip-pjax="true"
               rel="nofollow">
              <svg aria-hidden="true" class="octicon octicon-check select-menu-item-icon" height="16" version="1.1" viewBox="0 0 12 16" width="12"><path fill-rule="evenodd" d="M12 5l-8 8-4-4 1.5-1.5L4 10l6.5-6.5z"/></svg>
              <span class="select-menu-item-text css-truncate-target js-select-menu-filter-text">
                update-copyright
              </span>
            </a>
            <a class="select-menu-item js-navigation-item js-navigation-open "
               href="/ckan/ckan/blob/update-setup-py/ckan/config/routing.py"
               data-name="update-setup-py"
               data-skip-pjax="true"
               rel="nofollow">
              <svg aria-hidden="true" class="octicon octicon-check select-menu-item-icon" height="16" version="1.1" viewBox="0 0 12 16" width="12"><path fill-rule="evenodd" d="M12 5l-8 8-4-4 1.5-1.5L4 10l6.5-6.5z"/></svg>
              <span class="select-menu-item-text css-truncate-target js-select-menu-filter-text">
                update-setup-py
              </span>
            </a>
            <a class="select-menu-item js-navigation-item js-navigation-open "
               href="/ckan/ckan/blob/upgrade-dependencies/ckan/config/routing.py"
               data-name="upgrade-dependencies"
               data-skip-pjax="true"
               rel="nofollow">
              <svg aria-hidden="true" class="octicon octicon-check select-menu-item-icon" height="16" version="1.1" viewBox="0 0 12 16" width="12"><path fill-rule="evenodd" d="M12 5l-8 8-4-4 1.5-1.5L4 10l6.5-6.5z"/></svg>
              <span class="select-menu-item-text css-truncate-target js-select-menu-filter-text">
                upgrade-dependencies
              </span>
            </a>
            <a class="select-menu-item js-navigation-item js-navigation-open "
               href="/ckan/ckan/blob/upgrade-sqlalchemy-to-1.1/ckan/config/routing.py"
               data-name="upgrade-sqlalchemy-to-1.1"
               data-skip-pjax="true"
               rel="nofollow">
              <svg aria-hidden="true" class="octicon octicon-check select-menu-item-icon" height="16" version="1.1" viewBox="0 0 12 16" width="12"><path fill-rule="evenodd" d="M12 5l-8 8-4-4 1.5-1.5L4 10l6.5-6.5z"/></svg>
              <span class="select-menu-item-text css-truncate-target js-select-menu-filter-text">
                upgrade-sqlalchemy-to-1.1
              </span>
            </a>
            <a class="select-menu-item js-navigation-item js-navigation-open "
               href="/ckan/ckan/blob/use-travis-containers/ckan/config/routing.py"
               data-name="use-travis-containers"
               data-skip-pjax="true"
               rel="nofollow">
              <svg aria-hidden="true" class="octicon octicon-check select-menu-item-icon" height="16" version="1.1" viewBox="0 0 12 16" width="12"><path fill-rule="evenodd" d="M12 5l-8 8-4-4 1.5-1.5L4 10l6.5-6.5z"/></svg>
              <span class="select-menu-item-text css-truncate-target js-select-menu-filter-text">
                use-travis-containers
              </span>
            </a>
            <a class="select-menu-item js-navigation-item js-navigation-open "
               href="/ckan/ckan/blob/user_delete_not_found/ckan/config/routing.py"
               data-name="user_delete_not_found"
               data-skip-pjax="true"
               rel="nofollow">
              <svg aria-hidden="true" class="octicon octicon-check select-menu-item-icon" height="16" version="1.1" viewBox="0 0 12 16" width="12"><path fill-rule="evenodd" d="M12 5l-8 8-4-4 1.5-1.5L4 10l6.5-6.5z"/></svg>
              <span class="select-menu-item-text css-truncate-target js-select-menu-filter-text">
                user_delete_not_found
              </span>
            </a>
            <a class="select-menu-item js-navigation-item js-navigation-open "
               href="/ckan/ckan/blob/user_extras/ckan/config/routing.py"
               data-name="user_extras"
               data-skip-pjax="true"
               rel="nofollow">
              <svg aria-hidden="true" class="octicon octicon-check select-menu-item-icon" height="16" version="1.1" viewBox="0 0 12 16" width="12"><path fill-rule="evenodd" d="M12 5l-8 8-4-4 1.5-1.5L4 10l6.5-6.5z"/></svg>
              <span class="select-menu-item-text css-truncate-target js-select-menu-filter-text">
                user_extras
              </span>
            </a>
        </div>

          <div class="select-menu-no-results">Nothing to show</div>
      </div>

      <div class="select-menu-list select-menu-tab-bucket js-select-menu-tab-bucket" data-tab-filter="tags">
        <div data-filterable-for="context-commitish-filter-field" data-filterable-type="substring">


            <a class="select-menu-item js-navigation-item js-navigation-open "
              href="/ckan/ckan/tree/demo-0.2/ckan/config/routing.py"
              data-name="demo-0.2"
              data-skip-pjax="true"
              rel="nofollow">
              <svg aria-hidden="true" class="octicon octicon-check select-menu-item-icon" height="16" version="1.1" viewBox="0 0 12 16" width="12"><path fill-rule="evenodd" d="M12 5l-8 8-4-4 1.5-1.5L4 10l6.5-6.5z"/></svg>
              <span class="select-menu-item-text css-truncate-target" title="demo-0.2">
                demo-0.2
              </span>
            </a>
            <a class="select-menu-item js-navigation-item js-navigation-open "
              href="/ckan/ckan/tree/demo-0.1/ckan/config/routing.py"
              data-name="demo-0.1"
              data-skip-pjax="true"
              rel="nofollow">
              <svg aria-hidden="true" class="octicon octicon-check select-menu-item-icon" height="16" version="1.1" viewBox="0 0 12 16" width="12"><path fill-rule="evenodd" d="M12 5l-8 8-4-4 1.5-1.5L4 10l6.5-6.5z"/></svg>
              <span class="select-menu-item-text css-truncate-target" title="demo-0.1">
                demo-0.1
              </span>
            </a>
            <a class="select-menu-item js-navigation-item js-navigation-open "
              href="/ckan/ckan/tree/datagov-pre-idatasetform-changes/ckan/config/routing.py"
              data-name="datagov-pre-idatasetform-changes"
              data-skip-pjax="true"
              rel="nofollow">
              <svg aria-hidden="true" class="octicon octicon-check select-menu-item-icon" height="16" version="1.1" viewBox="0 0 12 16" width="12"><path fill-rule="evenodd" d="M12 5l-8 8-4-4 1.5-1.5L4 10l6.5-6.5z"/></svg>
              <span class="select-menu-item-text css-truncate-target" title="datagov-pre-idatasetform-changes">
                datagov-pre-idatasetform-changes
              </span>
            </a>
            <a class="select-menu-item js-navigation-item js-navigation-open "
              href="/ckan/ckan/tree/ckan-2.7.2/ckan/config/routing.py"
              data-name="ckan-2.7.2"
              data-skip-pjax="true"
              rel="nofollow">
              <svg aria-hidden="true" class="octicon octicon-check select-menu-item-icon" height="16" version="1.1" viewBox="0 0 12 16" width="12"><path fill-rule="evenodd" d="M12 5l-8 8-4-4 1.5-1.5L4 10l6.5-6.5z"/></svg>
              <span class="select-menu-item-text css-truncate-target" title="ckan-2.7.2">
                ckan-2.7.2
              </span>
            </a>
            <a class="select-menu-item js-navigation-item js-navigation-open "
              href="/ckan/ckan/tree/ckan-2.7.1/ckan/config/routing.py"
              data-name="ckan-2.7.1"
              data-skip-pjax="true"
              rel="nofollow">
              <svg aria-hidden="true" class="octicon octicon-check select-menu-item-icon" height="16" version="1.1" viewBox="0 0 12 16" width="12"><path fill-rule="evenodd" d="M12 5l-8 8-4-4 1.5-1.5L4 10l6.5-6.5z"/></svg>
              <span class="select-menu-item-text css-truncate-target" title="ckan-2.7.1">
                ckan-2.7.1
              </span>
            </a>
            <a class="select-menu-item js-navigation-item js-navigation-open "
              href="/ckan/ckan/tree/ckan-2.7.0/ckan/config/routing.py"
              data-name="ckan-2.7.0"
              data-skip-pjax="true"
              rel="nofollow">
              <svg aria-hidden="true" class="octicon octicon-check select-menu-item-icon" height="16" version="1.1" viewBox="0 0 12 16" width="12"><path fill-rule="evenodd" d="M12 5l-8 8-4-4 1.5-1.5L4 10l6.5-6.5z"/></svg>
              <span class="select-menu-item-text css-truncate-target" title="ckan-2.7.0">
                ckan-2.7.0
              </span>
            </a>
            <a class="select-menu-item js-navigation-item js-navigation-open "
              href="/ckan/ckan/tree/ckan-2.6.4/ckan/config/routing.py"
              data-name="ckan-2.6.4"
              data-skip-pjax="true"
              rel="nofollow">
              <svg aria-hidden="true" class="octicon octicon-check select-menu-item-icon" height="16" version="1.1" viewBox="0 0 12 16" width="12"><path fill-rule="evenodd" d="M12 5l-8 8-4-4 1.5-1.5L4 10l6.5-6.5z"/></svg>
              <span class="select-menu-item-text css-truncate-target" title="ckan-2.6.4">
                ckan-2.6.4
              </span>
            </a>
            <a class="select-menu-item js-navigation-item js-navigation-open "
              href="/ckan/ckan/tree/ckan-2.6.3/ckan/config/routing.py"
              data-name="ckan-2.6.3"
              data-skip-pjax="true"
              rel="nofollow">
              <svg aria-hidden="true" class="octicon octicon-check select-menu-item-icon" height="16" version="1.1" viewBox="0 0 12 16" width="12"><path fill-rule="evenodd" d="M12 5l-8 8-4-4 1.5-1.5L4 10l6.5-6.5z"/></svg>
              <span class="select-menu-item-text css-truncate-target" title="ckan-2.6.3">
                ckan-2.6.3
              </span>
            </a>
            <a class="select-menu-item js-navigation-item js-navigation-open "
              href="/ckan/ckan/tree/ckan-2.6.2/ckan/config/routing.py"
              data-name="ckan-2.6.2"
              data-skip-pjax="true"
              rel="nofollow">
              <svg aria-hidden="true" class="octicon octicon-check select-menu-item-icon" height="16" version="1.1" viewBox="0 0 12 16" width="12"><path fill-rule="evenodd" d="M12 5l-8 8-4-4 1.5-1.5L4 10l6.5-6.5z"/></svg>
              <span class="select-menu-item-text css-truncate-target" title="ckan-2.6.2">
                ckan-2.6.2
              </span>
            </a>
            <a class="select-menu-item js-navigation-item js-navigation-open "
              href="/ckan/ckan/tree/ckan-2.6.1/ckan/config/routing.py"
              data-name="ckan-2.6.1"
              data-skip-pjax="true"
              rel="nofollow">
              <svg aria-hidden="true" class="octicon octicon-check select-menu-item-icon" height="16" version="1.1" viewBox="0 0 12 16" width="12"><path fill-rule="evenodd" d="M12 5l-8 8-4-4 1.5-1.5L4 10l6.5-6.5z"/></svg>
              <span class="select-menu-item-text css-truncate-target" title="ckan-2.6.1">
                ckan-2.6.1
              </span>
            </a>
            <a class="select-menu-item js-navigation-item js-navigation-open "
              href="/ckan/ckan/tree/ckan-2.6.0/ckan/config/routing.py"
              data-name="ckan-2.6.0"
              data-skip-pjax="true"
              rel="nofollow">
              <svg aria-hidden="true" class="octicon octicon-check select-menu-item-icon" height="16" version="1.1" viewBox="0 0 12 16" width="12"><path fill-rule="evenodd" d="M12 5l-8 8-4-4 1.5-1.5L4 10l6.5-6.5z"/></svg>
              <span class="select-menu-item-text css-truncate-target" title="ckan-2.6.0">
                ckan-2.6.0
              </span>
            </a>
            <a class="select-menu-item js-navigation-item js-navigation-open "
              href="/ckan/ckan/tree/ckan-2.5.7/ckan/config/routing.py"
              data-name="ckan-2.5.7"
              data-skip-pjax="true"
              rel="nofollow">
              <svg aria-hidden="true" class="octicon octicon-check select-menu-item-icon" height="16" version="1.1" viewBox="0 0 12 16" width="12"><path fill-rule="evenodd" d="M12 5l-8 8-4-4 1.5-1.5L4 10l6.5-6.5z"/></svg>
              <span class="select-menu-item-text css-truncate-target" title="ckan-2.5.7">
                ckan-2.5.7
              </span>
            </a>
            <a class="select-menu-item js-navigation-item js-navigation-open "
              href="/ckan/ckan/tree/ckan-2.5.6/ckan/config/routing.py"
              data-name="ckan-2.5.6"
              data-skip-pjax="true"
              rel="nofollow">
              <svg aria-hidden="true" class="octicon octicon-check select-menu-item-icon" height="16" version="1.1" viewBox="0 0 12 16" width="12"><path fill-rule="evenodd" d="M12 5l-8 8-4-4 1.5-1.5L4 10l6.5-6.5z"/></svg>
              <span class="select-menu-item-text css-truncate-target" title="ckan-2.5.6">
                ckan-2.5.6
              </span>
            </a>
            <a class="select-menu-item js-navigation-item js-navigation-open "
              href="/ckan/ckan/tree/ckan-2.5.5/ckan/config/routing.py"
              data-name="ckan-2.5.5"
              data-skip-pjax="true"
              rel="nofollow">
              <svg aria-hidden="true" class="octicon octicon-check select-menu-item-icon" height="16" version="1.1" viewBox="0 0 12 16" width="12"><path fill-rule="evenodd" d="M12 5l-8 8-4-4 1.5-1.5L4 10l6.5-6.5z"/></svg>
              <span class="select-menu-item-text css-truncate-target" title="ckan-2.5.5">
                ckan-2.5.5
              </span>
            </a>
            <a class="select-menu-item js-navigation-item js-navigation-open "
              href="/ckan/ckan/tree/ckan-2.5.4/ckan/config/routing.py"
              data-name="ckan-2.5.4"
              data-skip-pjax="true"
              rel="nofollow">
              <svg aria-hidden="true" class="octicon octicon-check select-menu-item-icon" height="16" version="1.1" viewBox="0 0 12 16" width="12"><path fill-rule="evenodd" d="M12 5l-8 8-4-4 1.5-1.5L4 10l6.5-6.5z"/></svg>
              <span class="select-menu-item-text css-truncate-target" title="ckan-2.5.4">
                ckan-2.5.4
              </span>
            </a>
            <a class="select-menu-item js-navigation-item js-navigation-open "
              href="/ckan/ckan/tree/ckan-2.5.3/ckan/config/routing.py"
              data-name="ckan-2.5.3"
              data-skip-pjax="true"
              rel="nofollow">
              <svg aria-hidden="true" class="octicon octicon-check select-menu-item-icon" height="16" version="1.1" viewBox="0 0 12 16" width="12"><path fill-rule="evenodd" d="M12 5l-8 8-4-4 1.5-1.5L4 10l6.5-6.5z"/></svg>
              <span class="select-menu-item-text css-truncate-target" title="ckan-2.5.3">
                ckan-2.5.3
              </span>
            </a>
            <a class="select-menu-item js-navigation-item js-navigation-open "
              href="/ckan/ckan/tree/ckan-2.5.2/ckan/config/routing.py"
              data-name="ckan-2.5.2"
              data-skip-pjax="true"
              rel="nofollow">
              <svg aria-hidden="true" class="octicon octicon-check select-menu-item-icon" height="16" version="1.1" viewBox="0 0 12 16" width="12"><path fill-rule="evenodd" d="M12 5l-8 8-4-4 1.5-1.5L4 10l6.5-6.5z"/></svg>
              <span class="select-menu-item-text css-truncate-target" title="ckan-2.5.2">
                ckan-2.5.2
              </span>
            </a>
            <a class="select-menu-item js-navigation-item js-navigation-open "
              href="/ckan/ckan/tree/ckan-2.5.1/ckan/config/routing.py"
              data-name="ckan-2.5.1"
              data-skip-pjax="true"
              rel="nofollow">
              <svg aria-hidden="true" class="octicon octicon-check select-menu-item-icon" height="16" version="1.1" viewBox="0 0 12 16" width="12"><path fill-rule="evenodd" d="M12 5l-8 8-4-4 1.5-1.5L4 10l6.5-6.5z"/></svg>
              <span class="select-menu-item-text css-truncate-target" title="ckan-2.5.1">
                ckan-2.5.1
              </span>
            </a>
            <a class="select-menu-item js-navigation-item js-navigation-open "
              href="/ckan/ckan/tree/ckan-2.5.0/ckan/config/routing.py"
              data-name="ckan-2.5.0"
              data-skip-pjax="true"
              rel="nofollow">
              <svg aria-hidden="true" class="octicon octicon-check select-menu-item-icon" height="16" version="1.1" viewBox="0 0 12 16" width="12"><path fill-rule="evenodd" d="M12 5l-8 8-4-4 1.5-1.5L4 10l6.5-6.5z"/></svg>
              <span class="select-menu-item-text css-truncate-target" title="ckan-2.5.0">
                ckan-2.5.0
              </span>
            </a>
            <a class="select-menu-item js-navigation-item js-navigation-open "
              href="/ckan/ckan/tree/ckan-2.4.9/ckan/config/routing.py"
              data-name="ckan-2.4.9"
              data-skip-pjax="true"
              rel="nofollow">
              <svg aria-hidden="true" class="octicon octicon-check select-menu-item-icon" height="16" version="1.1" viewBox="0 0 12 16" width="12"><path fill-rule="evenodd" d="M12 5l-8 8-4-4 1.5-1.5L4 10l6.5-6.5z"/></svg>
              <span class="select-menu-item-text css-truncate-target" title="ckan-2.4.9">
                ckan-2.4.9
              </span>
            </a>
            <a class="select-menu-item js-navigation-item js-navigation-open "
              href="/ckan/ckan/tree/ckan-2.4.8/ckan/config/routing.py"
              data-name="ckan-2.4.8"
              data-skip-pjax="true"
              rel="nofollow">
              <svg aria-hidden="true" class="octicon octicon-check select-menu-item-icon" height="16" version="1.1" viewBox="0 0 12 16" width="12"><path fill-rule="evenodd" d="M12 5l-8 8-4-4 1.5-1.5L4 10l6.5-6.5z"/></svg>
              <span class="select-menu-item-text css-truncate-target" title="ckan-2.4.8">
                ckan-2.4.8
              </span>
            </a>
            <a class="select-menu-item js-navigation-item js-navigation-open "
              href="/ckan/ckan/tree/ckan-2.4.7/ckan/config/routing.py"
              data-name="ckan-2.4.7"
              data-skip-pjax="true"
              rel="nofollow">
              <svg aria-hidden="true" class="octicon octicon-check select-menu-item-icon" height="16" version="1.1" viewBox="0 0 12 16" width="12"><path fill-rule="evenodd" d="M12 5l-8 8-4-4 1.5-1.5L4 10l6.5-6.5z"/></svg>
              <span class="select-menu-item-text css-truncate-target" title="ckan-2.4.7">
                ckan-2.4.7
              </span>
            </a>
            <a class="select-menu-item js-navigation-item js-navigation-open "
              href="/ckan/ckan/tree/ckan-2.4.6/ckan/config/routing.py"
              data-name="ckan-2.4.6"
              data-skip-pjax="true"
              rel="nofollow">
              <svg aria-hidden="true" class="octicon octicon-check select-menu-item-icon" height="16" version="1.1" viewBox="0 0 12 16" width="12"><path fill-rule="evenodd" d="M12 5l-8 8-4-4 1.5-1.5L4 10l6.5-6.5z"/></svg>
              <span class="select-menu-item-text css-truncate-target" title="ckan-2.4.6">
                ckan-2.4.6
              </span>
            </a>
            <a class="select-menu-item js-navigation-item js-navigation-open "
              href="/ckan/ckan/tree/ckan-2.4.5/ckan/config/routing.py"
              data-name="ckan-2.4.5"
              data-skip-pjax="true"
              rel="nofollow">
              <svg aria-hidden="true" class="octicon octicon-check select-menu-item-icon" height="16" version="1.1" viewBox="0 0 12 16" width="12"><path fill-rule="evenodd" d="M12 5l-8 8-4-4 1.5-1.5L4 10l6.5-6.5z"/></svg>
              <span class="select-menu-item-text css-truncate-target" title="ckan-2.4.5">
                ckan-2.4.5
              </span>
            </a>
            <a class="select-menu-item js-navigation-item js-navigation-open "
              href="/ckan/ckan/tree/ckan-2.4.4/ckan/config/routing.py"
              data-name="ckan-2.4.4"
              data-skip-pjax="true"
              rel="nofollow">
              <svg aria-hidden="true" class="octicon octicon-check select-menu-item-icon" height="16" version="1.1" viewBox="0 0 12 16" width="12"><path fill-rule="evenodd" d="M12 5l-8 8-4-4 1.5-1.5L4 10l6.5-6.5z"/></svg>
              <span class="select-menu-item-text css-truncate-target" title="ckan-2.4.4">
                ckan-2.4.4
              </span>
            </a>
            <a class="select-menu-item js-navigation-item js-navigation-open "
              href="/ckan/ckan/tree/ckan-2.4.3/ckan/config/routing.py"
              data-name="ckan-2.4.3"
              data-skip-pjax="true"
              rel="nofollow">
              <svg aria-hidden="true" class="octicon octicon-check select-menu-item-icon" height="16" version="1.1" viewBox="0 0 12 16" width="12"><path fill-rule="evenodd" d="M12 5l-8 8-4-4 1.5-1.5L4 10l6.5-6.5z"/></svg>
              <span class="select-menu-item-text css-truncate-target" title="ckan-2.4.3">
                ckan-2.4.3
              </span>
            </a>
            <a class="select-menu-item js-navigation-item js-navigation-open "
              href="/ckan/ckan/tree/ckan-2.4.2/ckan/config/routing.py"
              data-name="ckan-2.4.2"
              data-skip-pjax="true"
              rel="nofollow">
              <svg aria-hidden="true" class="octicon octicon-check select-menu-item-icon" height="16" version="1.1" viewBox="0 0 12 16" width="12"><path fill-rule="evenodd" d="M12 5l-8 8-4-4 1.5-1.5L4 10l6.5-6.5z"/></svg>
              <span class="select-menu-item-text css-truncate-target" title="ckan-2.4.2">
                ckan-2.4.2
              </span>
            </a>
            <a class="select-menu-item js-navigation-item js-navigation-open "
              href="/ckan/ckan/tree/ckan-2.4.1/ckan/config/routing.py"
              data-name="ckan-2.4.1"
              data-skip-pjax="true"
              rel="nofollow">
              <svg aria-hidden="true" class="octicon octicon-check select-menu-item-icon" height="16" version="1.1" viewBox="0 0 12 16" width="12"><path fill-rule="evenodd" d="M12 5l-8 8-4-4 1.5-1.5L4 10l6.5-6.5z"/></svg>
              <span class="select-menu-item-text css-truncate-target" title="ckan-2.4.1">
                ckan-2.4.1
              </span>
            </a>
            <a class="select-menu-item js-navigation-item js-navigation-open "
              href="/ckan/ckan/tree/ckan-2.4.0/ckan/config/routing.py"
              data-name="ckan-2.4.0"
              data-skip-pjax="true"
              rel="nofollow">
              <svg aria-hidden="true" class="octicon octicon-check select-menu-item-icon" height="16" version="1.1" viewBox="0 0 12 16" width="12"><path fill-rule="evenodd" d="M12 5l-8 8-4-4 1.5-1.5L4 10l6.5-6.5z"/></svg>
              <span class="select-menu-item-text css-truncate-target" title="ckan-2.4.0">
                ckan-2.4.0
              </span>
            </a>
            <a class="select-menu-item js-navigation-item js-navigation-open "
              href="/ckan/ckan/tree/ckan-2.3.5/ckan/config/routing.py"
              data-name="ckan-2.3.5"
              data-skip-pjax="true"
              rel="nofollow">
              <svg aria-hidden="true" class="octicon octicon-check select-menu-item-icon" height="16" version="1.1" viewBox="0 0 12 16" width="12"><path fill-rule="evenodd" d="M12 5l-8 8-4-4 1.5-1.5L4 10l6.5-6.5z"/></svg>
              <span class="select-menu-item-text css-truncate-target" title="ckan-2.3.5">
                ckan-2.3.5
              </span>
            </a>
            <a class="select-menu-item js-navigation-item js-navigation-open "
              href="/ckan/ckan/tree/ckan-2.3.4/ckan/config/routing.py"
              data-name="ckan-2.3.4"
              data-skip-pjax="true"
              rel="nofollow">
              <svg aria-hidden="true" class="octicon octicon-check select-menu-item-icon" height="16" version="1.1" viewBox="0 0 12 16" width="12"><path fill-rule="evenodd" d="M12 5l-8 8-4-4 1.5-1.5L4 10l6.5-6.5z"/></svg>
              <span class="select-menu-item-text css-truncate-target" title="ckan-2.3.4">
                ckan-2.3.4
              </span>
            </a>
            <a class="select-menu-item js-navigation-item js-navigation-open "
              href="/ckan/ckan/tree/ckan-2.3.3/ckan/config/routing.py"
              data-name="ckan-2.3.3"
              data-skip-pjax="true"
              rel="nofollow">
              <svg aria-hidden="true" class="octicon octicon-check select-menu-item-icon" height="16" version="1.1" viewBox="0 0 12 16" width="12"><path fill-rule="evenodd" d="M12 5l-8 8-4-4 1.5-1.5L4 10l6.5-6.5z"/></svg>
              <span class="select-menu-item-text css-truncate-target" title="ckan-2.3.3">
                ckan-2.3.3
              </span>
            </a>
            <a class="select-menu-item js-navigation-item js-navigation-open "
              href="/ckan/ckan/tree/ckan-2.3.2/ckan/config/routing.py"
              data-name="ckan-2.3.2"
              data-skip-pjax="true"
              rel="nofollow">
              <svg aria-hidden="true" class="octicon octicon-check select-menu-item-icon" height="16" version="1.1" viewBox="0 0 12 16" width="12"><path fill-rule="evenodd" d="M12 5l-8 8-4-4 1.5-1.5L4 10l6.5-6.5z"/></svg>
              <span class="select-menu-item-text css-truncate-target" title="ckan-2.3.2">
                ckan-2.3.2
              </span>
            </a>
            <a class="select-menu-item js-navigation-item js-navigation-open "
              href="/ckan/ckan/tree/ckan-2.3.1/ckan/config/routing.py"
              data-name="ckan-2.3.1"
              data-skip-pjax="true"
              rel="nofollow">
              <svg aria-hidden="true" class="octicon octicon-check select-menu-item-icon" height="16" version="1.1" viewBox="0 0 12 16" width="12"><path fill-rule="evenodd" d="M12 5l-8 8-4-4 1.5-1.5L4 10l6.5-6.5z"/></svg>
              <span class="select-menu-item-text css-truncate-target" title="ckan-2.3.1">
                ckan-2.3.1
              </span>
            </a>
            <a class="select-menu-item js-navigation-item js-navigation-open "
              href="/ckan/ckan/tree/ckan-2.3/ckan/config/routing.py"
              data-name="ckan-2.3"
              data-skip-pjax="true"
              rel="nofollow">
              <svg aria-hidden="true" class="octicon octicon-check select-menu-item-icon" height="16" version="1.1" viewBox="0 0 12 16" width="12"><path fill-rule="evenodd" d="M12 5l-8 8-4-4 1.5-1.5L4 10l6.5-6.5z"/></svg>
              <span class="select-menu-item-text css-truncate-target" title="ckan-2.3">
                ckan-2.3
              </span>
            </a>
            <a class="select-menu-item js-navigation-item js-navigation-open "
              href="/ckan/ckan/tree/ckan-2.2.4/ckan/config/routing.py"
              data-name="ckan-2.2.4"
              data-skip-pjax="true"
              rel="nofollow">
              <svg aria-hidden="true" class="octicon octicon-check select-menu-item-icon" height="16" version="1.1" viewBox="0 0 12 16" width="12"><path fill-rule="evenodd" d="M12 5l-8 8-4-4 1.5-1.5L4 10l6.5-6.5z"/></svg>
              <span class="select-menu-item-text css-truncate-target" title="ckan-2.2.4">
                ckan-2.2.4
              </span>
            </a>
            <a class="select-menu-item js-navigation-item js-navigation-open "
              href="/ckan/ckan/tree/ckan-2.2.3/ckan/config/routing.py"
              data-name="ckan-2.2.3"
              data-skip-pjax="true"
              rel="nofollow">
              <svg aria-hidden="true" class="octicon octicon-check select-menu-item-icon" height="16" version="1.1" viewBox="0 0 12 16" width="12"><path fill-rule="evenodd" d="M12 5l-8 8-4-4 1.5-1.5L4 10l6.5-6.5z"/></svg>
              <span class="select-menu-item-text css-truncate-target" title="ckan-2.2.3">
                ckan-2.2.3
              </span>
            </a>
            <a class="select-menu-item js-navigation-item js-navigation-open "
              href="/ckan/ckan/tree/ckan-2.2.2/ckan/config/routing.py"
              data-name="ckan-2.2.2"
              data-skip-pjax="true"
              rel="nofollow">
              <svg aria-hidden="true" class="octicon octicon-check select-menu-item-icon" height="16" version="1.1" viewBox="0 0 12 16" width="12"><path fill-rule="evenodd" d="M12 5l-8 8-4-4 1.5-1.5L4 10l6.5-6.5z"/></svg>
              <span class="select-menu-item-text css-truncate-target" title="ckan-2.2.2">
                ckan-2.2.2
              </span>
            </a>
            <a class="select-menu-item js-navigation-item js-navigation-open "
              href="/ckan/ckan/tree/ckan-2.2.1/ckan/config/routing.py"
              data-name="ckan-2.2.1"
              data-skip-pjax="true"
              rel="nofollow">
              <svg aria-hidden="true" class="octicon octicon-check select-menu-item-icon" height="16" version="1.1" viewBox="0 0 12 16" width="12"><path fill-rule="evenodd" d="M12 5l-8 8-4-4 1.5-1.5L4 10l6.5-6.5z"/></svg>
              <span class="select-menu-item-text css-truncate-target" title="ckan-2.2.1">
                ckan-2.2.1
              </span>
            </a>
            <a class="select-menu-item js-navigation-item js-navigation-open "
              href="/ckan/ckan/tree/ckan-2.2/ckan/config/routing.py"
              data-name="ckan-2.2"
              data-skip-pjax="true"
              rel="nofollow">
              <svg aria-hidden="true" class="octicon octicon-check select-menu-item-icon" height="16" version="1.1" viewBox="0 0 12 16" width="12"><path fill-rule="evenodd" d="M12 5l-8 8-4-4 1.5-1.5L4 10l6.5-6.5z"/></svg>
              <span class="select-menu-item-text css-truncate-target" title="ckan-2.2">
                ckan-2.2
              </span>
            </a>
            <a class="select-menu-item js-navigation-item js-navigation-open "
              href="/ckan/ckan/tree/ckan-2.1.6/ckan/config/routing.py"
              data-name="ckan-2.1.6"
              data-skip-pjax="true"
              rel="nofollow">
              <svg aria-hidden="true" class="octicon octicon-check select-menu-item-icon" height="16" version="1.1" viewBox="0 0 12 16" width="12"><path fill-rule="evenodd" d="M12 5l-8 8-4-4 1.5-1.5L4 10l6.5-6.5z"/></svg>
              <span class="select-menu-item-text css-truncate-target" title="ckan-2.1.6">
                ckan-2.1.6
              </span>
            </a>
            <a class="select-menu-item js-navigation-item js-navigation-open "
              href="/ckan/ckan/tree/ckan-2.1.5/ckan/config/routing.py"
              data-name="ckan-2.1.5"
              data-skip-pjax="true"
              rel="nofollow">
              <svg aria-hidden="true" class="octicon octicon-check select-menu-item-icon" height="16" version="1.1" viewBox="0 0 12 16" width="12"><path fill-rule="evenodd" d="M12 5l-8 8-4-4 1.5-1.5L4 10l6.5-6.5z"/></svg>
              <span class="select-menu-item-text css-truncate-target" title="ckan-2.1.5">
                ckan-2.1.5
              </span>
            </a>
            <a class="select-menu-item js-navigation-item js-navigation-open "
              href="/ckan/ckan/tree/ckan-2.1.4/ckan/config/routing.py"
              data-name="ckan-2.1.4"
              data-skip-pjax="true"
              rel="nofollow">
              <svg aria-hidden="true" class="octicon octicon-check select-menu-item-icon" height="16" version="1.1" viewBox="0 0 12 16" width="12"><path fill-rule="evenodd" d="M12 5l-8 8-4-4 1.5-1.5L4 10l6.5-6.5z"/></svg>
              <span class="select-menu-item-text css-truncate-target" title="ckan-2.1.4">
                ckan-2.1.4
              </span>
            </a>
            <a class="select-menu-item js-navigation-item js-navigation-open "
              href="/ckan/ckan/tree/ckan-2.1.3/ckan/config/routing.py"
              data-name="ckan-2.1.3"
              data-skip-pjax="true"
              rel="nofollow">
              <svg aria-hidden="true" class="octicon octicon-check select-menu-item-icon" height="16" version="1.1" viewBox="0 0 12 16" width="12"><path fill-rule="evenodd" d="M12 5l-8 8-4-4 1.5-1.5L4 10l6.5-6.5z"/></svg>
              <span class="select-menu-item-text css-truncate-target" title="ckan-2.1.3">
                ckan-2.1.3
              </span>
            </a>
            <a class="select-menu-item js-navigation-item js-navigation-open "
              href="/ckan/ckan/tree/ckan-2.1.2/ckan/config/routing.py"
              data-name="ckan-2.1.2"
              data-skip-pjax="true"
              rel="nofollow">
              <svg aria-hidden="true" class="octicon octicon-check select-menu-item-icon" height="16" version="1.1" viewBox="0 0 12 16" width="12"><path fill-rule="evenodd" d="M12 5l-8 8-4-4 1.5-1.5L4 10l6.5-6.5z"/></svg>
              <span class="select-menu-item-text css-truncate-target" title="ckan-2.1.2">
                ckan-2.1.2
              </span>
            </a>
            <a class="select-menu-item js-navigation-item js-navigation-open "
              href="/ckan/ckan/tree/ckan-2.1.1/ckan/config/routing.py"
              data-name="ckan-2.1.1"
              data-skip-pjax="true"
              rel="nofollow">
              <svg aria-hidden="true" class="octicon octicon-check select-menu-item-icon" height="16" version="1.1" viewBox="0 0 12 16" width="12"><path fill-rule="evenodd" d="M12 5l-8 8-4-4 1.5-1.5L4 10l6.5-6.5z"/></svg>
              <span class="select-menu-item-text css-truncate-target" title="ckan-2.1.1">
                ckan-2.1.1
              </span>
            </a>
            <a class="select-menu-item js-navigation-item js-navigation-open "
              href="/ckan/ckan/tree/ckan-2.1/ckan/config/routing.py"
              data-name="ckan-2.1"
              data-skip-pjax="true"
              rel="nofollow">
              <svg aria-hidden="true" class="octicon octicon-check select-menu-item-icon" height="16" version="1.1" viewBox="0 0 12 16" width="12"><path fill-rule="evenodd" d="M12 5l-8 8-4-4 1.5-1.5L4 10l6.5-6.5z"/></svg>
              <span class="select-menu-item-text css-truncate-target" title="ckan-2.1">
                ckan-2.1
              </span>
            </a>
            <a class="select-menu-item js-navigation-item js-navigation-open "
              href="/ckan/ckan/tree/ckan-2.0.8/ckan/config/routing.py"
              data-name="ckan-2.0.8"
              data-skip-pjax="true"
              rel="nofollow">
              <svg aria-hidden="true" class="octicon octicon-check select-menu-item-icon" height="16" version="1.1" viewBox="0 0 12 16" width="12"><path fill-rule="evenodd" d="M12 5l-8 8-4-4 1.5-1.5L4 10l6.5-6.5z"/></svg>
              <span class="select-menu-item-text css-truncate-target" title="ckan-2.0.8">
                ckan-2.0.8
              </span>
            </a>
            <a class="select-menu-item js-navigation-item js-navigation-open "
              href="/ckan/ckan/tree/ckan-2.0.7/ckan/config/routing.py"
              data-name="ckan-2.0.7"
              data-skip-pjax="true"
              rel="nofollow">
              <svg aria-hidden="true" class="octicon octicon-check select-menu-item-icon" height="16" version="1.1" viewBox="0 0 12 16" width="12"><path fill-rule="evenodd" d="M12 5l-8 8-4-4 1.5-1.5L4 10l6.5-6.5z"/></svg>
              <span class="select-menu-item-text css-truncate-target" title="ckan-2.0.7">
                ckan-2.0.7
              </span>
            </a>
            <a class="select-menu-item js-navigation-item js-navigation-open "
              href="/ckan/ckan/tree/ckan-2.0.6/ckan/config/routing.py"
              data-name="ckan-2.0.6"
              data-skip-pjax="true"
              rel="nofollow">
              <svg aria-hidden="true" class="octicon octicon-check select-menu-item-icon" height="16" version="1.1" viewBox="0 0 12 16" width="12"><path fill-rule="evenodd" d="M12 5l-8 8-4-4 1.5-1.5L4 10l6.5-6.5z"/></svg>
              <span class="select-menu-item-text css-truncate-target" title="ckan-2.0.6">
                ckan-2.0.6
              </span>
            </a>
            <a class="select-menu-item js-navigation-item js-navigation-open "
              href="/ckan/ckan/tree/ckan-2.0.5/ckan/config/routing.py"
              data-name="ckan-2.0.5"
              data-skip-pjax="true"
              rel="nofollow">
              <svg aria-hidden="true" class="octicon octicon-check select-menu-item-icon" height="16" version="1.1" viewBox="0 0 12 16" width="12"><path fill-rule="evenodd" d="M12 5l-8 8-4-4 1.5-1.5L4 10l6.5-6.5z"/></svg>
              <span class="select-menu-item-text css-truncate-target" title="ckan-2.0.5">
                ckan-2.0.5
              </span>
            </a>
            <a class="select-menu-item js-navigation-item js-navigation-open "
              href="/ckan/ckan/tree/ckan-2.0.4/ckan/config/routing.py"
              data-name="ckan-2.0.4"
              data-skip-pjax="true"
              rel="nofollow">
              <svg aria-hidden="true" class="octicon octicon-check select-menu-item-icon" height="16" version="1.1" viewBox="0 0 12 16" width="12"><path fill-rule="evenodd" d="M12 5l-8 8-4-4 1.5-1.5L4 10l6.5-6.5z"/></svg>
              <span class="select-menu-item-text css-truncate-target" title="ckan-2.0.4">
                ckan-2.0.4
              </span>
            </a>
            <a class="select-menu-item js-navigation-item js-navigation-open "
              href="/ckan/ckan/tree/ckan-2.0.3/ckan/config/routing.py"
              data-name="ckan-2.0.3"
              data-skip-pjax="true"
              rel="nofollow">
              <svg aria-hidden="true" class="octicon octicon-check select-menu-item-icon" height="16" version="1.1" viewBox="0 0 12 16" width="12"><path fill-rule="evenodd" d="M12 5l-8 8-4-4 1.5-1.5L4 10l6.5-6.5z"/></svg>
              <span class="select-menu-item-text css-truncate-target" title="ckan-2.0.3">
                ckan-2.0.3
              </span>
            </a>
            <a class="select-menu-item js-navigation-item js-navigation-open "
              href="/ckan/ckan/tree/ckan-2.0.2/ckan/config/routing.py"
              data-name="ckan-2.0.2"
              data-skip-pjax="true"
              rel="nofollow">
              <svg aria-hidden="true" class="octicon octicon-check select-menu-item-icon" height="16" version="1.1" viewBox="0 0 12 16" width="12"><path fill-rule="evenodd" d="M12 5l-8 8-4-4 1.5-1.5L4 10l6.5-6.5z"/></svg>
              <span class="select-menu-item-text css-truncate-target" title="ckan-2.0.2">
                ckan-2.0.2
              </span>
            </a>
            <a class="select-menu-item js-navigation-item js-navigation-open "
              href="/ckan/ckan/tree/ckan-2.0.1/ckan/config/routing.py"
              data-name="ckan-2.0.1"
              data-skip-pjax="true"
              rel="nofollow">
              <svg aria-hidden="true" class="octicon octicon-check select-menu-item-icon" height="16" version="1.1" viewBox="0 0 12 16" width="12"><path fill-rule="evenodd" d="M12 5l-8 8-4-4 1.5-1.5L4 10l6.5-6.5z"/></svg>
              <span class="select-menu-item-text css-truncate-target" title="ckan-2.0.1">
                ckan-2.0.1
              </span>
            </a>
            <a class="select-menu-item js-navigation-item js-navigation-open "
              href="/ckan/ckan/tree/ckan-2.0/ckan/config/routing.py"
              data-name="ckan-2.0"
              data-skip-pjax="true"
              rel="nofollow">
              <svg aria-hidden="true" class="octicon octicon-check select-menu-item-icon" height="16" version="1.1" viewBox="0 0 12 16" width="12"><path fill-rule="evenodd" d="M12 5l-8 8-4-4 1.5-1.5L4 10l6.5-6.5z"/></svg>
              <span class="select-menu-item-text css-truncate-target" title="ckan-2.0">
                ckan-2.0
              </span>
            </a>
            <a class="select-menu-item js-navigation-item js-navigation-open "
              href="/ckan/ckan/tree/ckan-1.8.2/ckan/config/routing.py"
              data-name="ckan-1.8.2"
              data-skip-pjax="true"
              rel="nofollow">
              <svg aria-hidden="true" class="octicon octicon-check select-menu-item-icon" height="16" version="1.1" viewBox="0 0 12 16" width="12"><path fill-rule="evenodd" d="M12 5l-8 8-4-4 1.5-1.5L4 10l6.5-6.5z"/></svg>
              <span class="select-menu-item-text css-truncate-target" title="ckan-1.8.2">
                ckan-1.8.2
              </span>
            </a>
            <a class="select-menu-item js-navigation-item js-navigation-open "
              href="/ckan/ckan/tree/ckan-1.8.1/ckan/config/routing.py"
              data-name="ckan-1.8.1"
              data-skip-pjax="true"
              rel="nofollow">
              <svg aria-hidden="true" class="octicon octicon-check select-menu-item-icon" height="16" version="1.1" viewBox="0 0 12 16" width="12"><path fill-rule="evenodd" d="M12 5l-8 8-4-4 1.5-1.5L4 10l6.5-6.5z"/></svg>
              <span class="select-menu-item-text css-truncate-target" title="ckan-1.8.1">
                ckan-1.8.1
              </span>
            </a>
            <a class="select-menu-item js-navigation-item js-navigation-open "
              href="/ckan/ckan/tree/ckan-1.8/ckan/config/routing.py"
              data-name="ckan-1.8"
              data-skip-pjax="true"
              rel="nofollow">
              <svg aria-hidden="true" class="octicon octicon-check select-menu-item-icon" height="16" version="1.1" viewBox="0 0 12 16" width="12"><path fill-rule="evenodd" d="M12 5l-8 8-4-4 1.5-1.5L4 10l6.5-6.5z"/></svg>
              <span class="select-menu-item-text css-truncate-target" title="ckan-1.8">
                ckan-1.8
              </span>
            </a>
            <a class="select-menu-item js-navigation-item js-navigation-open "
              href="/ckan/ckan/tree/ckan-1.7.4/ckan/config/routing.py"
              data-name="ckan-1.7.4"
              data-skip-pjax="true"
              rel="nofollow">
              <svg aria-hidden="true" class="octicon octicon-check select-menu-item-icon" height="16" version="1.1" viewBox="0 0 12 16" width="12"><path fill-rule="evenodd" d="M12 5l-8 8-4-4 1.5-1.5L4 10l6.5-6.5z"/></svg>
              <span class="select-menu-item-text css-truncate-target" title="ckan-1.7.4">
                ckan-1.7.4
              </span>
            </a>
            <a class="select-menu-item js-navigation-item js-navigation-open "
              href="/ckan/ckan/tree/ckan-1.7.3/ckan/config/routing.py"
              data-name="ckan-1.7.3"
              data-skip-pjax="true"
              rel="nofollow">
              <svg aria-hidden="true" class="octicon octicon-check select-menu-item-icon" height="16" version="1.1" viewBox="0 0 12 16" width="12"><path fill-rule="evenodd" d="M12 5l-8 8-4-4 1.5-1.5L4 10l6.5-6.5z"/></svg>
              <span class="select-menu-item-text css-truncate-target" title="ckan-1.7.3">
                ckan-1.7.3
              </span>
            </a>
            <a class="select-menu-item js-navigation-item js-navigation-open "
              href="/ckan/ckan/tree/ckan-1.7.2/ckan/config/routing.py"
              data-name="ckan-1.7.2"
              data-skip-pjax="true"
              rel="nofollow">
              <svg aria-hidden="true" class="octicon octicon-check select-menu-item-icon" height="16" version="1.1" viewBox="0 0 12 16" width="12"><path fill-rule="evenodd" d="M12 5l-8 8-4-4 1.5-1.5L4 10l6.5-6.5z"/></svg>
              <span class="select-menu-item-text css-truncate-target" title="ckan-1.7.2">
                ckan-1.7.2
              </span>
            </a>
            <a class="select-menu-item js-navigation-item js-navigation-open "
              href="/ckan/ckan/tree/ckan-1.7.1/ckan/config/routing.py"
              data-name="ckan-1.7.1"
              data-skip-pjax="true"
              rel="nofollow">
              <svg aria-hidden="true" class="octicon octicon-check select-menu-item-icon" height="16" version="1.1" viewBox="0 0 12 16" width="12"><path fill-rule="evenodd" d="M12 5l-8 8-4-4 1.5-1.5L4 10l6.5-6.5z"/></svg>
              <span class="select-menu-item-text css-truncate-target" title="ckan-1.7.1">
                ckan-1.7.1
              </span>
            </a>
            <a class="select-menu-item js-navigation-item js-navigation-open "
              href="/ckan/ckan/tree/ckan-1.7/ckan/config/routing.py"
              data-name="ckan-1.7"
              data-skip-pjax="true"
              rel="nofollow">
              <svg aria-hidden="true" class="octicon octicon-check select-menu-item-icon" height="16" version="1.1" viewBox="0 0 12 16" width="12"><path fill-rule="evenodd" d="M12 5l-8 8-4-4 1.5-1.5L4 10l6.5-6.5z"/></svg>
              <span class="select-menu-item-text css-truncate-target" title="ckan-1.7">
                ckan-1.7
              </span>
            </a>
            <a class="select-menu-item js-navigation-item js-navigation-open "
              href="/ckan/ckan/tree/ckan-1.6/ckan/config/routing.py"
              data-name="ckan-1.6"
              data-skip-pjax="true"
              rel="nofollow">
              <svg aria-hidden="true" class="octicon octicon-check select-menu-item-icon" height="16" version="1.1" viewBox="0 0 12 16" width="12"><path fill-rule="evenodd" d="M12 5l-8 8-4-4 1.5-1.5L4 10l6.5-6.5z"/></svg>
              <span class="select-menu-item-text css-truncate-target" title="ckan-1.6">
                ckan-1.6
              </span>
            </a>
            <a class="select-menu-item js-navigation-item js-navigation-open "
              href="/ckan/ckan/tree/ckan-1.5.1/ckan/config/routing.py"
              data-name="ckan-1.5.1"
              data-skip-pjax="true"
              rel="nofollow">
              <svg aria-hidden="true" class="octicon octicon-check select-menu-item-icon" height="16" version="1.1" viewBox="0 0 12 16" width="12"><path fill-rule="evenodd" d="M12 5l-8 8-4-4 1.5-1.5L4 10l6.5-6.5z"/></svg>
              <span class="select-menu-item-text css-truncate-target" title="ckan-1.5.1">
                ckan-1.5.1
              </span>
            </a>
            <a class="select-menu-item js-navigation-item js-navigation-open "
              href="/ckan/ckan/tree/ckan-1.5/ckan/config/routing.py"
              data-name="ckan-1.5"
              data-skip-pjax="true"
              rel="nofollow">
              <svg aria-hidden="true" class="octicon octicon-check select-menu-item-icon" height="16" version="1.1" viewBox="0 0 12 16" width="12"><path fill-rule="evenodd" d="M12 5l-8 8-4-4 1.5-1.5L4 10l6.5-6.5z"/></svg>
              <span class="select-menu-item-text css-truncate-target" title="ckan-1.5">
                ckan-1.5
              </span>
            </a>
            <a class="select-menu-item js-navigation-item js-navigation-open "
              href="/ckan/ckan/tree/ckan-1.4.3/ckan/config/routing.py"
              data-name="ckan-1.4.3"
              data-skip-pjax="true"
              rel="nofollow">
              <svg aria-hidden="true" class="octicon octicon-check select-menu-item-icon" height="16" version="1.1" viewBox="0 0 12 16" width="12"><path fill-rule="evenodd" d="M12 5l-8 8-4-4 1.5-1.5L4 10l6.5-6.5z"/></svg>
              <span class="select-menu-item-text css-truncate-target" title="ckan-1.4.3">
                ckan-1.4.3
              </span>
            </a>
            <a class="select-menu-item js-navigation-item js-navigation-open "
              href="/ckan/ckan/tree/ckan-1.4.2/ckan/config/routing.py"
              data-name="ckan-1.4.2"
              data-skip-pjax="true"
              rel="nofollow">
              <svg aria-hidden="true" class="octicon octicon-check select-menu-item-icon" height="16" version="1.1" viewBox="0 0 12 16" width="12"><path fill-rule="evenodd" d="M12 5l-8 8-4-4 1.5-1.5L4 10l6.5-6.5z"/></svg>
              <span class="select-menu-item-text css-truncate-target" title="ckan-1.4.2">
                ckan-1.4.2
              </span>
            </a>
            <a class="select-menu-item js-navigation-item js-navigation-open "
              href="/ckan/ckan/tree/ckan-1.4.1/ckan/config/routing.py"
              data-name="ckan-1.4.1"
              data-skip-pjax="true"
              rel="nofollow">
              <svg aria-hidden="true" class="octicon octicon-check select-menu-item-icon" height="16" version="1.1" viewBox="0 0 12 16" width="12"><path fill-rule="evenodd" d="M12 5l-8 8-4-4 1.5-1.5L4 10l6.5-6.5z"/></svg>
              <span class="select-menu-item-text css-truncate-target" title="ckan-1.4.1">
                ckan-1.4.1
              </span>
            </a>
            <a class="select-menu-item js-navigation-item js-navigation-open "
              href="/ckan/ckan/tree/ckan-1.4/ckan/config/routing.py"
              data-name="ckan-1.4"
              data-skip-pjax="true"
              rel="nofollow">
              <svg aria-hidden="true" class="octicon octicon-check select-menu-item-icon" height="16" version="1.1" viewBox="0 0 12 16" width="12"><path fill-rule="evenodd" d="M12 5l-8 8-4-4 1.5-1.5L4 10l6.5-6.5z"/></svg>
              <span class="select-menu-item-text css-truncate-target" title="ckan-1.4">
                ckan-1.4
              </span>
            </a>
            <a class="select-menu-item js-navigation-item js-navigation-open "
              href="/ckan/ckan/tree/ckan-1.3.3b/ckan/config/routing.py"
              data-name="ckan-1.3.3b"
              data-skip-pjax="true"
              rel="nofollow">
              <svg aria-hidden="true" class="octicon octicon-check select-menu-item-icon" height="16" version="1.1" viewBox="0 0 12 16" width="12"><path fill-rule="evenodd" d="M12 5l-8 8-4-4 1.5-1.5L4 10l6.5-6.5z"/></svg>
              <span class="select-menu-item-text css-truncate-target" title="ckan-1.3.3b">
                ckan-1.3.3b
              </span>
            </a>
        </div>

        <div class="select-menu-no-results">Nothing to show</div>
      </div>

    </div>
  </div>
</div>

    <div class="BtnGroup float-right">
      <a href="/ckan/ckan/find/master"
            class="js-pjax-capture-input btn btn-sm BtnGroup-item"
            data-pjax
            data-hotkey="t">
        Find file
      </a>
      <button aria-label="Copy file path to clipboard" class="js-zeroclipboard btn btn-sm BtnGroup-item tooltipped tooltipped-s" data-copied-hint="Copied!" type="button">Copy path</button>
    </div>
    <div class="breadcrumb js-zeroclipboard-target">
      <span class="repo-root js-repo-root"><span class="js-path-segment"><a href="/ckan/ckan"><span>ckan</span></a></span></span><span class="separator">/</span><span class="js-path-segment"><a href="/ckan/ckan/tree/master/ckan"><span>ckan</span></a></span><span class="separator">/</span><span class="js-path-segment"><a href="/ckan/ckan/tree/master/ckan/config"><span>config</span></a></span><span class="separator">/</span><strong class="final-path">routing.py</strong>
    </div>
  </div>


  
  <div class="commit-tease">
      <span class="float-right">
        <a class="commit-tease-sha" href="/ckan/ckan/commit/97bbcdc5f94a6cdd7adeeb8821e6ef19cd4f88d8" data-pjax>
          97bbcdc
        </a>
        <relative-time datetime="2017-08-31T12:22:52Z">Aug 31, 2017</relative-time>
      </span>
      <div>
        <img alt="@amercader" class="avatar" height="20" src="https://avatars3.githubusercontent.com/u/200230?v=4&amp;s=40" width="20" />
        <a href="/amercader" class="user-mention" rel="contributor">amercader</a>
          <a href="/ckan/ckan/commit/97bbcdc5f94a6cdd7adeeb8821e6ef19cd4f88d8" class="message" data-pjax="true" title="Merge branch &#39;master&#39; into 3229-api-blueprint">Merge branch 'master' into 3229-api-blueprint</a>
      </div>

    <div class="commit-tease-contributors">
      <button type="button" class="btn-link muted-link contributors-toggle" data-facebox="#blob_contributors_box">
        <strong>40</strong>
         contributors
      </button>
          <a class="avatar-link tooltipped tooltipped-s" aria-label="tobes" href="/ckan/ckan/commits/master/ckan/config/routing.py?author=tobes"><img alt="@tobes" class="avatar" height="20" src="https://avatars0.githubusercontent.com/u/56311?v=4&amp;s=40" width="20" /> </a>
    <a class="avatar-link tooltipped tooltipped-s" aria-label="rossjones" href="/ckan/ckan/commits/master/ckan/config/routing.py?author=rossjones"><img alt="@rossjones" class="avatar" height="20" src="https://avatars3.githubusercontent.com/u/118063?v=4&amp;s=40" width="20" /> </a>
    <a class="avatar-link tooltipped tooltipped-s" aria-label="rufuspollock" href="/ckan/ckan/commits/master/ckan/config/routing.py?author=rufuspollock"><img alt="@rufuspollock" class="avatar" height="20" src="https://avatars0.githubusercontent.com/u/180658?v=4&amp;s=40" width="20" /> </a>
    <a class="avatar-link tooltipped tooltipped-s" aria-label="johnmartin" href="/ckan/ckan/commits/master/ckan/config/routing.py?author=johnmartin"><img alt="@johnmartin" class="avatar" height="20" src="https://avatars0.githubusercontent.com/u/67366?v=4&amp;s=40" width="20" /> </a>
    <a class="avatar-link tooltipped tooltipped-s" aria-label="kindly" href="/ckan/ckan/commits/master/ckan/config/routing.py?author=kindly"><img alt="@kindly" class="avatar" height="20" src="https://avatars3.githubusercontent.com/u/30636?v=4&amp;s=40" width="20" /> </a>
    <a class="avatar-link tooltipped tooltipped-s" aria-label="amercader" href="/ckan/ckan/commits/master/ckan/config/routing.py?author=amercader"><img alt="@amercader" class="avatar" height="20" src="https://avatars3.githubusercontent.com/u/200230?v=4&amp;s=40" width="20" /> </a>
    <a class="avatar-link tooltipped tooltipped-s" aria-label="johnbywater" href="/ckan/ckan/commits/master/ckan/config/routing.py?author=johnbywater"><img alt="@johnbywater" class="avatar" height="20" src="https://avatars0.githubusercontent.com/u/3607503?v=4&amp;s=40" width="20" /> </a>
    <a class="avatar-link tooltipped tooltipped-s" aria-label="pudo" href="/ckan/ckan/commits/master/ckan/config/routing.py?author=pudo"><img alt="@pudo" class="avatar" height="20" src="https://avatars1.githubusercontent.com/u/41628?v=4&amp;s=40" width="20" /> </a>
    <a class="avatar-link tooltipped tooltipped-s" aria-label="zephod" href="/ckan/ckan/commits/master/ckan/config/routing.py?author=zephod"><img alt="@zephod" class="avatar" height="20" src="https://avatars1.githubusercontent.com/u/92938?v=4&amp;s=40" width="20" /> </a>
    <a class="avatar-link tooltipped tooltipped-s" aria-label="icmurray" href="/ckan/ckan/commits/master/ckan/config/routing.py?author=icmurray"><img alt="@icmurray" class="avatar" height="20" src="https://avatars0.githubusercontent.com/u/280463?v=4&amp;s=40" width="20" /> </a>
    <a class="avatar-link tooltipped tooltipped-s" aria-label="domoritz" href="/ckan/ckan/commits/master/ckan/config/routing.py?author=domoritz"><img alt="@domoritz" class="avatar" height="20" src="https://avatars2.githubusercontent.com/u/589034?v=4&amp;s=40" width="20" /> </a>
    <a class="avatar-link tooltipped tooltipped-s" aria-label="johnglover" href="/ckan/ckan/commits/master/ckan/config/routing.py?author=johnglover"><img alt="@johnglover" class="avatar" height="20" src="https://avatars2.githubusercontent.com/u/343435?v=4&amp;s=40" width="20" /> </a>
    <a class="avatar-link tooltipped tooltipped-s" aria-label="aron" href="/ckan/ckan/commits/master/ckan/config/routing.py?author=aron"><img alt="@aron" class="avatar" height="20" src="https://avatars2.githubusercontent.com/u/47144?v=4&amp;s=40" width="20" /> </a>
    <a class="avatar-link tooltipped tooltipped-s" aria-label="ollyc" href="/ckan/ckan/commits/master/ckan/config/routing.py?author=ollyc"><img alt="@ollyc" class="avatar" height="20" src="https://avatars3.githubusercontent.com/u/111527?v=4&amp;s=40" width="20" /> </a>
    <a class="avatar-link tooltipped tooltipped-s" aria-label="vitorbaptista" href="/ckan/ckan/commits/master/ckan/config/routing.py?author=vitorbaptista"><img alt="@vitorbaptista" class="avatar" height="20" src="https://avatars0.githubusercontent.com/u/76945?v=4&amp;s=40" width="20" /> </a>
    <a class="avatar-link tooltipped tooltipped-s" aria-label="brew" href="/ckan/ckan/commits/master/ckan/config/routing.py?author=brew"><img alt="@brew" class="avatar" height="20" src="https://avatars2.githubusercontent.com/u/3993?v=4&amp;s=40" width="20" /> </a>
    <a class="avatar-link tooltipped tooltipped-s" aria-label="smotornyuk" href="/ckan/ckan/commits/master/ckan/config/routing.py?author=smotornyuk"><img alt="@smotornyuk" class="avatar" height="20" src="https://avatars1.githubusercontent.com/u/11091199?v=4&amp;s=40" width="20" /> </a>
    <a class="avatar-link tooltipped tooltipped-s" aria-label="torfsen" href="/ckan/ckan/commits/master/ckan/config/routing.py?author=torfsen"><img alt="@torfsen" class="avatar" height="20" src="https://avatars1.githubusercontent.com/u/2877717?v=4&amp;s=40" width="20" /> </a>
    <a class="avatar-link tooltipped tooltipped-s" aria-label="fanjinfei" href="/ckan/ckan/commits/master/ckan/config/routing.py?author=fanjinfei"><img alt="@fanjinfei" class="avatar" height="20" src="https://avatars3.githubusercontent.com/u/4493004?v=4&amp;s=40" width="20" /> </a>
    <a class="avatar-link tooltipped tooltipped-s" aria-label="davidread" href="/ckan/ckan/commits/master/ckan/config/routing.py?author=davidread"><img alt="@davidread" class="avatar" height="20" src="https://avatars0.githubusercontent.com/u/307612?v=4&amp;s=40" width="20" /> </a>
    <a class="avatar-link tooltipped tooltipped-s" aria-label="TkTech" href="/ckan/ckan/commits/master/ckan/config/routing.py?author=TkTech"><img alt="@TkTech" class="avatar" height="20" src="https://avatars0.githubusercontent.com/u/72590?v=4&amp;s=40" width="20" /> </a>
    <a class="avatar-link tooltipped tooltipped-s" aria-label="nigelbabu" href="/ckan/ckan/commits/master/ckan/config/routing.py?author=nigelbabu"><img alt="@nigelbabu" class="avatar" height="20" src="https://avatars1.githubusercontent.com/u/373438?v=4&amp;s=40" width="20" /> </a>
    <a class="avatar-link tooltipped tooltipped-s" aria-label="nickstenning" href="/ckan/ckan/commits/master/ckan/config/routing.py?author=nickstenning"><img alt="@nickstenning" class="avatar" height="20" src="https://avatars0.githubusercontent.com/u/3602?v=4&amp;s=40" width="20" /> </a>
    <a class="avatar-link tooltipped tooltipped-s" aria-label="mwahlroos" href="/ckan/ckan/commits/master/ckan/config/routing.py?author=mwahlroos"><img alt="@mwahlroos" class="avatar" height="20" src="https://avatars3.githubusercontent.com/u/5259586?v=4&amp;s=40" width="20" /> </a>
    <a class="avatar-link tooltipped tooltipped-s" aria-label="mvi-eea-sk" href="/ckan/ckan/commits/master/ckan/config/routing.py?author=mvi-eea-sk"><img alt="@mvi-eea-sk" class="avatar" height="20" src="https://avatars2.githubusercontent.com/u/8155157?v=4&amp;s=40" width="20" /> </a>
    <a class="avatar-link tooltipped tooltipped-s" aria-label="Khalegh-H3" href="/ckan/ckan/commits/master/ckan/config/routing.py?author=Khalegh-H3"><img alt="@Khalegh-H3" class="avatar" height="20" src="https://avatars0.githubusercontent.com/u/6463284?v=4&amp;s=40" width="20" /> </a>

    <button type="button" data-facebox="#blob_contributors_box" class="btn-link others-text">and others</button>

    </div>

    <div id="blob_contributors_box" style="display:none">
      <h2 class="facebox-header" data-facebox-id="facebox-header">Users who have contributed to this file</h2>
      <ul class="facebox-user-list" data-facebox-id="facebox-description">
          <li class="facebox-user-list-item">
            <img alt="@tobes" height="24" src="https://avatars2.githubusercontent.com/u/56311?v=4&amp;s=48" width="24" />
            <a href="/tobes">tobes</a>
          </li>
          <li class="facebox-user-list-item">
            <img alt="@rossjones" height="24" src="https://avatars1.githubusercontent.com/u/118063?v=4&amp;s=48" width="24" />
            <a href="/rossjones">rossjones</a>
          </li>
          <li class="facebox-user-list-item">
            <img alt="@rufuspollock" height="24" src="https://avatars2.githubusercontent.com/u/180658?v=4&amp;s=48" width="24" />
            <a href="/rufuspollock">rufuspollock</a>
          </li>
          <li class="facebox-user-list-item">
            <img alt="@johnmartin" height="24" src="https://avatars2.githubusercontent.com/u/67366?v=4&amp;s=48" width="24" />
            <a href="/johnmartin">johnmartin</a>
          </li>
          <li class="facebox-user-list-item">
            <img alt="@kindly" height="24" src="https://avatars1.githubusercontent.com/u/30636?v=4&amp;s=48" width="24" />
            <a href="/kindly">kindly</a>
          </li>
          <li class="facebox-user-list-item">
            <img alt="@amercader" height="24" src="https://avatars1.githubusercontent.com/u/200230?v=4&amp;s=48" width="24" />
            <a href="/amercader">amercader</a>
          </li>
          <li class="facebox-user-list-item">
            <img alt="@johnbywater" height="24" src="https://avatars2.githubusercontent.com/u/3607503?v=4&amp;s=48" width="24" />
            <a href="/johnbywater">johnbywater</a>
          </li>
          <li class="facebox-user-list-item">
            <img alt="@pudo" height="24" src="https://avatars3.githubusercontent.com/u/41628?v=4&amp;s=48" width="24" />
            <a href="/pudo">pudo</a>
          </li>
          <li class="facebox-user-list-item">
            <img alt="@zephod" height="24" src="https://avatars3.githubusercontent.com/u/92938?v=4&amp;s=48" width="24" />
            <a href="/zephod">zephod</a>
          </li>
          <li class="facebox-user-list-item">
            <img alt="@icmurray" height="24" src="https://avatars2.githubusercontent.com/u/280463?v=4&amp;s=48" width="24" />
            <a href="/icmurray">icmurray</a>
          </li>
          <li class="facebox-user-list-item">
            <img alt="@domoritz" height="24" src="https://avatars0.githubusercontent.com/u/589034?v=4&amp;s=48" width="24" />
            <a href="/domoritz">domoritz</a>
          </li>
          <li class="facebox-user-list-item">
            <img alt="@johnglover" height="24" src="https://avatars0.githubusercontent.com/u/343435?v=4&amp;s=48" width="24" />
            <a href="/johnglover">johnglover</a>
          </li>
          <li class="facebox-user-list-item">
            <img alt="@aron" height="24" src="https://avatars0.githubusercontent.com/u/47144?v=4&amp;s=48" width="24" />
            <a href="/aron">aron</a>
          </li>
          <li class="facebox-user-list-item">
            <img alt="@ollyc" height="24" src="https://avatars1.githubusercontent.com/u/111527?v=4&amp;s=48" width="24" />
            <a href="/ollyc">ollyc</a>
          </li>
          <li class="facebox-user-list-item">
            <img alt="@vitorbaptista" height="24" src="https://avatars2.githubusercontent.com/u/76945?v=4&amp;s=48" width="24" />
            <a href="/vitorbaptista">vitorbaptista</a>
          </li>
          <li class="facebox-user-list-item">
            <img alt="@brew" height="24" src="https://avatars0.githubusercontent.com/u/3993?v=4&amp;s=48" width="24" />
            <a href="/brew">brew</a>
          </li>
          <li class="facebox-user-list-item">
            <img alt="@smotornyuk" height="24" src="https://avatars3.githubusercontent.com/u/11091199?v=4&amp;s=48" width="24" />
            <a href="/smotornyuk">smotornyuk</a>
          </li>
          <li class="facebox-user-list-item">
            <img alt="@torfsen" height="24" src="https://avatars3.githubusercontent.com/u/2877717?v=4&amp;s=48" width="24" />
            <a href="/torfsen">torfsen</a>
          </li>
          <li class="facebox-user-list-item">
            <img alt="@fanjinfei" height="24" src="https://avatars1.githubusercontent.com/u/4493004?v=4&amp;s=48" width="24" />
            <a href="/fanjinfei">fanjinfei</a>
          </li>
          <li class="facebox-user-list-item">
            <img alt="@davidread" height="24" src="https://avatars2.githubusercontent.com/u/307612?v=4&amp;s=48" width="24" />
            <a href="/davidread">davidread</a>
          </li>
          <li class="facebox-user-list-item">
            <img alt="@TkTech" height="24" src="https://avatars2.githubusercontent.com/u/72590?v=4&amp;s=48" width="24" />
            <a href="/TkTech">TkTech</a>
          </li>
          <li class="facebox-user-list-item">
            <img alt="@nigelbabu" height="24" src="https://avatars3.githubusercontent.com/u/373438?v=4&amp;s=48" width="24" />
            <a href="/nigelbabu">nigelbabu</a>
          </li>
          <li class="facebox-user-list-item">
            <img alt="@nickstenning" height="24" src="https://avatars2.githubusercontent.com/u/3602?v=4&amp;s=48" width="24" />
            <a href="/nickstenning">nickstenning</a>
          </li>
          <li class="facebox-user-list-item">
            <img alt="@mwahlroos" height="24" src="https://avatars1.githubusercontent.com/u/5259586?v=4&amp;s=48" width="24" />
            <a href="/mwahlroos">mwahlroos</a>
          </li>
          <li class="facebox-user-list-item">
            <img alt="@mvi-eea-sk" height="24" src="https://avatars0.githubusercontent.com/u/8155157?v=4&amp;s=48" width="24" />
            <a href="/mvi-eea-sk">mvi-eea-sk</a>
          </li>
          <li class="facebox-user-list-item">
            <img alt="@Khalegh-H3" height="24" src="https://avatars2.githubusercontent.com/u/6463284?v=4&amp;s=48" width="24" />
            <a href="/Khalegh-H3">Khalegh-H3</a>
          </li>
          <li class="facebox-user-list-item">
            <img alt="@joetsoi" height="24" src="https://avatars3.githubusercontent.com/u/241130?v=4&amp;s=48" width="24" />
            <a href="/joetsoi">joetsoi</a>
          </li>
          <li class="facebox-user-list-item">
            <img alt="@jbspeakr" height="24" src="https://avatars0.githubusercontent.com/u/2291138?v=4&amp;s=48" width="24" />
            <a href="/jbspeakr">jbspeakr</a>
          </li>
      </ul>
    </div>
  </div>


  <div class="file">
    <div class="file-header">
  <div class="file-actions">

    <div class="BtnGroup">
      <a href="/ckan/ckan/raw/master/ckan/config/routing.py" class="btn btn-sm BtnGroup-item" id="raw-url">Raw</a>
        <a href="/ckan/ckan/blame/master/ckan/config/routing.py" class="btn btn-sm js-update-url-with-hash BtnGroup-item" data-hotkey="b">Blame</a>
      <a href="/ckan/ckan/commits/master/ckan/config/routing.py" class="btn btn-sm BtnGroup-item" rel="nofollow">History</a>
    </div>

        <a class="btn-octicon tooltipped tooltipped-nw"
           href="https://desktop.github.com"
           aria-label="Open this file in GitHub Desktop"
           data-ga-click="Repository, open with desktop, type:windows">
            <svg aria-hidden="true" class="octicon octicon-device-desktop" height="16" version="1.1" viewBox="0 0 16 16" width="16"><path fill-rule="evenodd" d="M15 2H1c-.55 0-1 .45-1 1v9c0 .55.45 1 1 1h5.34c-.25.61-.86 1.39-2.34 2h8c-1.48-.61-2.09-1.39-2.34-2H15c.55 0 1-.45 1-1V3c0-.55-.45-1-1-1zm0 9H1V3h14v8z"/></svg>
        </a>

        <!-- '"` --><!-- </textarea></xmp> --></option></form><form accept-charset="UTF-8" action="/ckan/ckan/edit/master/ckan/config/routing.py" class="inline-form js-update-url-with-hash" method="post"><div style="margin:0;padding:0;display:inline"><input name="utf8" type="hidden" value="&#x2713;" /><input name="authenticity_token" type="hidden" value="yA1qT1fv+V/XWlIhId9zwdJ8rSd2UsfYzwI4f6FZZx04hlHowqNfjPXWywyc3zzDc9UKqklERTleD18S+WTeaQ==" /></div>
          <button class="btn-octicon tooltipped tooltipped-nw" type="submit"
            aria-label="Edit the file in your fork of this project" data-hotkey="e" data-disable-with>
            <svg aria-hidden="true" class="octicon octicon-pencil" height="16" version="1.1" viewBox="0 0 14 16" width="14"><path fill-rule="evenodd" d="M0 12v3h3l8-8-3-3-8 8zm3 2H1v-2h1v1h1v1zm10.3-9.3L12 6 9 3l1.3-1.3a.996.996 0 0 1 1.41 0l1.59 1.59c.39.39.39 1.02 0 1.41z"/></svg>
          </button>
</form>        <!-- '"` --><!-- </textarea></xmp> --></option></form><form accept-charset="UTF-8" action="/ckan/ckan/delete/master/ckan/config/routing.py" class="inline-form" method="post"><div style="margin:0;padding:0;display:inline"><input name="utf8" type="hidden" value="&#x2713;" /><input name="authenticity_token" type="hidden" value="HV8vIS2TYWxZ8vPrpk4B+p0dV3q1jH3v1WPjusY1+71Qqa8U5QOZEF/4AoUtSBkTXqPXk8uSdRtIHaZipaxSHQ==" /></div>
          <button class="btn-octicon btn-octicon-danger tooltipped tooltipped-nw" type="submit"
            aria-label="Delete the file in your fork of this project" data-disable-with>
            <svg aria-hidden="true" class="octicon octicon-trashcan" height="16" version="1.1" viewBox="0 0 12 16" width="12"><path fill-rule="evenodd" d="M11 2H9c0-.55-.45-1-1-1H5c-.55 0-1 .45-1 1H2c-.55 0-1 .45-1 1v1c0 .55.45 1 1 1v9c0 .55.45 1 1 1h7c.55 0 1-.45 1-1V5c.55 0 1-.45 1-1V3c0-.55-.45-1-1-1zm-1 12H3V5h1v8h1V5h1v8h1V5h1v8h1V5h1v9zm1-10H2V3h9v1z"/></svg>
          </button>
</form>  </div>

  <div class="file-info">
      426 lines (375 sloc)
      <span class="file-info-divider"></span>
    18.3 KB
  </div>
</div>

    

  <div itemprop="text" class="blob-wrapper data type-python">
      <table class="highlight tab-size js-file-line-container" data-tab-size="4">
      <tr>
        <td id="L1" class="blob-num js-line-number" data-line-number="1"></td>
        <td id="LC1" class="blob-code blob-code-inner js-file-line"><span class="pl-c"><span class="pl-c">#</span> encoding: utf-8</span></td>
      </tr>
      <tr>
        <td id="L2" class="blob-num js-line-number" data-line-number="2"></td>
        <td id="LC2" class="blob-code blob-code-inner js-file-line">
</td>
      </tr>
      <tr>
        <td id="L3" class="blob-num js-line-number" data-line-number="3"></td>
        <td id="LC3" class="blob-code blob-code-inner js-file-line"><span class="pl-s"><span class="pl-pds">&quot;&quot;&quot;</span>Routes configuration</span></td>
      </tr>
      <tr>
        <td id="L4" class="blob-num js-line-number" data-line-number="4"></td>
        <td id="LC4" class="blob-code blob-code-inner js-file-line"><span class="pl-s"></span></td>
      </tr>
      <tr>
        <td id="L5" class="blob-num js-line-number" data-line-number="5"></td>
        <td id="LC5" class="blob-code blob-code-inner js-file-line"><span class="pl-s">The more specific and detailed routes should be defined first so they</span></td>
      </tr>
      <tr>
        <td id="L6" class="blob-num js-line-number" data-line-number="6"></td>
        <td id="LC6" class="blob-code blob-code-inner js-file-line"><span class="pl-s">may take precedent over the more generic routes. For more information</span></td>
      </tr>
      <tr>
        <td id="L7" class="blob-num js-line-number" data-line-number="7"></td>
        <td id="LC7" class="blob-code blob-code-inner js-file-line"><span class="pl-s">refer to the routes manual at http://routes.groovie.org/docs/</span></td>
      </tr>
      <tr>
        <td id="L8" class="blob-num js-line-number" data-line-number="8"></td>
        <td id="LC8" class="blob-code blob-code-inner js-file-line"><span class="pl-s"></span></td>
      </tr>
      <tr>
        <td id="L9" class="blob-num js-line-number" data-line-number="9"></td>
        <td id="LC9" class="blob-code blob-code-inner js-file-line"><span class="pl-s"><span class="pl-pds">&quot;&quot;&quot;</span></span></td>
      </tr>
      <tr>
        <td id="L10" class="blob-num js-line-number" data-line-number="10"></td>
        <td id="LC10" class="blob-code blob-code-inner js-file-line"><span class="pl-k">import</span> re</td>
      </tr>
      <tr>
        <td id="L11" class="blob-num js-line-number" data-line-number="11"></td>
        <td id="LC11" class="blob-code blob-code-inner js-file-line">
</td>
      </tr>
      <tr>
        <td id="L12" class="blob-num js-line-number" data-line-number="12"></td>
        <td id="LC12" class="blob-code blob-code-inner js-file-line"><span class="pl-k">from</span> routes.mapper <span class="pl-k">import</span> SubMapper, Mapper <span class="pl-k">as</span> _Mapper</td>
      </tr>
      <tr>
        <td id="L13" class="blob-num js-line-number" data-line-number="13"></td>
        <td id="LC13" class="blob-code blob-code-inner js-file-line">
</td>
      </tr>
      <tr>
        <td id="L14" class="blob-num js-line-number" data-line-number="14"></td>
        <td id="LC14" class="blob-code blob-code-inner js-file-line"><span class="pl-k">import</span> ckan.plugins <span class="pl-k">as</span> p</td>
      </tr>
      <tr>
        <td id="L15" class="blob-num js-line-number" data-line-number="15"></td>
        <td id="LC15" class="blob-code blob-code-inner js-file-line"><span class="pl-k">from</span> ckan.common <span class="pl-k">import</span> config</td>
      </tr>
      <tr>
        <td id="L16" class="blob-num js-line-number" data-line-number="16"></td>
        <td id="LC16" class="blob-code blob-code-inner js-file-line">
</td>
      </tr>
      <tr>
        <td id="L17" class="blob-num js-line-number" data-line-number="17"></td>
        <td id="LC17" class="blob-code blob-code-inner js-file-line">named_routes <span class="pl-k">=</span> {}</td>
      </tr>
      <tr>
        <td id="L18" class="blob-num js-line-number" data-line-number="18"></td>
        <td id="LC18" class="blob-code blob-code-inner js-file-line">
</td>
      </tr>
      <tr>
        <td id="L19" class="blob-num js-line-number" data-line-number="19"></td>
        <td id="LC19" class="blob-code blob-code-inner js-file-line">
</td>
      </tr>
      <tr>
        <td id="L20" class="blob-num js-line-number" data-line-number="20"></td>
        <td id="LC20" class="blob-code blob-code-inner js-file-line"><span class="pl-k">class</span> <span class="pl-en">Mapper</span>(<span class="pl-e">_Mapper</span>):</td>
      </tr>
      <tr>
        <td id="L21" class="blob-num js-line-number" data-line-number="21"></td>
        <td id="LC21" class="blob-code blob-code-inner js-file-line">    <span class="pl-s"><span class="pl-pds">&#39;&#39;&#39;</span> This Mapper allows us to intercept the connect calls used by routes</span></td>
      </tr>
      <tr>
        <td id="L22" class="blob-num js-line-number" data-line-number="22"></td>
        <td id="LC22" class="blob-code blob-code-inner js-file-line"><span class="pl-s">    so that we can collect named routes and later use them to create links</span></td>
      </tr>
      <tr>
        <td id="L23" class="blob-num js-line-number" data-line-number="23"></td>
        <td id="LC23" class="blob-code blob-code-inner js-file-line"><span class="pl-s">    via some helper functions like build_nav(). <span class="pl-pds">&#39;&#39;&#39;</span></span></td>
      </tr>
      <tr>
        <td id="L24" class="blob-num js-line-number" data-line-number="24"></td>
        <td id="LC24" class="blob-code blob-code-inner js-file-line">
</td>
      </tr>
      <tr>
        <td id="L25" class="blob-num js-line-number" data-line-number="25"></td>
        <td id="LC25" class="blob-code blob-code-inner js-file-line">    <span class="pl-k">def</span> <span class="pl-en">connect</span>(<span class="pl-smi"><span class="pl-smi">self</span></span>, <span class="pl-k">*</span><span class="pl-smi">args</span>, <span class="pl-k">**</span><span class="pl-smi">kw</span>):</td>
      </tr>
      <tr>
        <td id="L26" class="blob-num js-line-number" data-line-number="26"></td>
        <td id="LC26" class="blob-code blob-code-inner js-file-line">        <span class="pl-s"><span class="pl-pds">&#39;&#39;&#39;</span>Connect a new route, storing any named routes for later.</span></td>
      </tr>
      <tr>
        <td id="L27" class="blob-num js-line-number" data-line-number="27"></td>
        <td id="LC27" class="blob-code blob-code-inner js-file-line"><span class="pl-s"></span></td>
      </tr>
      <tr>
        <td id="L28" class="blob-num js-line-number" data-line-number="28"></td>
        <td id="LC28" class="blob-code blob-code-inner js-file-line"><span class="pl-s">        This custom connect() method wraps the standard connect() method,</span></td>
      </tr>
      <tr>
        <td id="L29" class="blob-num js-line-number" data-line-number="29"></td>
        <td id="LC29" class="blob-code blob-code-inner js-file-line"><span class="pl-s">        and additionally saves any named routes that are connected in a dict</span></td>
      </tr>
      <tr>
        <td id="L30" class="blob-num js-line-number" data-line-number="30"></td>
        <td id="LC30" class="blob-code blob-code-inner js-file-line"><span class="pl-s">        ckan.routing.named_routes, which ends up being accessible via the</span></td>
      </tr>
      <tr>
        <td id="L31" class="blob-num js-line-number" data-line-number="31"></td>
        <td id="LC31" class="blob-code blob-code-inner js-file-line"><span class="pl-s">        Pylons config as config[&#39;routes.named_routes&#39;].</span></td>
      </tr>
      <tr>
        <td id="L32" class="blob-num js-line-number" data-line-number="32"></td>
        <td id="LC32" class="blob-code blob-code-inner js-file-line"><span class="pl-s"></span></td>
      </tr>
      <tr>
        <td id="L33" class="blob-num js-line-number" data-line-number="33"></td>
        <td id="LC33" class="blob-code blob-code-inner js-file-line"><span class="pl-s">        Also takes some additional params:</span></td>
      </tr>
      <tr>
        <td id="L34" class="blob-num js-line-number" data-line-number="34"></td>
        <td id="LC34" class="blob-code blob-code-inner js-file-line"><span class="pl-s"></span></td>
      </tr>
      <tr>
        <td id="L35" class="blob-num js-line-number" data-line-number="35"></td>
        <td id="LC35" class="blob-code blob-code-inner js-file-line"><span class="pl-s">        :param ckan_icon: name of the icon to be associated with this route,</span></td>
      </tr>
      <tr>
        <td id="L36" class="blob-num js-line-number" data-line-number="36"></td>
        <td id="LC36" class="blob-code blob-code-inner js-file-line"><span class="pl-s">            e.g. &#39;group&#39;, &#39;time&#39;. Available icons are listed here:</span></td>
      </tr>
      <tr>
        <td id="L37" class="blob-num js-line-number" data-line-number="37"></td>
        <td id="LC37" class="blob-code blob-code-inner js-file-line"><span class="pl-s">            http://fortawesome.github.io/Font-Awesome/3.2.1/icons/</span></td>
      </tr>
      <tr>
        <td id="L38" class="blob-num js-line-number" data-line-number="38"></td>
        <td id="LC38" class="blob-code blob-code-inner js-file-line"><span class="pl-s">        :type ckan_icon: string</span></td>
      </tr>
      <tr>
        <td id="L39" class="blob-num js-line-number" data-line-number="39"></td>
        <td id="LC39" class="blob-code blob-code-inner js-file-line"><span class="pl-s">        :param highlight_actions: space-separated list of controller actions</span></td>
      </tr>
      <tr>
        <td id="L40" class="blob-num js-line-number" data-line-number="40"></td>
        <td id="LC40" class="blob-code blob-code-inner js-file-line"><span class="pl-s">            that should be treated as the same as this named route for menu</span></td>
      </tr>
      <tr>
        <td id="L41" class="blob-num js-line-number" data-line-number="41"></td>
        <td id="LC41" class="blob-code blob-code-inner js-file-line"><span class="pl-s">            highlighting purposes, e.g. &#39;index search&#39;</span></td>
      </tr>
      <tr>
        <td id="L42" class="blob-num js-line-number" data-line-number="42"></td>
        <td id="LC42" class="blob-code blob-code-inner js-file-line"><span class="pl-s">        :type highlight_actions: string</span></td>
      </tr>
      <tr>
        <td id="L43" class="blob-num js-line-number" data-line-number="43"></td>
        <td id="LC43" class="blob-code blob-code-inner js-file-line"><span class="pl-s"></span></td>
      </tr>
      <tr>
        <td id="L44" class="blob-num js-line-number" data-line-number="44"></td>
        <td id="LC44" class="blob-code blob-code-inner js-file-line"><span class="pl-s">        <span class="pl-pds">&#39;&#39;&#39;</span></span></td>
      </tr>
      <tr>
        <td id="L45" class="blob-num js-line-number" data-line-number="45"></td>
        <td id="LC45" class="blob-code blob-code-inner js-file-line">
</td>
      </tr>
      <tr>
        <td id="L46" class="blob-num js-line-number" data-line-number="46"></td>
        <td id="LC46" class="blob-code blob-code-inner js-file-line">        ckan_icon <span class="pl-k">=</span> kw.pop(<span class="pl-s"><span class="pl-pds">&#39;</span>ckan_icon<span class="pl-pds">&#39;</span></span>, <span class="pl-c1">None</span>)</td>
      </tr>
      <tr>
        <td id="L47" class="blob-num js-line-number" data-line-number="47"></td>
        <td id="LC47" class="blob-code blob-code-inner js-file-line">        highlight_actions <span class="pl-k">=</span> kw.pop(<span class="pl-s"><span class="pl-pds">&#39;</span>highlight_actions<span class="pl-pds">&#39;</span></span>, kw.get(<span class="pl-s"><span class="pl-pds">&#39;</span>action<span class="pl-pds">&#39;</span></span>, <span class="pl-s"><span class="pl-pds">&#39;</span><span class="pl-pds">&#39;</span></span>))</td>
      </tr>
      <tr>
        <td id="L48" class="blob-num js-line-number" data-line-number="48"></td>
        <td id="LC48" class="blob-code blob-code-inner js-file-line">        ckan_core <span class="pl-k">=</span> kw.pop(<span class="pl-s"><span class="pl-pds">&#39;</span>ckan_core<span class="pl-pds">&#39;</span></span>, <span class="pl-c1">None</span>)</td>
      </tr>
      <tr>
        <td id="L49" class="blob-num js-line-number" data-line-number="49"></td>
        <td id="LC49" class="blob-code blob-code-inner js-file-line">        out <span class="pl-k">=</span> _Mapper.connect(<span class="pl-c1">self</span>, <span class="pl-k">*</span>args, <span class="pl-k">**</span>kw)</td>
      </tr>
      <tr>
        <td id="L50" class="blob-num js-line-number" data-line-number="50"></td>
        <td id="LC50" class="blob-code blob-code-inner js-file-line">        route <span class="pl-k">=</span> <span class="pl-c1">self</span>.matchlist[<span class="pl-k">-</span><span class="pl-c1">1</span>]</td>
      </tr>
      <tr>
        <td id="L51" class="blob-num js-line-number" data-line-number="51"></td>
        <td id="LC51" class="blob-code blob-code-inner js-file-line">        <span class="pl-k">if</span> ckan_core <span class="pl-k">is</span> <span class="pl-k">not</span> <span class="pl-c1">None</span>:</td>
      </tr>
      <tr>
        <td id="L52" class="blob-num js-line-number" data-line-number="52"></td>
        <td id="LC52" class="blob-code blob-code-inner js-file-line">            route._ckan_core <span class="pl-k">=</span> ckan_core</td>
      </tr>
      <tr>
        <td id="L53" class="blob-num js-line-number" data-line-number="53"></td>
        <td id="LC53" class="blob-code blob-code-inner js-file-line">        <span class="pl-k">if</span> <span class="pl-c1">len</span>(args) <span class="pl-k">==</span> <span class="pl-c1">1</span> <span class="pl-k">or</span> args[<span class="pl-c1">0</span>].startswith(<span class="pl-s"><span class="pl-pds">&#39;</span>_redirect_<span class="pl-pds">&#39;</span></span>):</td>
      </tr>
      <tr>
        <td id="L54" class="blob-num js-line-number" data-line-number="54"></td>
        <td id="LC54" class="blob-code blob-code-inner js-file-line">            <span class="pl-k">return</span> out</td>
      </tr>
      <tr>
        <td id="L55" class="blob-num js-line-number" data-line-number="55"></td>
        <td id="LC55" class="blob-code blob-code-inner js-file-line">        <span class="pl-c"><span class="pl-c">#</span> we have a named route</span></td>
      </tr>
      <tr>
        <td id="L56" class="blob-num js-line-number" data-line-number="56"></td>
        <td id="LC56" class="blob-code blob-code-inner js-file-line">        needed <span class="pl-k">=</span> []</td>
      </tr>
      <tr>
        <td id="L57" class="blob-num js-line-number" data-line-number="57"></td>
        <td id="LC57" class="blob-code blob-code-inner js-file-line">        matches <span class="pl-k">=</span> re.findall(<span class="pl-s"><span class="pl-pds">&#39;</span>\{([^:}]*)(\}|:)<span class="pl-pds">&#39;</span></span>, args[<span class="pl-c1">1</span>])</td>
      </tr>
      <tr>
        <td id="L58" class="blob-num js-line-number" data-line-number="58"></td>
        <td id="LC58" class="blob-code blob-code-inner js-file-line">        <span class="pl-k">for</span> match <span class="pl-k">in</span> matches:</td>
      </tr>
      <tr>
        <td id="L59" class="blob-num js-line-number" data-line-number="59"></td>
        <td id="LC59" class="blob-code blob-code-inner js-file-line">            needed.append(match[<span class="pl-c1">0</span>])</td>
      </tr>
      <tr>
        <td id="L60" class="blob-num js-line-number" data-line-number="60"></td>
        <td id="LC60" class="blob-code blob-code-inner js-file-line">        route_data <span class="pl-k">=</span> {</td>
      </tr>
      <tr>
        <td id="L61" class="blob-num js-line-number" data-line-number="61"></td>
        <td id="LC61" class="blob-code blob-code-inner js-file-line">            <span class="pl-s"><span class="pl-pds">&#39;</span>icon<span class="pl-pds">&#39;</span></span>: ckan_icon,</td>
      </tr>
      <tr>
        <td id="L62" class="blob-num js-line-number" data-line-number="62"></td>
        <td id="LC62" class="blob-code blob-code-inner js-file-line">            <span class="pl-c"><span class="pl-c">#</span> needed lists the names of the parameters that need defining</span></td>
      </tr>
      <tr>
        <td id="L63" class="blob-num js-line-number" data-line-number="63"></td>
        <td id="LC63" class="blob-code blob-code-inner js-file-line">            <span class="pl-c"><span class="pl-c">#</span> for the route to be generated</span></td>
      </tr>
      <tr>
        <td id="L64" class="blob-num js-line-number" data-line-number="64"></td>
        <td id="LC64" class="blob-code blob-code-inner js-file-line">            <span class="pl-s"><span class="pl-pds">&#39;</span>needed<span class="pl-pds">&#39;</span></span>: needed,</td>
      </tr>
      <tr>
        <td id="L65" class="blob-num js-line-number" data-line-number="65"></td>
        <td id="LC65" class="blob-code blob-code-inner js-file-line">            <span class="pl-s"><span class="pl-pds">&#39;</span>controller<span class="pl-pds">&#39;</span></span>: kw.get(<span class="pl-s"><span class="pl-pds">&#39;</span>controller<span class="pl-pds">&#39;</span></span>),</td>
      </tr>
      <tr>
        <td id="L66" class="blob-num js-line-number" data-line-number="66"></td>
        <td id="LC66" class="blob-code blob-code-inner js-file-line">            <span class="pl-s"><span class="pl-pds">&#39;</span>action<span class="pl-pds">&#39;</span></span>: kw.get(<span class="pl-s"><span class="pl-pds">&#39;</span>action<span class="pl-pds">&#39;</span></span>, <span class="pl-s"><span class="pl-pds">&#39;</span><span class="pl-pds">&#39;</span></span>),</td>
      </tr>
      <tr>
        <td id="L67" class="blob-num js-line-number" data-line-number="67"></td>
        <td id="LC67" class="blob-code blob-code-inner js-file-line">            <span class="pl-s"><span class="pl-pds">&#39;</span>highlight_actions<span class="pl-pds">&#39;</span></span>: highlight_actions</td>
      </tr>
      <tr>
        <td id="L68" class="blob-num js-line-number" data-line-number="68"></td>
        <td id="LC68" class="blob-code blob-code-inner js-file-line">        }</td>
      </tr>
      <tr>
        <td id="L69" class="blob-num js-line-number" data-line-number="69"></td>
        <td id="LC69" class="blob-code blob-code-inner js-file-line">        named_routes[args[<span class="pl-c1">0</span>]] <span class="pl-k">=</span> route_data</td>
      </tr>
      <tr>
        <td id="L70" class="blob-num js-line-number" data-line-number="70"></td>
        <td id="LC70" class="blob-code blob-code-inner js-file-line">        <span class="pl-k">return</span> out</td>
      </tr>
      <tr>
        <td id="L71" class="blob-num js-line-number" data-line-number="71"></td>
        <td id="LC71" class="blob-code blob-code-inner js-file-line">
</td>
      </tr>
      <tr>
        <td id="L72" class="blob-num js-line-number" data-line-number="72"></td>
        <td id="LC72" class="blob-code blob-code-inner js-file-line">
</td>
      </tr>
      <tr>
        <td id="L73" class="blob-num js-line-number" data-line-number="73"></td>
        <td id="LC73" class="blob-code blob-code-inner js-file-line"><span class="pl-k">def</span> <span class="pl-en">make_map</span>():</td>
      </tr>
      <tr>
        <td id="L74" class="blob-num js-line-number" data-line-number="74"></td>
        <td id="LC74" class="blob-code blob-code-inner js-file-line">    <span class="pl-s"><span class="pl-pds">&quot;&quot;&quot;</span>Create, configure and return the routes Mapper<span class="pl-pds">&quot;&quot;&quot;</span></span></td>
      </tr>
      <tr>
        <td id="L75" class="blob-num js-line-number" data-line-number="75"></td>
        <td id="LC75" class="blob-code blob-code-inner js-file-line">    <span class="pl-c"><span class="pl-c">#</span> import controllers here rather than at root level because</span></td>
      </tr>
      <tr>
        <td id="L76" class="blob-num js-line-number" data-line-number="76"></td>
        <td id="LC76" class="blob-code blob-code-inner js-file-line">    <span class="pl-c"><span class="pl-c">#</span> pylons config is initialised by this point.</span></td>
      </tr>
      <tr>
        <td id="L77" class="blob-num js-line-number" data-line-number="77"></td>
        <td id="LC77" class="blob-code blob-code-inner js-file-line">
</td>
      </tr>
      <tr>
        <td id="L78" class="blob-num js-line-number" data-line-number="78"></td>
        <td id="LC78" class="blob-code blob-code-inner js-file-line">    <span class="pl-c"><span class="pl-c">#</span> Helpers to reduce code clutter</span></td>
      </tr>
      <tr>
        <td id="L79" class="blob-num js-line-number" data-line-number="79"></td>
        <td id="LC79" class="blob-code blob-code-inner js-file-line">    <span class="pl-c1">GET</span> <span class="pl-k">=</span> <span class="pl-c1">dict</span>(<span class="pl-v">method</span><span class="pl-k">=</span>[<span class="pl-s"><span class="pl-pds">&#39;</span>GET<span class="pl-pds">&#39;</span></span>])</td>
      </tr>
      <tr>
        <td id="L80" class="blob-num js-line-number" data-line-number="80"></td>
        <td id="LC80" class="blob-code blob-code-inner js-file-line">    <span class="pl-c1">PUT</span> <span class="pl-k">=</span> <span class="pl-c1">dict</span>(<span class="pl-v">method</span><span class="pl-k">=</span>[<span class="pl-s"><span class="pl-pds">&#39;</span>PUT<span class="pl-pds">&#39;</span></span>])</td>
      </tr>
      <tr>
        <td id="L81" class="blob-num js-line-number" data-line-number="81"></td>
        <td id="LC81" class="blob-code blob-code-inner js-file-line">    <span class="pl-c1">POST</span> <span class="pl-k">=</span> <span class="pl-c1">dict</span>(<span class="pl-v">method</span><span class="pl-k">=</span>[<span class="pl-s"><span class="pl-pds">&#39;</span>POST<span class="pl-pds">&#39;</span></span>])</td>
      </tr>
      <tr>
        <td id="L82" class="blob-num js-line-number" data-line-number="82"></td>
        <td id="LC82" class="blob-code blob-code-inner js-file-line">    <span class="pl-c1">DELETE</span> <span class="pl-k">=</span> <span class="pl-c1">dict</span>(<span class="pl-v">method</span><span class="pl-k">=</span>[<span class="pl-s"><span class="pl-pds">&#39;</span>DELETE<span class="pl-pds">&#39;</span></span>])</td>
      </tr>
      <tr>
        <td id="L83" class="blob-num js-line-number" data-line-number="83"></td>
        <td id="LC83" class="blob-code blob-code-inner js-file-line">    <span class="pl-c1">GET_POST</span> <span class="pl-k">=</span> <span class="pl-c1">dict</span>(<span class="pl-v">method</span><span class="pl-k">=</span>[<span class="pl-s"><span class="pl-pds">&#39;</span>GET<span class="pl-pds">&#39;</span></span>, <span class="pl-s"><span class="pl-pds">&#39;</span>POST<span class="pl-pds">&#39;</span></span>])</td>
      </tr>
      <tr>
        <td id="L84" class="blob-num js-line-number" data-line-number="84"></td>
        <td id="LC84" class="blob-code blob-code-inner js-file-line">    <span class="pl-c1">PUT_POST</span> <span class="pl-k">=</span> <span class="pl-c1">dict</span>(<span class="pl-v">method</span><span class="pl-k">=</span>[<span class="pl-s"><span class="pl-pds">&#39;</span>PUT<span class="pl-pds">&#39;</span></span>, <span class="pl-s"><span class="pl-pds">&#39;</span>POST<span class="pl-pds">&#39;</span></span>])</td>
      </tr>
      <tr>
        <td id="L85" class="blob-num js-line-number" data-line-number="85"></td>
        <td id="LC85" class="blob-code blob-code-inner js-file-line">    <span class="pl-c1">PUT_POST_DELETE</span> <span class="pl-k">=</span> <span class="pl-c1">dict</span>(<span class="pl-v">method</span><span class="pl-k">=</span>[<span class="pl-s"><span class="pl-pds">&#39;</span>PUT<span class="pl-pds">&#39;</span></span>, <span class="pl-s"><span class="pl-pds">&#39;</span>POST<span class="pl-pds">&#39;</span></span>, <span class="pl-s"><span class="pl-pds">&#39;</span>DELETE<span class="pl-pds">&#39;</span></span>])</td>
      </tr>
      <tr>
        <td id="L86" class="blob-num js-line-number" data-line-number="86"></td>
        <td id="LC86" class="blob-code blob-code-inner js-file-line">    <span class="pl-c1">OPTIONS</span> <span class="pl-k">=</span> <span class="pl-c1">dict</span>(<span class="pl-v">method</span><span class="pl-k">=</span>[<span class="pl-s"><span class="pl-pds">&#39;</span>OPTIONS<span class="pl-pds">&#39;</span></span>])</td>
      </tr>
      <tr>
        <td id="L87" class="blob-num js-line-number" data-line-number="87"></td>
        <td id="LC87" class="blob-code blob-code-inner js-file-line">
</td>
      </tr>
      <tr>
        <td id="L88" class="blob-num js-line-number" data-line-number="88"></td>
        <td id="LC88" class="blob-code blob-code-inner js-file-line">    <span class="pl-k">import</span> ckan.lib.plugins <span class="pl-k">as</span> lib_plugins</td>
      </tr>
      <tr>
        <td id="L89" class="blob-num js-line-number" data-line-number="89"></td>
        <td id="LC89" class="blob-code blob-code-inner js-file-line">    lib_plugins.reset_package_plugins()</td>
      </tr>
      <tr>
        <td id="L90" class="blob-num js-line-number" data-line-number="90"></td>
        <td id="LC90" class="blob-code blob-code-inner js-file-line">
</td>
      </tr>
      <tr>
        <td id="L91" class="blob-num js-line-number" data-line-number="91"></td>
        <td id="LC91" class="blob-code blob-code-inner js-file-line">    <span class="pl-c1">map</span> <span class="pl-k">=</span> Mapper(<span class="pl-v">directory</span><span class="pl-k">=</span>config[<span class="pl-s"><span class="pl-pds">&#39;</span>pylons.paths<span class="pl-pds">&#39;</span></span>][<span class="pl-s"><span class="pl-pds">&#39;</span>controllers<span class="pl-pds">&#39;</span></span>],</td>
      </tr>
      <tr>
        <td id="L92" class="blob-num js-line-number" data-line-number="92"></td>
        <td id="LC92" class="blob-code blob-code-inner js-file-line">                 <span class="pl-v">always_scan</span><span class="pl-k">=</span>config[<span class="pl-s"><span class="pl-pds">&#39;</span>debug<span class="pl-pds">&#39;</span></span>])</td>
      </tr>
      <tr>
        <td id="L93" class="blob-num js-line-number" data-line-number="93"></td>
        <td id="LC93" class="blob-code blob-code-inner js-file-line">    <span class="pl-c1">map</span>.minimization <span class="pl-k">=</span> <span class="pl-c1">False</span></td>
      </tr>
      <tr>
        <td id="L94" class="blob-num js-line-number" data-line-number="94"></td>
        <td id="LC94" class="blob-code blob-code-inner js-file-line">    <span class="pl-c1">map</span>.explicit <span class="pl-k">=</span> <span class="pl-c1">True</span></td>
      </tr>
      <tr>
        <td id="L95" class="blob-num js-line-number" data-line-number="95"></td>
        <td id="LC95" class="blob-code blob-code-inner js-file-line">
</td>
      </tr>
      <tr>
        <td id="L96" class="blob-num js-line-number" data-line-number="96"></td>
        <td id="LC96" class="blob-code blob-code-inner js-file-line">    <span class="pl-c"><span class="pl-c">#</span> CUSTOM ROUTES HERE</span></td>
      </tr>
      <tr>
        <td id="L97" class="blob-num js-line-number" data-line-number="97"></td>
        <td id="LC97" class="blob-code blob-code-inner js-file-line">    <span class="pl-k">for</span> plugin <span class="pl-k">in</span> p.PluginImplementations(p.IRoutes):</td>
      </tr>
      <tr>
        <td id="L98" class="blob-num js-line-number" data-line-number="98"></td>
        <td id="LC98" class="blob-code blob-code-inner js-file-line">        <span class="pl-c1">map</span> <span class="pl-k">=</span> plugin.before_map(<span class="pl-c1">map</span>)</td>
      </tr>
      <tr>
        <td id="L99" class="blob-num js-line-number" data-line-number="99"></td>
        <td id="LC99" class="blob-code blob-code-inner js-file-line">
</td>
      </tr>
      <tr>
        <td id="L100" class="blob-num js-line-number" data-line-number="100"></td>
        <td id="LC100" class="blob-code blob-code-inner js-file-line">    <span class="pl-c"><span class="pl-c">#</span> The ErrorController route (handles 404/500 error pages); it should</span></td>
      </tr>
      <tr>
        <td id="L101" class="blob-num js-line-number" data-line-number="101"></td>
        <td id="LC101" class="blob-code blob-code-inner js-file-line">    <span class="pl-c"><span class="pl-c">#</span> likely stay at the top, ensuring it can always be resolved.</span></td>
      </tr>
      <tr>
        <td id="L102" class="blob-num js-line-number" data-line-number="102"></td>
        <td id="LC102" class="blob-code blob-code-inner js-file-line">    <span class="pl-c1">map</span>.connect(<span class="pl-s"><span class="pl-pds">&#39;</span>/error/<span class="pl-c1">{action}</span><span class="pl-pds">&#39;</span></span>, <span class="pl-v">controller</span><span class="pl-k">=</span><span class="pl-s"><span class="pl-pds">&#39;</span>error<span class="pl-pds">&#39;</span></span>, <span class="pl-v">ckan_core</span><span class="pl-k">=</span><span class="pl-c1">True</span>)</td>
      </tr>
      <tr>
        <td id="L103" class="blob-num js-line-number" data-line-number="103"></td>
        <td id="LC103" class="blob-code blob-code-inner js-file-line">    <span class="pl-c1">map</span>.connect(<span class="pl-s"><span class="pl-pds">&#39;</span>/error/<span class="pl-c1">{action}</span>/<span class="pl-c1">{id}</span><span class="pl-pds">&#39;</span></span>, <span class="pl-v">controller</span><span class="pl-k">=</span><span class="pl-s"><span class="pl-pds">&#39;</span>error<span class="pl-pds">&#39;</span></span>, <span class="pl-v">ckan_core</span><span class="pl-k">=</span><span class="pl-c1">True</span>)</td>
      </tr>
      <tr>
        <td id="L104" class="blob-num js-line-number" data-line-number="104"></td>
        <td id="LC104" class="blob-code blob-code-inner js-file-line">
</td>
      </tr>
      <tr>
        <td id="L105" class="blob-num js-line-number" data-line-number="105"></td>
        <td id="LC105" class="blob-code blob-code-inner js-file-line">    <span class="pl-c1">map</span>.connect(<span class="pl-s"><span class="pl-pds">&#39;</span>*url<span class="pl-pds">&#39;</span></span>, <span class="pl-v">controller</span><span class="pl-k">=</span><span class="pl-s"><span class="pl-pds">&#39;</span>home<span class="pl-pds">&#39;</span></span>, <span class="pl-v">action</span><span class="pl-k">=</span><span class="pl-s"><span class="pl-pds">&#39;</span>cors_options<span class="pl-pds">&#39;</span></span>,</td>
      </tr>
      <tr>
        <td id="L106" class="blob-num js-line-number" data-line-number="106"></td>
        <td id="LC106" class="blob-code blob-code-inner js-file-line">                <span class="pl-v">conditions</span><span class="pl-k">=</span><span class="pl-c1">OPTIONS</span>, <span class="pl-v">ckan_core</span><span class="pl-k">=</span><span class="pl-c1">True</span>)</td>
      </tr>
      <tr>
        <td id="L107" class="blob-num js-line-number" data-line-number="107"></td>
        <td id="LC107" class="blob-code blob-code-inner js-file-line">
</td>
      </tr>
      <tr>
        <td id="L108" class="blob-num js-line-number" data-line-number="108"></td>
        <td id="LC108" class="blob-code blob-code-inner js-file-line">    <span class="pl-c"><span class="pl-c">#</span> Mark all routes added from extensions on the `before_map` extension point</span></td>
      </tr>
      <tr>
        <td id="L109" class="blob-num js-line-number" data-line-number="109"></td>
        <td id="LC109" class="blob-code blob-code-inner js-file-line">    <span class="pl-c"><span class="pl-c">#</span> as non-core</span></td>
      </tr>
      <tr>
        <td id="L110" class="blob-num js-line-number" data-line-number="110"></td>
        <td id="LC110" class="blob-code blob-code-inner js-file-line">    <span class="pl-k">for</span> route <span class="pl-k">in</span> <span class="pl-c1">map</span>.matchlist:</td>
      </tr>
      <tr>
        <td id="L111" class="blob-num js-line-number" data-line-number="111"></td>
        <td id="LC111" class="blob-code blob-code-inner js-file-line">        <span class="pl-k">if</span> <span class="pl-k">not</span> <span class="pl-c1">hasattr</span>(route, <span class="pl-s"><span class="pl-pds">&#39;</span>_ckan_core<span class="pl-pds">&#39;</span></span>):</td>
      </tr>
      <tr>
        <td id="L112" class="blob-num js-line-number" data-line-number="112"></td>
        <td id="LC112" class="blob-code blob-code-inner js-file-line">            route._ckan_core <span class="pl-k">=</span> <span class="pl-c1">False</span></td>
      </tr>
      <tr>
        <td id="L113" class="blob-num js-line-number" data-line-number="113"></td>
        <td id="LC113" class="blob-code blob-code-inner js-file-line">
</td>
      </tr>
      <tr>
        <td id="L114" class="blob-num js-line-number" data-line-number="114"></td>
        <td id="LC114" class="blob-code blob-code-inner js-file-line">    <span class="pl-c1">map</span>.connect(<span class="pl-s"><span class="pl-pds">&#39;</span>home<span class="pl-pds">&#39;</span></span>, <span class="pl-s"><span class="pl-pds">&#39;</span>/<span class="pl-pds">&#39;</span></span>, <span class="pl-v">controller</span><span class="pl-k">=</span><span class="pl-s"><span class="pl-pds">&#39;</span>home<span class="pl-pds">&#39;</span></span>, <span class="pl-v">action</span><span class="pl-k">=</span><span class="pl-s"><span class="pl-pds">&#39;</span>index<span class="pl-pds">&#39;</span></span>)</td>
      </tr>
      <tr>
        <td id="L115" class="blob-num js-line-number" data-line-number="115"></td>
        <td id="LC115" class="blob-code blob-code-inner js-file-line">    <span class="pl-c1">map</span>.connect(<span class="pl-s"><span class="pl-pds">&#39;</span>about<span class="pl-pds">&#39;</span></span>, <span class="pl-s"><span class="pl-pds">&#39;</span>/about<span class="pl-pds">&#39;</span></span>, <span class="pl-v">controller</span><span class="pl-k">=</span><span class="pl-s"><span class="pl-pds">&#39;</span>home<span class="pl-pds">&#39;</span></span>, <span class="pl-v">action</span><span class="pl-k">=</span><span class="pl-s"><span class="pl-pds">&#39;</span>about<span class="pl-pds">&#39;</span></span>)</td>
      </tr>
      <tr>
        <td id="L116" class="blob-num js-line-number" data-line-number="116"></td>
        <td id="LC116" class="blob-code blob-code-inner js-file-line">    <span class="pl-c"><span class="pl-c">#</span> CKAN API versioned.</span></td>
      </tr>
      <tr>
        <td id="L117" class="blob-num js-line-number" data-line-number="117"></td>
        <td id="LC117" class="blob-code blob-code-inner js-file-line">    register_list <span class="pl-k">=</span> [</td>
      </tr>
      <tr>
        <td id="L118" class="blob-num js-line-number" data-line-number="118"></td>
        <td id="LC118" class="blob-code blob-code-inner js-file-line">        <span class="pl-s"><span class="pl-pds">&#39;</span>package<span class="pl-pds">&#39;</span></span>,</td>
      </tr>
      <tr>
        <td id="L119" class="blob-num js-line-number" data-line-number="119"></td>
        <td id="LC119" class="blob-code blob-code-inner js-file-line">        <span class="pl-s"><span class="pl-pds">&#39;</span>dataset<span class="pl-pds">&#39;</span></span>,</td>
      </tr>
      <tr>
        <td id="L120" class="blob-num js-line-number" data-line-number="120"></td>
        <td id="LC120" class="blob-code blob-code-inner js-file-line">        <span class="pl-s"><span class="pl-pds">&#39;</span>resource<span class="pl-pds">&#39;</span></span>,</td>
      </tr>
      <tr>
        <td id="L121" class="blob-num js-line-number" data-line-number="121"></td>
        <td id="LC121" class="blob-code blob-code-inner js-file-line">        <span class="pl-s"><span class="pl-pds">&#39;</span>tag<span class="pl-pds">&#39;</span></span>,</td>
      </tr>
      <tr>
        <td id="L122" class="blob-num js-line-number" data-line-number="122"></td>
        <td id="LC122" class="blob-code blob-code-inner js-file-line">        <span class="pl-s"><span class="pl-pds">&#39;</span>group<span class="pl-pds">&#39;</span></span>,</td>
      </tr>
      <tr>
        <td id="L123" class="blob-num js-line-number" data-line-number="123"></td>
        <td id="LC123" class="blob-code blob-code-inner js-file-line">        <span class="pl-s"><span class="pl-pds">&#39;</span>revision<span class="pl-pds">&#39;</span></span>,</td>
      </tr>
      <tr>
        <td id="L124" class="blob-num js-line-number" data-line-number="124"></td>
        <td id="LC124" class="blob-code blob-code-inner js-file-line">        <span class="pl-s"><span class="pl-pds">&#39;</span>licenses<span class="pl-pds">&#39;</span></span>,</td>
      </tr>
      <tr>
        <td id="L125" class="blob-num js-line-number" data-line-number="125"></td>
        <td id="LC125" class="blob-code blob-code-inner js-file-line">        <span class="pl-s"><span class="pl-pds">&#39;</span>rating<span class="pl-pds">&#39;</span></span>,</td>
      </tr>
      <tr>
        <td id="L126" class="blob-num js-line-number" data-line-number="126"></td>
        <td id="LC126" class="blob-code blob-code-inner js-file-line">        <span class="pl-s"><span class="pl-pds">&#39;</span>user<span class="pl-pds">&#39;</span></span>,</td>
      </tr>
      <tr>
        <td id="L127" class="blob-num js-line-number" data-line-number="127"></td>
        <td id="LC127" class="blob-code blob-code-inner js-file-line">        <span class="pl-s"><span class="pl-pds">&#39;</span>activity<span class="pl-pds">&#39;</span></span></td>
      </tr>
      <tr>
        <td id="L128" class="blob-num js-line-number" data-line-number="128"></td>
        <td id="LC128" class="blob-code blob-code-inner js-file-line">    ]</td>
      </tr>
      <tr>
        <td id="L129" class="blob-num js-line-number" data-line-number="129"></td>
        <td id="LC129" class="blob-code blob-code-inner js-file-line">    register_list_str <span class="pl-k">=</span> <span class="pl-s"><span class="pl-pds">&#39;</span>|<span class="pl-pds">&#39;</span></span>.join(register_list)</td>
      </tr>
      <tr>
        <td id="L130" class="blob-num js-line-number" data-line-number="130"></td>
        <td id="LC130" class="blob-code blob-code-inner js-file-line">
</td>
      </tr>
      <tr>
        <td id="L131" class="blob-num js-line-number" data-line-number="131"></td>
        <td id="LC131" class="blob-code blob-code-inner js-file-line">    <span class="pl-c"><span class="pl-c">#</span> /api ver 1, 2, 3 or none</span></td>
      </tr>
      <tr>
        <td id="L132" class="blob-num js-line-number" data-line-number="132"></td>
        <td id="LC132" class="blob-code blob-code-inner js-file-line">    <span class="pl-k">with</span> SubMapper(<span class="pl-c1">map</span>, <span class="pl-v">controller</span><span class="pl-k">=</span><span class="pl-s"><span class="pl-pds">&#39;</span>api<span class="pl-pds">&#39;</span></span>, <span class="pl-v">path_prefix</span><span class="pl-k">=</span><span class="pl-s"><span class="pl-pds">&#39;</span>/api<span class="pl-c1">{ver<span class="pl-k">:</span>/1|/2|/3|}</span><span class="pl-pds">&#39;</span></span>,</td>
      </tr>
      <tr>
        <td id="L133" class="blob-num js-line-number" data-line-number="133"></td>
        <td id="LC133" class="blob-code blob-code-inner js-file-line">                   <span class="pl-v">ver</span><span class="pl-k">=</span><span class="pl-s"><span class="pl-pds">&#39;</span>/1<span class="pl-pds">&#39;</span></span>) <span class="pl-k">as</span> m:</td>
      </tr>
      <tr>
        <td id="L134" class="blob-num js-line-number" data-line-number="134"></td>
        <td id="LC134" class="blob-code blob-code-inner js-file-line">        m.connect(<span class="pl-s"><span class="pl-pds">&#39;</span>/search/<span class="pl-c1">{register}</span><span class="pl-pds">&#39;</span></span>, <span class="pl-v">action</span><span class="pl-k">=</span><span class="pl-s"><span class="pl-pds">&#39;</span>search<span class="pl-pds">&#39;</span></span>)</td>
      </tr>
      <tr>
        <td id="L135" class="blob-num js-line-number" data-line-number="135"></td>
        <td id="LC135" class="blob-code blob-code-inner js-file-line">
</td>
      </tr>
      <tr>
        <td id="L136" class="blob-num js-line-number" data-line-number="136"></td>
        <td id="LC136" class="blob-code blob-code-inner js-file-line">    <span class="pl-c"><span class="pl-c">#</span> /api ver 1, 2 or none</span></td>
      </tr>
      <tr>
        <td id="L137" class="blob-num js-line-number" data-line-number="137"></td>
        <td id="LC137" class="blob-code blob-code-inner js-file-line">    <span class="pl-k">with</span> SubMapper(<span class="pl-c1">map</span>, <span class="pl-v">controller</span><span class="pl-k">=</span><span class="pl-s"><span class="pl-pds">&#39;</span>api<span class="pl-pds">&#39;</span></span>, <span class="pl-v">path_prefix</span><span class="pl-k">=</span><span class="pl-s"><span class="pl-pds">&#39;</span>/api<span class="pl-c1">{ver<span class="pl-k">:</span>/1|/2|}</span><span class="pl-pds">&#39;</span></span>,</td>
      </tr>
      <tr>
        <td id="L138" class="blob-num js-line-number" data-line-number="138"></td>
        <td id="LC138" class="blob-code blob-code-inner js-file-line">                   <span class="pl-v">ver</span><span class="pl-k">=</span><span class="pl-s"><span class="pl-pds">&#39;</span>/1<span class="pl-pds">&#39;</span></span>) <span class="pl-k">as</span> m:</td>
      </tr>
      <tr>
        <td id="L139" class="blob-num js-line-number" data-line-number="139"></td>
        <td id="LC139" class="blob-code blob-code-inner js-file-line">        m.connect(<span class="pl-s"><span class="pl-pds">&#39;</span>/rest<span class="pl-pds">&#39;</span></span>, <span class="pl-v">action</span><span class="pl-k">=</span><span class="pl-s"><span class="pl-pds">&#39;</span>index<span class="pl-pds">&#39;</span></span>)</td>
      </tr>
      <tr>
        <td id="L140" class="blob-num js-line-number" data-line-number="140"></td>
        <td id="LC140" class="blob-code blob-code-inner js-file-line">
</td>
      </tr>
      <tr>
        <td id="L141" class="blob-num js-line-number" data-line-number="141"></td>
        <td id="LC141" class="blob-code blob-code-inner js-file-line">    <span class="pl-c"><span class="pl-c">#</span> /api/rest ver 1, 2 or none</span></td>
      </tr>
      <tr>
        <td id="L142" class="blob-num js-line-number" data-line-number="142"></td>
        <td id="LC142" class="blob-code blob-code-inner js-file-line">    <span class="pl-k">with</span> SubMapper(<span class="pl-c1">map</span>, <span class="pl-v">controller</span><span class="pl-k">=</span><span class="pl-s"><span class="pl-pds">&#39;</span>api<span class="pl-pds">&#39;</span></span>, <span class="pl-v">path_prefix</span><span class="pl-k">=</span><span class="pl-s"><span class="pl-pds">&#39;</span>/api<span class="pl-c1">{ver<span class="pl-k">:</span>/1|/2|}</span><span class="pl-pds">&#39;</span></span>,</td>
      </tr>
      <tr>
        <td id="L143" class="blob-num js-line-number" data-line-number="143"></td>
        <td id="LC143" class="blob-code blob-code-inner js-file-line">                   <span class="pl-v">ver</span><span class="pl-k">=</span><span class="pl-s"><span class="pl-pds">&#39;</span>/1<span class="pl-pds">&#39;</span></span>, <span class="pl-v">requirements</span><span class="pl-k">=</span><span class="pl-c1">dict</span>(<span class="pl-v">register</span><span class="pl-k">=</span>register_list_str)</td>
      </tr>
      <tr>
        <td id="L144" class="blob-num js-line-number" data-line-number="144"></td>
        <td id="LC144" class="blob-code blob-code-inner js-file-line">                   ) <span class="pl-k">as</span> m:</td>
      </tr>
      <tr>
        <td id="L145" class="blob-num js-line-number" data-line-number="145"></td>
        <td id="LC145" class="blob-code blob-code-inner js-file-line">
</td>
      </tr>
      <tr>
        <td id="L146" class="blob-num js-line-number" data-line-number="146"></td>
        <td id="LC146" class="blob-code blob-code-inner js-file-line">        m.connect(<span class="pl-s"><span class="pl-pds">&#39;</span>/rest/<span class="pl-c1">{register}</span><span class="pl-pds">&#39;</span></span>, <span class="pl-v">action</span><span class="pl-k">=</span><span class="pl-s"><span class="pl-pds">&#39;</span>list<span class="pl-pds">&#39;</span></span>, <span class="pl-v">conditions</span><span class="pl-k">=</span><span class="pl-c1">GET</span>)</td>
      </tr>
      <tr>
        <td id="L147" class="blob-num js-line-number" data-line-number="147"></td>
        <td id="LC147" class="blob-code blob-code-inner js-file-line">        m.connect(<span class="pl-s"><span class="pl-pds">&#39;</span>/rest/<span class="pl-c1">{register}</span><span class="pl-pds">&#39;</span></span>, <span class="pl-v">action</span><span class="pl-k">=</span><span class="pl-s"><span class="pl-pds">&#39;</span>create<span class="pl-pds">&#39;</span></span>, <span class="pl-v">conditions</span><span class="pl-k">=</span><span class="pl-c1">POST</span>)</td>
      </tr>
      <tr>
        <td id="L148" class="blob-num js-line-number" data-line-number="148"></td>
        <td id="LC148" class="blob-code blob-code-inner js-file-line">        m.connect(<span class="pl-s"><span class="pl-pds">&#39;</span>/rest/<span class="pl-c1">{register}</span>/<span class="pl-c1">{id}</span><span class="pl-pds">&#39;</span></span>, <span class="pl-v">action</span><span class="pl-k">=</span><span class="pl-s"><span class="pl-pds">&#39;</span>show<span class="pl-pds">&#39;</span></span>, <span class="pl-v">conditions</span><span class="pl-k">=</span><span class="pl-c1">GET</span>)</td>
      </tr>
      <tr>
        <td id="L149" class="blob-num js-line-number" data-line-number="149"></td>
        <td id="LC149" class="blob-code blob-code-inner js-file-line">        m.connect(<span class="pl-s"><span class="pl-pds">&#39;</span>/rest/<span class="pl-c1">{register}</span>/<span class="pl-c1">{id}</span><span class="pl-pds">&#39;</span></span>, <span class="pl-v">action</span><span class="pl-k">=</span><span class="pl-s"><span class="pl-pds">&#39;</span>update<span class="pl-pds">&#39;</span></span>, <span class="pl-v">conditions</span><span class="pl-k">=</span><span class="pl-c1">PUT</span>)</td>
      </tr>
      <tr>
        <td id="L150" class="blob-num js-line-number" data-line-number="150"></td>
        <td id="LC150" class="blob-code blob-code-inner js-file-line">        m.connect(<span class="pl-s"><span class="pl-pds">&#39;</span>/rest/<span class="pl-c1">{register}</span>/<span class="pl-c1">{id}</span><span class="pl-pds">&#39;</span></span>, <span class="pl-v">action</span><span class="pl-k">=</span><span class="pl-s"><span class="pl-pds">&#39;</span>update<span class="pl-pds">&#39;</span></span>, <span class="pl-v">conditions</span><span class="pl-k">=</span><span class="pl-c1">POST</span>)</td>
      </tr>
      <tr>
        <td id="L151" class="blob-num js-line-number" data-line-number="151"></td>
        <td id="LC151" class="blob-code blob-code-inner js-file-line">        m.connect(<span class="pl-s"><span class="pl-pds">&#39;</span>/rest/<span class="pl-c1">{register}</span>/<span class="pl-c1">{id}</span><span class="pl-pds">&#39;</span></span>, <span class="pl-v">action</span><span class="pl-k">=</span><span class="pl-s"><span class="pl-pds">&#39;</span>delete<span class="pl-pds">&#39;</span></span>, <span class="pl-v">conditions</span><span class="pl-k">=</span><span class="pl-c1">DELETE</span>)</td>
      </tr>
      <tr>
        <td id="L152" class="blob-num js-line-number" data-line-number="152"></td>
        <td id="LC152" class="blob-code blob-code-inner js-file-line">        m.connect(<span class="pl-s"><span class="pl-pds">&#39;</span>/rest/<span class="pl-c1">{register}</span>/<span class="pl-c1">{id}</span>/:subregister<span class="pl-pds">&#39;</span></span>, <span class="pl-v">action</span><span class="pl-k">=</span><span class="pl-s"><span class="pl-pds">&#39;</span>list<span class="pl-pds">&#39;</span></span>,</td>
      </tr>
      <tr>
        <td id="L153" class="blob-num js-line-number" data-line-number="153"></td>
        <td id="LC153" class="blob-code blob-code-inner js-file-line">                  <span class="pl-v">conditions</span><span class="pl-k">=</span><span class="pl-c1">GET</span>)</td>
      </tr>
      <tr>
        <td id="L154" class="blob-num js-line-number" data-line-number="154"></td>
        <td id="LC154" class="blob-code blob-code-inner js-file-line">        m.connect(<span class="pl-s"><span class="pl-pds">&#39;</span>/rest/<span class="pl-c1">{register}</span>/<span class="pl-c1">{id}</span>/:subregister<span class="pl-pds">&#39;</span></span>, <span class="pl-v">action</span><span class="pl-k">=</span><span class="pl-s"><span class="pl-pds">&#39;</span>create<span class="pl-pds">&#39;</span></span>,</td>
      </tr>
      <tr>
        <td id="L155" class="blob-num js-line-number" data-line-number="155"></td>
        <td id="LC155" class="blob-code blob-code-inner js-file-line">                  <span class="pl-v">conditions</span><span class="pl-k">=</span><span class="pl-c1">POST</span>)</td>
      </tr>
      <tr>
        <td id="L156" class="blob-num js-line-number" data-line-number="156"></td>
        <td id="LC156" class="blob-code blob-code-inner js-file-line">        m.connect(<span class="pl-s"><span class="pl-pds">&#39;</span>/rest/<span class="pl-c1">{register}</span>/<span class="pl-c1">{id}</span>/:subregister/<span class="pl-c1">{id2}</span><span class="pl-pds">&#39;</span></span>, <span class="pl-v">action</span><span class="pl-k">=</span><span class="pl-s"><span class="pl-pds">&#39;</span>create<span class="pl-pds">&#39;</span></span>,</td>
      </tr>
      <tr>
        <td id="L157" class="blob-num js-line-number" data-line-number="157"></td>
        <td id="LC157" class="blob-code blob-code-inner js-file-line">                  <span class="pl-v">conditions</span><span class="pl-k">=</span><span class="pl-c1">POST</span>)</td>
      </tr>
      <tr>
        <td id="L158" class="blob-num js-line-number" data-line-number="158"></td>
        <td id="LC158" class="blob-code blob-code-inner js-file-line">        m.connect(<span class="pl-s"><span class="pl-pds">&#39;</span>/rest/<span class="pl-c1">{register}</span>/<span class="pl-c1">{id}</span>/:subregister/<span class="pl-c1">{id2}</span><span class="pl-pds">&#39;</span></span>, <span class="pl-v">action</span><span class="pl-k">=</span><span class="pl-s"><span class="pl-pds">&#39;</span>show<span class="pl-pds">&#39;</span></span>,</td>
      </tr>
      <tr>
        <td id="L159" class="blob-num js-line-number" data-line-number="159"></td>
        <td id="LC159" class="blob-code blob-code-inner js-file-line">                  <span class="pl-v">conditions</span><span class="pl-k">=</span><span class="pl-c1">GET</span>)</td>
      </tr>
      <tr>
        <td id="L160" class="blob-num js-line-number" data-line-number="160"></td>
        <td id="LC160" class="blob-code blob-code-inner js-file-line">        m.connect(<span class="pl-s"><span class="pl-pds">&#39;</span>/rest/<span class="pl-c1">{register}</span>/<span class="pl-c1">{id}</span>/:subregister/<span class="pl-c1">{id2}</span><span class="pl-pds">&#39;</span></span>, <span class="pl-v">action</span><span class="pl-k">=</span><span class="pl-s"><span class="pl-pds">&#39;</span>update<span class="pl-pds">&#39;</span></span>,</td>
      </tr>
      <tr>
        <td id="L161" class="blob-num js-line-number" data-line-number="161"></td>
        <td id="LC161" class="blob-code blob-code-inner js-file-line">                  <span class="pl-v">conditions</span><span class="pl-k">=</span><span class="pl-c1">PUT</span>)</td>
      </tr>
      <tr>
        <td id="L162" class="blob-num js-line-number" data-line-number="162"></td>
        <td id="LC162" class="blob-code blob-code-inner js-file-line">        m.connect(<span class="pl-s"><span class="pl-pds">&#39;</span>/rest/<span class="pl-c1">{register}</span>/<span class="pl-c1">{id}</span>/:subregister/<span class="pl-c1">{id2}</span><span class="pl-pds">&#39;</span></span>, <span class="pl-v">action</span><span class="pl-k">=</span><span class="pl-s"><span class="pl-pds">&#39;</span>delete<span class="pl-pds">&#39;</span></span>,</td>
      </tr>
      <tr>
        <td id="L163" class="blob-num js-line-number" data-line-number="163"></td>
        <td id="LC163" class="blob-code blob-code-inner js-file-line">                  <span class="pl-v">conditions</span><span class="pl-k">=</span><span class="pl-c1">DELETE</span>)</td>
      </tr>
      <tr>
        <td id="L164" class="blob-num js-line-number" data-line-number="164"></td>
        <td id="LC164" class="blob-code blob-code-inner js-file-line">
</td>
      </tr>
      <tr>
        <td id="L165" class="blob-num js-line-number" data-line-number="165"></td>
        <td id="LC165" class="blob-code blob-code-inner js-file-line">
</td>
      </tr>
      <tr>
        <td id="L166" class="blob-num js-line-number" data-line-number="166"></td>
        <td id="LC166" class="blob-code blob-code-inner js-file-line">    <span class="pl-c"><span class="pl-c">#</span> /api/util ver 1, 2 or none</span></td>
      </tr>
      <tr>
        <td id="L167" class="blob-num js-line-number" data-line-number="167"></td>
        <td id="LC167" class="blob-code blob-code-inner js-file-line">    <span class="pl-k">with</span> SubMapper(<span class="pl-c1">map</span>, <span class="pl-v">controller</span><span class="pl-k">=</span><span class="pl-s"><span class="pl-pds">&#39;</span>api<span class="pl-pds">&#39;</span></span>, <span class="pl-v">path_prefix</span><span class="pl-k">=</span><span class="pl-s"><span class="pl-pds">&#39;</span>/api<span class="pl-c1">{ver<span class="pl-k">:</span>/1|/2|}</span><span class="pl-pds">&#39;</span></span>,</td>
      </tr>
      <tr>
        <td id="L168" class="blob-num js-line-number" data-line-number="168"></td>
        <td id="LC168" class="blob-code blob-code-inner js-file-line">                   <span class="pl-v">ver</span><span class="pl-k">=</span><span class="pl-s"><span class="pl-pds">&#39;</span>/1<span class="pl-pds">&#39;</span></span>) <span class="pl-k">as</span> m:</td>
      </tr>
      <tr>
        <td id="L169" class="blob-num js-line-number" data-line-number="169"></td>
        <td id="LC169" class="blob-code blob-code-inner js-file-line">        m.connect(<span class="pl-s"><span class="pl-pds">&#39;</span>/util/dataset/munge_name<span class="pl-pds">&#39;</span></span>, <span class="pl-v">action</span><span class="pl-k">=</span><span class="pl-s"><span class="pl-pds">&#39;</span>munge_package_name<span class="pl-pds">&#39;</span></span>)</td>
      </tr>
      <tr>
        <td id="L170" class="blob-num js-line-number" data-line-number="170"></td>
        <td id="LC170" class="blob-code blob-code-inner js-file-line">        m.connect(<span class="pl-s"><span class="pl-pds">&#39;</span>/util/dataset/munge_title_to_name<span class="pl-pds">&#39;</span></span>,</td>
      </tr>
      <tr>
        <td id="L171" class="blob-num js-line-number" data-line-number="171"></td>
        <td id="LC171" class="blob-code blob-code-inner js-file-line">                  <span class="pl-v">action</span><span class="pl-k">=</span><span class="pl-s"><span class="pl-pds">&#39;</span>munge_title_to_package_name<span class="pl-pds">&#39;</span></span>)</td>
      </tr>
      <tr>
        <td id="L172" class="blob-num js-line-number" data-line-number="172"></td>
        <td id="LC172" class="blob-code blob-code-inner js-file-line">        m.connect(<span class="pl-s"><span class="pl-pds">&#39;</span>/util/tag/munge<span class="pl-pds">&#39;</span></span>, <span class="pl-v">action</span><span class="pl-k">=</span><span class="pl-s"><span class="pl-pds">&#39;</span>munge_tag<span class="pl-pds">&#39;</span></span>)</td>
      </tr>
      <tr>
        <td id="L173" class="blob-num js-line-number" data-line-number="173"></td>
        <td id="LC173" class="blob-code blob-code-inner js-file-line">
</td>
      </tr>
      <tr>
        <td id="L174" class="blob-num js-line-number" data-line-number="174"></td>
        <td id="LC174" class="blob-code blob-code-inner js-file-line">    <span class="pl-c"><span class="pl-c">#</span>##########</span></td>
      </tr>
      <tr>
        <td id="L175" class="blob-num js-line-number" data-line-number="175"></td>
        <td id="LC175" class="blob-code blob-code-inner js-file-line">    <span class="pl-c"><span class="pl-c">#</span># /END API</span></td>
      </tr>
      <tr>
        <td id="L176" class="blob-num js-line-number" data-line-number="176"></td>
        <td id="LC176" class="blob-code blob-code-inner js-file-line">    <span class="pl-c"><span class="pl-c">#</span>##########</span></td>
      </tr>
      <tr>
        <td id="L177" class="blob-num js-line-number" data-line-number="177"></td>
        <td id="LC177" class="blob-code blob-code-inner js-file-line">
</td>
      </tr>
      <tr>
        <td id="L178" class="blob-num js-line-number" data-line-number="178"></td>
        <td id="LC178" class="blob-code blob-code-inner js-file-line">    <span class="pl-c1">map</span>.redirect(<span class="pl-s"><span class="pl-pds">&#39;</span>/packages<span class="pl-pds">&#39;</span></span>, <span class="pl-s"><span class="pl-pds">&#39;</span>/dataset<span class="pl-pds">&#39;</span></span>)</td>
      </tr>
      <tr>
        <td id="L179" class="blob-num js-line-number" data-line-number="179"></td>
        <td id="LC179" class="blob-code blob-code-inner js-file-line">    <span class="pl-c1">map</span>.redirect(<span class="pl-s"><span class="pl-pds">&#39;</span>/packages/<span class="pl-c1">{url<span class="pl-k">:</span>.*}</span><span class="pl-pds">&#39;</span></span>, <span class="pl-s"><span class="pl-pds">&#39;</span>/dataset/<span class="pl-c1">{url}</span><span class="pl-pds">&#39;</span></span>)</td>
      </tr>
      <tr>
        <td id="L180" class="blob-num js-line-number" data-line-number="180"></td>
        <td id="LC180" class="blob-code blob-code-inner js-file-line">    <span class="pl-c1">map</span>.redirect(<span class="pl-s"><span class="pl-pds">&#39;</span>/package<span class="pl-pds">&#39;</span></span>, <span class="pl-s"><span class="pl-pds">&#39;</span>/dataset<span class="pl-pds">&#39;</span></span>)</td>
      </tr>
      <tr>
        <td id="L181" class="blob-num js-line-number" data-line-number="181"></td>
        <td id="LC181" class="blob-code blob-code-inner js-file-line">    <span class="pl-c1">map</span>.redirect(<span class="pl-s"><span class="pl-pds">&#39;</span>/package/<span class="pl-c1">{url<span class="pl-k">:</span>.*}</span><span class="pl-pds">&#39;</span></span>, <span class="pl-s"><span class="pl-pds">&#39;</span>/dataset/<span class="pl-c1">{url}</span><span class="pl-pds">&#39;</span></span>)</td>
      </tr>
      <tr>
        <td id="L182" class="blob-num js-line-number" data-line-number="182"></td>
        <td id="LC182" class="blob-code blob-code-inner js-file-line">
</td>
      </tr>
      <tr>
        <td id="L183" class="blob-num js-line-number" data-line-number="183"></td>
        <td id="LC183" class="blob-code blob-code-inner js-file-line">    <span class="pl-k">with</span> SubMapper(<span class="pl-c1">map</span>, <span class="pl-v">controller</span><span class="pl-k">=</span><span class="pl-s"><span class="pl-pds">&#39;</span>package<span class="pl-pds">&#39;</span></span>) <span class="pl-k">as</span> m:</td>
      </tr>
      <tr>
        <td id="L184" class="blob-num js-line-number" data-line-number="184"></td>
        <td id="LC184" class="blob-code blob-code-inner js-file-line">        m.connect(<span class="pl-s"><span class="pl-pds">&#39;</span>search<span class="pl-pds">&#39;</span></span>, <span class="pl-s"><span class="pl-pds">&#39;</span>/dataset<span class="pl-pds">&#39;</span></span>, <span class="pl-v">action</span><span class="pl-k">=</span><span class="pl-s"><span class="pl-pds">&#39;</span>search<span class="pl-pds">&#39;</span></span>,</td>
      </tr>
      <tr>
        <td id="L185" class="blob-num js-line-number" data-line-number="185"></td>
        <td id="LC185" class="blob-code blob-code-inner js-file-line">                  <span class="pl-v">highlight_actions</span><span class="pl-k">=</span><span class="pl-s"><span class="pl-pds">&#39;</span>index search<span class="pl-pds">&#39;</span></span>)</td>
      </tr>
      <tr>
        <td id="L186" class="blob-num js-line-number" data-line-number="186"></td>
        <td id="LC186" class="blob-code blob-code-inner js-file-line">        m.connect(<span class="pl-s"><span class="pl-pds">&#39;</span>add dataset<span class="pl-pds">&#39;</span></span>, <span class="pl-s"><span class="pl-pds">&#39;</span>/dataset/new<span class="pl-pds">&#39;</span></span>, <span class="pl-v">action</span><span class="pl-k">=</span><span class="pl-s"><span class="pl-pds">&#39;</span>new<span class="pl-pds">&#39;</span></span>)</td>
      </tr>
      <tr>
        <td id="L187" class="blob-num js-line-number" data-line-number="187"></td>
        <td id="LC187" class="blob-code blob-code-inner js-file-line">        m.connect(<span class="pl-s"><span class="pl-pds">&#39;</span>/dataset/<span class="pl-c1">{action}</span><span class="pl-pds">&#39;</span></span>,</td>
      </tr>
      <tr>
        <td id="L188" class="blob-num js-line-number" data-line-number="188"></td>
        <td id="LC188" class="blob-code blob-code-inner js-file-line">                  <span class="pl-v">requirements</span><span class="pl-k">=</span><span class="pl-c1">dict</span>(<span class="pl-v">action</span><span class="pl-k">=</span><span class="pl-s"><span class="pl-pds">&#39;</span>|<span class="pl-pds">&#39;</span></span>.join([</td>
      </tr>
      <tr>
        <td id="L189" class="blob-num js-line-number" data-line-number="189"></td>
        <td id="LC189" class="blob-code blob-code-inner js-file-line">                      <span class="pl-s"><span class="pl-pds">&#39;</span>list<span class="pl-pds">&#39;</span></span>,</td>
      </tr>
      <tr>
        <td id="L190" class="blob-num js-line-number" data-line-number="190"></td>
        <td id="LC190" class="blob-code blob-code-inner js-file-line">                      <span class="pl-s"><span class="pl-pds">&#39;</span>autocomplete<span class="pl-pds">&#39;</span></span>,</td>
      </tr>
      <tr>
        <td id="L191" class="blob-num js-line-number" data-line-number="191"></td>
        <td id="LC191" class="blob-code blob-code-inner js-file-line">                      <span class="pl-s"><span class="pl-pds">&#39;</span>search<span class="pl-pds">&#39;</span></span></td>
      </tr>
      <tr>
        <td id="L192" class="blob-num js-line-number" data-line-number="192"></td>
        <td id="LC192" class="blob-code blob-code-inner js-file-line">                  ])))</td>
      </tr>
      <tr>
        <td id="L193" class="blob-num js-line-number" data-line-number="193"></td>
        <td id="LC193" class="blob-code blob-code-inner js-file-line">
</td>
      </tr>
      <tr>
        <td id="L194" class="blob-num js-line-number" data-line-number="194"></td>
        <td id="LC194" class="blob-code blob-code-inner js-file-line">        m.connect(<span class="pl-s"><span class="pl-pds">&#39;</span>/dataset/<span class="pl-c1">{action}</span>/<span class="pl-c1">{id}</span>/<span class="pl-c1">{revision}</span><span class="pl-pds">&#39;</span></span>, <span class="pl-v">action</span><span class="pl-k">=</span><span class="pl-s"><span class="pl-pds">&#39;</span>read_ajax<span class="pl-pds">&#39;</span></span>,</td>
      </tr>
      <tr>
        <td id="L195" class="blob-num js-line-number" data-line-number="195"></td>
        <td id="LC195" class="blob-code blob-code-inner js-file-line">                  <span class="pl-v">requirements</span><span class="pl-k">=</span><span class="pl-c1">dict</span>(<span class="pl-v">action</span><span class="pl-k">=</span><span class="pl-s"><span class="pl-pds">&#39;</span>|<span class="pl-pds">&#39;</span></span>.join([</td>
      </tr>
      <tr>
        <td id="L196" class="blob-num js-line-number" data-line-number="196"></td>
        <td id="LC196" class="blob-code blob-code-inner js-file-line">                      <span class="pl-s"><span class="pl-pds">&#39;</span>read<span class="pl-pds">&#39;</span></span>,</td>
      </tr>
      <tr>
        <td id="L197" class="blob-num js-line-number" data-line-number="197"></td>
        <td id="LC197" class="blob-code blob-code-inner js-file-line">                      <span class="pl-s"><span class="pl-pds">&#39;</span>edit<span class="pl-pds">&#39;</span></span>,</td>
      </tr>
      <tr>
        <td id="L198" class="blob-num js-line-number" data-line-number="198"></td>
        <td id="LC198" class="blob-code blob-code-inner js-file-line">                      <span class="pl-s"><span class="pl-pds">&#39;</span>history<span class="pl-pds">&#39;</span></span>,</td>
      </tr>
      <tr>
        <td id="L199" class="blob-num js-line-number" data-line-number="199"></td>
        <td id="LC199" class="blob-code blob-code-inner js-file-line">                  ])))</td>
      </tr>
      <tr>
        <td id="L200" class="blob-num js-line-number" data-line-number="200"></td>
        <td id="LC200" class="blob-code blob-code-inner js-file-line">        m.connect(<span class="pl-s"><span class="pl-pds">&#39;</span>/dataset/<span class="pl-c1">{action}</span>/<span class="pl-c1">{id}</span><span class="pl-pds">&#39;</span></span>,</td>
      </tr>
      <tr>
        <td id="L201" class="blob-num js-line-number" data-line-number="201"></td>
        <td id="LC201" class="blob-code blob-code-inner js-file-line">                  <span class="pl-v">requirements</span><span class="pl-k">=</span><span class="pl-c1">dict</span>(<span class="pl-v">action</span><span class="pl-k">=</span><span class="pl-s"><span class="pl-pds">&#39;</span>|<span class="pl-pds">&#39;</span></span>.join([</td>
      </tr>
      <tr>
        <td id="L202" class="blob-num js-line-number" data-line-number="202"></td>
        <td id="LC202" class="blob-code blob-code-inner js-file-line">                      <span class="pl-s"><span class="pl-pds">&#39;</span>new_resource<span class="pl-pds">&#39;</span></span>,</td>
      </tr>
      <tr>
        <td id="L203" class="blob-num js-line-number" data-line-number="203"></td>
        <td id="LC203" class="blob-code blob-code-inner js-file-line">                      <span class="pl-s"><span class="pl-pds">&#39;</span>history<span class="pl-pds">&#39;</span></span>,</td>
      </tr>
      <tr>
        <td id="L204" class="blob-num js-line-number" data-line-number="204"></td>
        <td id="LC204" class="blob-code blob-code-inner js-file-line">                      <span class="pl-s"><span class="pl-pds">&#39;</span>read_ajax<span class="pl-pds">&#39;</span></span>,</td>
      </tr>
      <tr>
        <td id="L205" class="blob-num js-line-number" data-line-number="205"></td>
        <td id="LC205" class="blob-code blob-code-inner js-file-line">                      <span class="pl-s"><span class="pl-pds">&#39;</span>history_ajax<span class="pl-pds">&#39;</span></span>,</td>
      </tr>
      <tr>
        <td id="L206" class="blob-num js-line-number" data-line-number="206"></td>
        <td id="LC206" class="blob-code blob-code-inner js-file-line">                      <span class="pl-s"><span class="pl-pds">&#39;</span>follow<span class="pl-pds">&#39;</span></span>,</td>
      </tr>
      <tr>
        <td id="L207" class="blob-num js-line-number" data-line-number="207"></td>
        <td id="LC207" class="blob-code blob-code-inner js-file-line">                      <span class="pl-s"><span class="pl-pds">&#39;</span>activity<span class="pl-pds">&#39;</span></span>,</td>
      </tr>
      <tr>
        <td id="L208" class="blob-num js-line-number" data-line-number="208"></td>
        <td id="LC208" class="blob-code blob-code-inner js-file-line">                      <span class="pl-s"><span class="pl-pds">&#39;</span>groups<span class="pl-pds">&#39;</span></span>,</td>
      </tr>
      <tr>
        <td id="L209" class="blob-num js-line-number" data-line-number="209"></td>
        <td id="LC209" class="blob-code blob-code-inner js-file-line">                      <span class="pl-s"><span class="pl-pds">&#39;</span>unfollow<span class="pl-pds">&#39;</span></span>,</td>
      </tr>
      <tr>
        <td id="L210" class="blob-num js-line-number" data-line-number="210"></td>
        <td id="LC210" class="blob-code blob-code-inner js-file-line">                      <span class="pl-s"><span class="pl-pds">&#39;</span>delete<span class="pl-pds">&#39;</span></span>,</td>
      </tr>
      <tr>
        <td id="L211" class="blob-num js-line-number" data-line-number="211"></td>
        <td id="LC211" class="blob-code blob-code-inner js-file-line">                      <span class="pl-s"><span class="pl-pds">&#39;</span>api_data<span class="pl-pds">&#39;</span></span>,</td>
      </tr>
      <tr>
        <td id="L212" class="blob-num js-line-number" data-line-number="212"></td>
        <td id="LC212" class="blob-code blob-code-inner js-file-line">                  ])))</td>
      </tr>
      <tr>
        <td id="L213" class="blob-num js-line-number" data-line-number="213"></td>
        <td id="LC213" class="blob-code blob-code-inner js-file-line">        m.connect(<span class="pl-s"><span class="pl-pds">&#39;</span>dataset_edit<span class="pl-pds">&#39;</span></span>, <span class="pl-s"><span class="pl-pds">&#39;</span>/dataset/edit/<span class="pl-c1">{id}</span><span class="pl-pds">&#39;</span></span>, <span class="pl-v">action</span><span class="pl-k">=</span><span class="pl-s"><span class="pl-pds">&#39;</span>edit<span class="pl-pds">&#39;</span></span>,</td>
      </tr>
      <tr>
        <td id="L214" class="blob-num js-line-number" data-line-number="214"></td>
        <td id="LC214" class="blob-code blob-code-inner js-file-line">                  <span class="pl-v">ckan_icon</span><span class="pl-k">=</span><span class="pl-s"><span class="pl-pds">&#39;</span>pencil-square-o<span class="pl-pds">&#39;</span></span>)</td>
      </tr>
      <tr>
        <td id="L215" class="blob-num js-line-number" data-line-number="215"></td>
        <td id="LC215" class="blob-code blob-code-inner js-file-line">        m.connect(<span class="pl-s"><span class="pl-pds">&#39;</span>dataset_followers<span class="pl-pds">&#39;</span></span>, <span class="pl-s"><span class="pl-pds">&#39;</span>/dataset/followers/<span class="pl-c1">{id}</span><span class="pl-pds">&#39;</span></span>,</td>
      </tr>
      <tr>
        <td id="L216" class="blob-num js-line-number" data-line-number="216"></td>
        <td id="LC216" class="blob-code blob-code-inner js-file-line">                  <span class="pl-v">action</span><span class="pl-k">=</span><span class="pl-s"><span class="pl-pds">&#39;</span>followers<span class="pl-pds">&#39;</span></span>, <span class="pl-v">ckan_icon</span><span class="pl-k">=</span><span class="pl-s"><span class="pl-pds">&#39;</span>users<span class="pl-pds">&#39;</span></span>)</td>
      </tr>
      <tr>
        <td id="L217" class="blob-num js-line-number" data-line-number="217"></td>
        <td id="LC217" class="blob-code blob-code-inner js-file-line">        m.connect(<span class="pl-s"><span class="pl-pds">&#39;</span>dataset_activity<span class="pl-pds">&#39;</span></span>, <span class="pl-s"><span class="pl-pds">&#39;</span>/dataset/activity/<span class="pl-c1">{id}</span><span class="pl-pds">&#39;</span></span>,</td>
      </tr>
      <tr>
        <td id="L218" class="blob-num js-line-number" data-line-number="218"></td>
        <td id="LC218" class="blob-code blob-code-inner js-file-line">                  <span class="pl-v">action</span><span class="pl-k">=</span><span class="pl-s"><span class="pl-pds">&#39;</span>activity<span class="pl-pds">&#39;</span></span>, <span class="pl-v">ckan_icon</span><span class="pl-k">=</span><span class="pl-s"><span class="pl-pds">&#39;</span>clock-o<span class="pl-pds">&#39;</span></span>)</td>
      </tr>
      <tr>
        <td id="L219" class="blob-num js-line-number" data-line-number="219"></td>
        <td id="LC219" class="blob-code blob-code-inner js-file-line">        m.connect(<span class="pl-s"><span class="pl-pds">&#39;</span>/dataset/activity/<span class="pl-c1">{id}</span>/<span class="pl-c1">{offset}</span><span class="pl-pds">&#39;</span></span>, <span class="pl-v">action</span><span class="pl-k">=</span><span class="pl-s"><span class="pl-pds">&#39;</span>activity<span class="pl-pds">&#39;</span></span>)</td>
      </tr>
      <tr>
        <td id="L220" class="blob-num js-line-number" data-line-number="220"></td>
        <td id="LC220" class="blob-code blob-code-inner js-file-line">        m.connect(<span class="pl-s"><span class="pl-pds">&#39;</span>dataset_groups<span class="pl-pds">&#39;</span></span>, <span class="pl-s"><span class="pl-pds">&#39;</span>/dataset/groups/<span class="pl-c1">{id}</span><span class="pl-pds">&#39;</span></span>,</td>
      </tr>
      <tr>
        <td id="L221" class="blob-num js-line-number" data-line-number="221"></td>
        <td id="LC221" class="blob-code blob-code-inner js-file-line">                  <span class="pl-v">action</span><span class="pl-k">=</span><span class="pl-s"><span class="pl-pds">&#39;</span>groups<span class="pl-pds">&#39;</span></span>, <span class="pl-v">ckan_icon</span><span class="pl-k">=</span><span class="pl-s"><span class="pl-pds">&#39;</span>users<span class="pl-pds">&#39;</span></span>)</td>
      </tr>
      <tr>
        <td id="L222" class="blob-num js-line-number" data-line-number="222"></td>
        <td id="LC222" class="blob-code blob-code-inner js-file-line">        m.connect(<span class="pl-s"><span class="pl-pds">&#39;</span>dataset_resources<span class="pl-pds">&#39;</span></span>, <span class="pl-s"><span class="pl-pds">&#39;</span>/dataset/resources/<span class="pl-c1">{id}</span><span class="pl-pds">&#39;</span></span>,</td>
      </tr>
      <tr>
        <td id="L223" class="blob-num js-line-number" data-line-number="223"></td>
        <td id="LC223" class="blob-code blob-code-inner js-file-line">                  <span class="pl-v">action</span><span class="pl-k">=</span><span class="pl-s"><span class="pl-pds">&#39;</span>resources<span class="pl-pds">&#39;</span></span>, <span class="pl-v">ckan_icon</span><span class="pl-k">=</span><span class="pl-s"><span class="pl-pds">&#39;</span>bars<span class="pl-pds">&#39;</span></span>)</td>
      </tr>
      <tr>
        <td id="L224" class="blob-num js-line-number" data-line-number="224"></td>
        <td id="LC224" class="blob-code blob-code-inner js-file-line">        m.connect(<span class="pl-s"><span class="pl-pds">&#39;</span>dataset_read<span class="pl-pds">&#39;</span></span>, <span class="pl-s"><span class="pl-pds">&#39;</span>/dataset/<span class="pl-c1">{id}</span><span class="pl-pds">&#39;</span></span>, <span class="pl-v">action</span><span class="pl-k">=</span><span class="pl-s"><span class="pl-pds">&#39;</span>read<span class="pl-pds">&#39;</span></span>,</td>
      </tr>
      <tr>
        <td id="L225" class="blob-num js-line-number" data-line-number="225"></td>
        <td id="LC225" class="blob-code blob-code-inner js-file-line">                  <span class="pl-v">ckan_icon</span><span class="pl-k">=</span><span class="pl-s"><span class="pl-pds">&#39;</span>sitemap<span class="pl-pds">&#39;</span></span>)</td>
      </tr>
      <tr>
        <td id="L226" class="blob-num js-line-number" data-line-number="226"></td>
        <td id="LC226" class="blob-code blob-code-inner js-file-line">        m.connect(<span class="pl-s"><span class="pl-pds">&#39;</span>/dataset/<span class="pl-c1">{id}</span>/resource/<span class="pl-c1">{resource_id}</span><span class="pl-pds">&#39;</span></span>,</td>
      </tr>
      <tr>
        <td id="L227" class="blob-num js-line-number" data-line-number="227"></td>
        <td id="LC227" class="blob-code blob-code-inner js-file-line">                  <span class="pl-v">action</span><span class="pl-k">=</span><span class="pl-s"><span class="pl-pds">&#39;</span>resource_read<span class="pl-pds">&#39;</span></span>)</td>
      </tr>
      <tr>
        <td id="L228" class="blob-num js-line-number" data-line-number="228"></td>
        <td id="LC228" class="blob-code blob-code-inner js-file-line">        m.connect(<span class="pl-s"><span class="pl-pds">&#39;</span>/dataset/<span class="pl-c1">{id}</span>/resource_delete/<span class="pl-c1">{resource_id}</span><span class="pl-pds">&#39;</span></span>,</td>
      </tr>
      <tr>
        <td id="L229" class="blob-num js-line-number" data-line-number="229"></td>
        <td id="LC229" class="blob-code blob-code-inner js-file-line">                  <span class="pl-v">action</span><span class="pl-k">=</span><span class="pl-s"><span class="pl-pds">&#39;</span>resource_delete<span class="pl-pds">&#39;</span></span>)</td>
      </tr>
      <tr>
        <td id="L230" class="blob-num js-line-number" data-line-number="230"></td>
        <td id="LC230" class="blob-code blob-code-inner js-file-line">        m.connect(<span class="pl-s"><span class="pl-pds">&#39;</span>resource_edit<span class="pl-pds">&#39;</span></span>, <span class="pl-s"><span class="pl-pds">&#39;</span>/dataset/<span class="pl-c1">{id}</span>/resource_edit/<span class="pl-c1">{resource_id}</span><span class="pl-pds">&#39;</span></span>,</td>
      </tr>
      <tr>
        <td id="L231" class="blob-num js-line-number" data-line-number="231"></td>
        <td id="LC231" class="blob-code blob-code-inner js-file-line">                  <span class="pl-v">action</span><span class="pl-k">=</span><span class="pl-s"><span class="pl-pds">&#39;</span>resource_edit<span class="pl-pds">&#39;</span></span>, <span class="pl-v">ckan_icon</span><span class="pl-k">=</span><span class="pl-s"><span class="pl-pds">&#39;</span>pencil-square-o<span class="pl-pds">&#39;</span></span>)</td>
      </tr>
      <tr>
        <td id="L232" class="blob-num js-line-number" data-line-number="232"></td>
        <td id="LC232" class="blob-code blob-code-inner js-file-line">        m.connect(<span class="pl-s"><span class="pl-pds">&#39;</span>/dataset/<span class="pl-c1">{id}</span>/resource/<span class="pl-c1">{resource_id}</span>/download<span class="pl-pds">&#39;</span></span>,</td>
      </tr>
      <tr>
        <td id="L233" class="blob-num js-line-number" data-line-number="233"></td>
        <td id="LC233" class="blob-code blob-code-inner js-file-line">                  <span class="pl-v">action</span><span class="pl-k">=</span><span class="pl-s"><span class="pl-pds">&#39;</span>resource_download<span class="pl-pds">&#39;</span></span>)</td>
      </tr>
      <tr>
        <td id="L234" class="blob-num js-line-number" data-line-number="234"></td>
        <td id="LC234" class="blob-code blob-code-inner js-file-line">        m.connect(<span class="pl-s"><span class="pl-pds">&#39;</span>/dataset/<span class="pl-c1">{id}</span>/resource/<span class="pl-c1">{resource_id}</span>/download/<span class="pl-c1">{filename}</span><span class="pl-pds">&#39;</span></span>,</td>
      </tr>
      <tr>
        <td id="L235" class="blob-num js-line-number" data-line-number="235"></td>
        <td id="LC235" class="blob-code blob-code-inner js-file-line">                  <span class="pl-v">action</span><span class="pl-k">=</span><span class="pl-s"><span class="pl-pds">&#39;</span>resource_download<span class="pl-pds">&#39;</span></span>)</td>
      </tr>
      <tr>
        <td id="L236" class="blob-num js-line-number" data-line-number="236"></td>
        <td id="LC236" class="blob-code blob-code-inner js-file-line">        m.connect(<span class="pl-s"><span class="pl-pds">&#39;</span>/dataset/<span class="pl-c1">{id}</span>/resource/<span class="pl-c1">{resource_id}</span>/embed<span class="pl-pds">&#39;</span></span>,</td>
      </tr>
      <tr>
        <td id="L237" class="blob-num js-line-number" data-line-number="237"></td>
        <td id="LC237" class="blob-code blob-code-inner js-file-line">                  <span class="pl-v">action</span><span class="pl-k">=</span><span class="pl-s"><span class="pl-pds">&#39;</span>resource_embedded_dataviewer<span class="pl-pds">&#39;</span></span>)</td>
      </tr>
      <tr>
        <td id="L238" class="blob-num js-line-number" data-line-number="238"></td>
        <td id="LC238" class="blob-code blob-code-inner js-file-line">        m.connect(<span class="pl-s"><span class="pl-pds">&#39;</span>/dataset/<span class="pl-c1">{id}</span>/resource/<span class="pl-c1">{resource_id}</span>/viewer<span class="pl-pds">&#39;</span></span>,</td>
      </tr>
      <tr>
        <td id="L239" class="blob-num js-line-number" data-line-number="239"></td>
        <td id="LC239" class="blob-code blob-code-inner js-file-line">                  <span class="pl-v">action</span><span class="pl-k">=</span><span class="pl-s"><span class="pl-pds">&#39;</span>resource_embedded_dataviewer<span class="pl-pds">&#39;</span></span>, <span class="pl-v">width</span><span class="pl-k">=</span><span class="pl-s"><span class="pl-pds">&quot;</span>960<span class="pl-pds">&quot;</span></span>,</td>
      </tr>
      <tr>
        <td id="L240" class="blob-num js-line-number" data-line-number="240"></td>
        <td id="LC240" class="blob-code blob-code-inner js-file-line">                  <span class="pl-v">height</span><span class="pl-k">=</span><span class="pl-s"><span class="pl-pds">&quot;</span>800<span class="pl-pds">&quot;</span></span>)</td>
      </tr>
      <tr>
        <td id="L241" class="blob-num js-line-number" data-line-number="241"></td>
        <td id="LC241" class="blob-code blob-code-inner js-file-line">        m.connect(<span class="pl-s"><span class="pl-pds">&#39;</span>/dataset/<span class="pl-c1">{id}</span>/resource/<span class="pl-c1">{resource_id}</span>/preview<span class="pl-pds">&#39;</span></span>,</td>
      </tr>
      <tr>
        <td id="L242" class="blob-num js-line-number" data-line-number="242"></td>
        <td id="LC242" class="blob-code blob-code-inner js-file-line">                  <span class="pl-v">action</span><span class="pl-k">=</span><span class="pl-s"><span class="pl-pds">&#39;</span>resource_datapreview<span class="pl-pds">&#39;</span></span>)</td>
      </tr>
      <tr>
        <td id="L243" class="blob-num js-line-number" data-line-number="243"></td>
        <td id="LC243" class="blob-code blob-code-inner js-file-line">        m.connect(<span class="pl-s"><span class="pl-pds">&#39;</span>views<span class="pl-pds">&#39;</span></span>, <span class="pl-s"><span class="pl-pds">&#39;</span>/dataset/<span class="pl-c1">{id}</span>/resource/<span class="pl-c1">{resource_id}</span>/views<span class="pl-pds">&#39;</span></span>,</td>
      </tr>
      <tr>
        <td id="L244" class="blob-num js-line-number" data-line-number="244"></td>
        <td id="LC244" class="blob-code blob-code-inner js-file-line">                  <span class="pl-v">action</span><span class="pl-k">=</span><span class="pl-s"><span class="pl-pds">&#39;</span>resource_views<span class="pl-pds">&#39;</span></span>, <span class="pl-v">ckan_icon</span><span class="pl-k">=</span><span class="pl-s"><span class="pl-pds">&#39;</span>bars<span class="pl-pds">&#39;</span></span>)</td>
      </tr>
      <tr>
        <td id="L245" class="blob-num js-line-number" data-line-number="245"></td>
        <td id="LC245" class="blob-code blob-code-inner js-file-line">        m.connect(<span class="pl-s"><span class="pl-pds">&#39;</span>new_view<span class="pl-pds">&#39;</span></span>, <span class="pl-s"><span class="pl-pds">&#39;</span>/dataset/<span class="pl-c1">{id}</span>/resource/<span class="pl-c1">{resource_id}</span>/new_view<span class="pl-pds">&#39;</span></span>,</td>
      </tr>
      <tr>
        <td id="L246" class="blob-num js-line-number" data-line-number="246"></td>
        <td id="LC246" class="blob-code blob-code-inner js-file-line">                  <span class="pl-v">action</span><span class="pl-k">=</span><span class="pl-s"><span class="pl-pds">&#39;</span>edit_view<span class="pl-pds">&#39;</span></span>, <span class="pl-v">ckan_icon</span><span class="pl-k">=</span><span class="pl-s"><span class="pl-pds">&#39;</span>pencil-square-o<span class="pl-pds">&#39;</span></span>)</td>
      </tr>
      <tr>
        <td id="L247" class="blob-num js-line-number" data-line-number="247"></td>
        <td id="LC247" class="blob-code blob-code-inner js-file-line">        m.connect(<span class="pl-s"><span class="pl-pds">&#39;</span>edit_view<span class="pl-pds">&#39;</span></span>,</td>
      </tr>
      <tr>
        <td id="L248" class="blob-num js-line-number" data-line-number="248"></td>
        <td id="LC248" class="blob-code blob-code-inner js-file-line">                  <span class="pl-s"><span class="pl-pds">&#39;</span>/dataset/<span class="pl-c1">{id}</span>/resource/<span class="pl-c1">{resource_id}</span>/edit_view/<span class="pl-c1">{view_id}</span><span class="pl-pds">&#39;</span></span>,</td>
      </tr>
      <tr>
        <td id="L249" class="blob-num js-line-number" data-line-number="249"></td>
        <td id="LC249" class="blob-code blob-code-inner js-file-line">                  <span class="pl-v">action</span><span class="pl-k">=</span><span class="pl-s"><span class="pl-pds">&#39;</span>edit_view<span class="pl-pds">&#39;</span></span>, <span class="pl-v">ckan_icon</span><span class="pl-k">=</span><span class="pl-s"><span class="pl-pds">&#39;</span>pencil-square-o<span class="pl-pds">&#39;</span></span>)</td>
      </tr>
      <tr>
        <td id="L250" class="blob-num js-line-number" data-line-number="250"></td>
        <td id="LC250" class="blob-code blob-code-inner js-file-line">        m.connect(<span class="pl-s"><span class="pl-pds">&#39;</span>resource_view<span class="pl-pds">&#39;</span></span>,</td>
      </tr>
      <tr>
        <td id="L251" class="blob-num js-line-number" data-line-number="251"></td>
        <td id="LC251" class="blob-code blob-code-inner js-file-line">                  <span class="pl-s"><span class="pl-pds">&#39;</span>/dataset/<span class="pl-c1">{id}</span>/resource/<span class="pl-c1">{resource_id}</span>/view/<span class="pl-c1">{view_id}</span><span class="pl-pds">&#39;</span></span>,</td>
      </tr>
      <tr>
        <td id="L252" class="blob-num js-line-number" data-line-number="252"></td>
        <td id="LC252" class="blob-code blob-code-inner js-file-line">                  <span class="pl-v">action</span><span class="pl-k">=</span><span class="pl-s"><span class="pl-pds">&#39;</span>resource_view<span class="pl-pds">&#39;</span></span>)</td>
      </tr>
      <tr>
        <td id="L253" class="blob-num js-line-number" data-line-number="253"></td>
        <td id="LC253" class="blob-code blob-code-inner js-file-line">        m.connect(<span class="pl-s"><span class="pl-pds">&#39;</span>/dataset/<span class="pl-c1">{id}</span>/resource/<span class="pl-c1">{resource_id}</span>/view/<span class="pl-pds">&#39;</span></span>,</td>
      </tr>
      <tr>
        <td id="L254" class="blob-num js-line-number" data-line-number="254"></td>
        <td id="LC254" class="blob-code blob-code-inner js-file-line">                  <span class="pl-v">action</span><span class="pl-k">=</span><span class="pl-s"><span class="pl-pds">&#39;</span>resource_view<span class="pl-pds">&#39;</span></span>)</td>
      </tr>
      <tr>
        <td id="L255" class="blob-num js-line-number" data-line-number="255"></td>
        <td id="LC255" class="blob-code blob-code-inner js-file-line">
</td>
      </tr>
      <tr>
        <td id="L256" class="blob-num js-line-number" data-line-number="256"></td>
        <td id="LC256" class="blob-code blob-code-inner js-file-line">    <span class="pl-c"><span class="pl-c">#</span> group</span></td>
      </tr>
      <tr>
        <td id="L257" class="blob-num js-line-number" data-line-number="257"></td>
        <td id="LC257" class="blob-code blob-code-inner js-file-line">    <span class="pl-c1">map</span>.redirect(<span class="pl-s"><span class="pl-pds">&#39;</span>/groups<span class="pl-pds">&#39;</span></span>, <span class="pl-s"><span class="pl-pds">&#39;</span>/group<span class="pl-pds">&#39;</span></span>)</td>
      </tr>
      <tr>
        <td id="L258" class="blob-num js-line-number" data-line-number="258"></td>
        <td id="LC258" class="blob-code blob-code-inner js-file-line">    <span class="pl-c1">map</span>.redirect(<span class="pl-s"><span class="pl-pds">&#39;</span>/groups/<span class="pl-c1">{url<span class="pl-k">:</span>.*}</span><span class="pl-pds">&#39;</span></span>, <span class="pl-s"><span class="pl-pds">&#39;</span>/group/<span class="pl-c1">{url}</span><span class="pl-pds">&#39;</span></span>)</td>
      </tr>
      <tr>
        <td id="L259" class="blob-num js-line-number" data-line-number="259"></td>
        <td id="LC259" class="blob-code blob-code-inner js-file-line">
</td>
      </tr>
      <tr>
        <td id="L260" class="blob-num js-line-number" data-line-number="260"></td>
        <td id="LC260" class="blob-code blob-code-inner js-file-line">    <span class="pl-c"><span class="pl-c">#</span> These named routes are used for custom group forms which will use the</span></td>
      </tr>
      <tr>
        <td id="L261" class="blob-num js-line-number" data-line-number="261"></td>
        <td id="LC261" class="blob-code blob-code-inner js-file-line">    <span class="pl-c"><span class="pl-c">#</span> names below based on the group.type (&#39;group&#39; is the default type)</span></td>
      </tr>
      <tr>
        <td id="L262" class="blob-num js-line-number" data-line-number="262"></td>
        <td id="LC262" class="blob-code blob-code-inner js-file-line">    <span class="pl-k">with</span> SubMapper(<span class="pl-c1">map</span>, <span class="pl-v">controller</span><span class="pl-k">=</span><span class="pl-s"><span class="pl-pds">&#39;</span>group<span class="pl-pds">&#39;</span></span>) <span class="pl-k">as</span> m:</td>
      </tr>
      <tr>
        <td id="L263" class="blob-num js-line-number" data-line-number="263"></td>
        <td id="LC263" class="blob-code blob-code-inner js-file-line">        m.connect(<span class="pl-s"><span class="pl-pds">&#39;</span>group_index<span class="pl-pds">&#39;</span></span>, <span class="pl-s"><span class="pl-pds">&#39;</span>/group<span class="pl-pds">&#39;</span></span>, <span class="pl-v">action</span><span class="pl-k">=</span><span class="pl-s"><span class="pl-pds">&#39;</span>index<span class="pl-pds">&#39;</span></span>,</td>
      </tr>
      <tr>
        <td id="L264" class="blob-num js-line-number" data-line-number="264"></td>
        <td id="LC264" class="blob-code blob-code-inner js-file-line">                  <span class="pl-v">highlight_actions</span><span class="pl-k">=</span><span class="pl-s"><span class="pl-pds">&#39;</span>index search<span class="pl-pds">&#39;</span></span>)</td>
      </tr>
      <tr>
        <td id="L265" class="blob-num js-line-number" data-line-number="265"></td>
        <td id="LC265" class="blob-code blob-code-inner js-file-line">        m.connect(<span class="pl-s"><span class="pl-pds">&#39;</span>group_list<span class="pl-pds">&#39;</span></span>, <span class="pl-s"><span class="pl-pds">&#39;</span>/group/list<span class="pl-pds">&#39;</span></span>, <span class="pl-v">action</span><span class="pl-k">=</span><span class="pl-s"><span class="pl-pds">&#39;</span>list<span class="pl-pds">&#39;</span></span>)</td>
      </tr>
      <tr>
        <td id="L266" class="blob-num js-line-number" data-line-number="266"></td>
        <td id="LC266" class="blob-code blob-code-inner js-file-line">        m.connect(<span class="pl-s"><span class="pl-pds">&#39;</span>group_new<span class="pl-pds">&#39;</span></span>, <span class="pl-s"><span class="pl-pds">&#39;</span>/group/new<span class="pl-pds">&#39;</span></span>, <span class="pl-v">action</span><span class="pl-k">=</span><span class="pl-s"><span class="pl-pds">&#39;</span>new<span class="pl-pds">&#39;</span></span>)</td>
      </tr>
      <tr>
        <td id="L267" class="blob-num js-line-number" data-line-number="267"></td>
        <td id="LC267" class="blob-code blob-code-inner js-file-line">        m.connect(<span class="pl-s"><span class="pl-pds">&#39;</span>group_action<span class="pl-pds">&#39;</span></span>, <span class="pl-s"><span class="pl-pds">&#39;</span>/group/<span class="pl-c1">{action}</span>/<span class="pl-c1">{id}</span><span class="pl-pds">&#39;</span></span>,</td>
      </tr>
      <tr>
        <td id="L268" class="blob-num js-line-number" data-line-number="268"></td>
        <td id="LC268" class="blob-code blob-code-inner js-file-line">                  <span class="pl-v">requirements</span><span class="pl-k">=</span><span class="pl-c1">dict</span>(<span class="pl-v">action</span><span class="pl-k">=</span><span class="pl-s"><span class="pl-pds">&#39;</span>|<span class="pl-pds">&#39;</span></span>.join([</td>
      </tr>
      <tr>
        <td id="L269" class="blob-num js-line-number" data-line-number="269"></td>
        <td id="LC269" class="blob-code blob-code-inner js-file-line">                      <span class="pl-s"><span class="pl-pds">&#39;</span>edit<span class="pl-pds">&#39;</span></span>,</td>
      </tr>
      <tr>
        <td id="L270" class="blob-num js-line-number" data-line-number="270"></td>
        <td id="LC270" class="blob-code blob-code-inner js-file-line">                      <span class="pl-s"><span class="pl-pds">&#39;</span>delete<span class="pl-pds">&#39;</span></span>,</td>
      </tr>
      <tr>
        <td id="L271" class="blob-num js-line-number" data-line-number="271"></td>
        <td id="LC271" class="blob-code blob-code-inner js-file-line">                      <span class="pl-s"><span class="pl-pds">&#39;</span>member_new<span class="pl-pds">&#39;</span></span>,</td>
      </tr>
      <tr>
        <td id="L272" class="blob-num js-line-number" data-line-number="272"></td>
        <td id="LC272" class="blob-code blob-code-inner js-file-line">                      <span class="pl-s"><span class="pl-pds">&#39;</span>member_delete<span class="pl-pds">&#39;</span></span>,</td>
      </tr>
      <tr>
        <td id="L273" class="blob-num js-line-number" data-line-number="273"></td>
        <td id="LC273" class="blob-code blob-code-inner js-file-line">                      <span class="pl-s"><span class="pl-pds">&#39;</span>history<span class="pl-pds">&#39;</span></span>,</td>
      </tr>
      <tr>
        <td id="L274" class="blob-num js-line-number" data-line-number="274"></td>
        <td id="LC274" class="blob-code blob-code-inner js-file-line">                      <span class="pl-s"><span class="pl-pds">&#39;</span>followers<span class="pl-pds">&#39;</span></span>,</td>
      </tr>
      <tr>
        <td id="L275" class="blob-num js-line-number" data-line-number="275"></td>
        <td id="LC275" class="blob-code blob-code-inner js-file-line">                      <span class="pl-s"><span class="pl-pds">&#39;</span>follow<span class="pl-pds">&#39;</span></span>,</td>
      </tr>
      <tr>
        <td id="L276" class="blob-num js-line-number" data-line-number="276"></td>
        <td id="LC276" class="blob-code blob-code-inner js-file-line">                      <span class="pl-s"><span class="pl-pds">&#39;</span>unfollow<span class="pl-pds">&#39;</span></span>,</td>
      </tr>
      <tr>
        <td id="L277" class="blob-num js-line-number" data-line-number="277"></td>
        <td id="LC277" class="blob-code blob-code-inner js-file-line">                      <span class="pl-s"><span class="pl-pds">&#39;</span>admins<span class="pl-pds">&#39;</span></span>,</td>
      </tr>
      <tr>
        <td id="L278" class="blob-num js-line-number" data-line-number="278"></td>
        <td id="LC278" class="blob-code blob-code-inner js-file-line">                      <span class="pl-s"><span class="pl-pds">&#39;</span>activity<span class="pl-pds">&#39;</span></span>,</td>
      </tr>
      <tr>
        <td id="L279" class="blob-num js-line-number" data-line-number="279"></td>
        <td id="LC279" class="blob-code blob-code-inner js-file-line">                  ])))</td>
      </tr>
      <tr>
        <td id="L280" class="blob-num js-line-number" data-line-number="280"></td>
        <td id="LC280" class="blob-code blob-code-inner js-file-line">        m.connect(<span class="pl-s"><span class="pl-pds">&#39;</span>group_about<span class="pl-pds">&#39;</span></span>, <span class="pl-s"><span class="pl-pds">&#39;</span>/group/about/<span class="pl-c1">{id}</span><span class="pl-pds">&#39;</span></span>, <span class="pl-v">action</span><span class="pl-k">=</span><span class="pl-s"><span class="pl-pds">&#39;</span>about<span class="pl-pds">&#39;</span></span>,</td>
      </tr>
      <tr>
        <td id="L281" class="blob-num js-line-number" data-line-number="281"></td>
        <td id="LC281" class="blob-code blob-code-inner js-file-line">                  <span class="pl-v">ckan_icon</span><span class="pl-k">=</span><span class="pl-s"><span class="pl-pds">&#39;</span>info-circle<span class="pl-pds">&#39;</span></span>),</td>
      </tr>
      <tr>
        <td id="L282" class="blob-num js-line-number" data-line-number="282"></td>
        <td id="LC282" class="blob-code blob-code-inner js-file-line">        m.connect(<span class="pl-s"><span class="pl-pds">&#39;</span>group_edit<span class="pl-pds">&#39;</span></span>, <span class="pl-s"><span class="pl-pds">&#39;</span>/group/edit/<span class="pl-c1">{id}</span><span class="pl-pds">&#39;</span></span>, <span class="pl-v">action</span><span class="pl-k">=</span><span class="pl-s"><span class="pl-pds">&#39;</span>edit<span class="pl-pds">&#39;</span></span>,</td>
      </tr>
      <tr>
        <td id="L283" class="blob-num js-line-number" data-line-number="283"></td>
        <td id="LC283" class="blob-code blob-code-inner js-file-line">                  <span class="pl-v">ckan_icon</span><span class="pl-k">=</span><span class="pl-s"><span class="pl-pds">&#39;</span>pencil-square-o<span class="pl-pds">&#39;</span></span>)</td>
      </tr>
      <tr>
        <td id="L284" class="blob-num js-line-number" data-line-number="284"></td>
        <td id="LC284" class="blob-code blob-code-inner js-file-line">        m.connect(<span class="pl-s"><span class="pl-pds">&#39;</span>group_members<span class="pl-pds">&#39;</span></span>, <span class="pl-s"><span class="pl-pds">&#39;</span>/group/members/<span class="pl-c1">{id}</span><span class="pl-pds">&#39;</span></span>, <span class="pl-v">action</span><span class="pl-k">=</span><span class="pl-s"><span class="pl-pds">&#39;</span>members<span class="pl-pds">&#39;</span></span>,</td>
      </tr>
      <tr>
        <td id="L285" class="blob-num js-line-number" data-line-number="285"></td>
        <td id="LC285" class="blob-code blob-code-inner js-file-line">                  <span class="pl-v">ckan_icon</span><span class="pl-k">=</span><span class="pl-s"><span class="pl-pds">&#39;</span>users<span class="pl-pds">&#39;</span></span>),</td>
      </tr>
      <tr>
        <td id="L286" class="blob-num js-line-number" data-line-number="286"></td>
        <td id="LC286" class="blob-code blob-code-inner js-file-line">        m.connect(<span class="pl-s"><span class="pl-pds">&#39;</span>group_activity<span class="pl-pds">&#39;</span></span>, <span class="pl-s"><span class="pl-pds">&#39;</span>/group/activity/<span class="pl-c1">{id}</span>/<span class="pl-c1">{offset}</span><span class="pl-pds">&#39;</span></span>,</td>
      </tr>
      <tr>
        <td id="L287" class="blob-num js-line-number" data-line-number="287"></td>
        <td id="LC287" class="blob-code blob-code-inner js-file-line">                  <span class="pl-v">action</span><span class="pl-k">=</span><span class="pl-s"><span class="pl-pds">&#39;</span>activity<span class="pl-pds">&#39;</span></span>, <span class="pl-v">ckan_icon</span><span class="pl-k">=</span><span class="pl-s"><span class="pl-pds">&#39;</span>clock-o<span class="pl-pds">&#39;</span></span>),</td>
      </tr>
      <tr>
        <td id="L288" class="blob-num js-line-number" data-line-number="288"></td>
        <td id="LC288" class="blob-code blob-code-inner js-file-line">        m.connect(<span class="pl-s"><span class="pl-pds">&#39;</span>group_read<span class="pl-pds">&#39;</span></span>, <span class="pl-s"><span class="pl-pds">&#39;</span>/group/<span class="pl-c1">{id}</span><span class="pl-pds">&#39;</span></span>, <span class="pl-v">action</span><span class="pl-k">=</span><span class="pl-s"><span class="pl-pds">&#39;</span>read<span class="pl-pds">&#39;</span></span>,</td>
      </tr>
      <tr>
        <td id="L289" class="blob-num js-line-number" data-line-number="289"></td>
        <td id="LC289" class="blob-code blob-code-inner js-file-line">                  <span class="pl-v">ckan_icon</span><span class="pl-k">=</span><span class="pl-s"><span class="pl-pds">&#39;</span>sitemap<span class="pl-pds">&#39;</span></span>)</td>
      </tr>
      <tr>
        <td id="L290" class="blob-num js-line-number" data-line-number="290"></td>
        <td id="LC290" class="blob-code blob-code-inner js-file-line">
</td>
      </tr>
      <tr>
        <td id="L291" class="blob-num js-line-number" data-line-number="291"></td>
        <td id="LC291" class="blob-code blob-code-inner js-file-line">    <span class="pl-c"><span class="pl-c">#</span> organizations these basically end up being the same as groups</span></td>
      </tr>
      <tr>
        <td id="L292" class="blob-num js-line-number" data-line-number="292"></td>
        <td id="LC292" class="blob-code blob-code-inner js-file-line">    <span class="pl-k">with</span> SubMapper(<span class="pl-c1">map</span>, <span class="pl-v">controller</span><span class="pl-k">=</span><span class="pl-s"><span class="pl-pds">&#39;</span>organization<span class="pl-pds">&#39;</span></span>) <span class="pl-k">as</span> m:</td>
      </tr>
      <tr>
        <td id="L293" class="blob-num js-line-number" data-line-number="293"></td>
        <td id="LC293" class="blob-code blob-code-inner js-file-line">        m.connect(<span class="pl-s"><span class="pl-pds">&#39;</span>organizations_index<span class="pl-pds">&#39;</span></span>, <span class="pl-s"><span class="pl-pds">&#39;</span>/organization<span class="pl-pds">&#39;</span></span>, <span class="pl-v">action</span><span class="pl-k">=</span><span class="pl-s"><span class="pl-pds">&#39;</span>index<span class="pl-pds">&#39;</span></span>)</td>
      </tr>
      <tr>
        <td id="L294" class="blob-num js-line-number" data-line-number="294"></td>
        <td id="LC294" class="blob-code blob-code-inner js-file-line">        m.connect(<span class="pl-s"><span class="pl-pds">&#39;</span>/organization/list<span class="pl-pds">&#39;</span></span>, <span class="pl-v">action</span><span class="pl-k">=</span><span class="pl-s"><span class="pl-pds">&#39;</span>list<span class="pl-pds">&#39;</span></span>)</td>
      </tr>
      <tr>
        <td id="L295" class="blob-num js-line-number" data-line-number="295"></td>
        <td id="LC295" class="blob-code blob-code-inner js-file-line">        m.connect(<span class="pl-s"><span class="pl-pds">&#39;</span>/organization/new<span class="pl-pds">&#39;</span></span>, <span class="pl-v">action</span><span class="pl-k">=</span><span class="pl-s"><span class="pl-pds">&#39;</span>new<span class="pl-pds">&#39;</span></span>)</td>
      </tr>
      <tr>
        <td id="L296" class="blob-num js-line-number" data-line-number="296"></td>
        <td id="LC296" class="blob-code blob-code-inner js-file-line">        m.connect(<span class="pl-s"><span class="pl-pds">&#39;</span>/organization/<span class="pl-c1">{action}</span>/<span class="pl-c1">{id}</span><span class="pl-pds">&#39;</span></span>,</td>
      </tr>
      <tr>
        <td id="L297" class="blob-num js-line-number" data-line-number="297"></td>
        <td id="LC297" class="blob-code blob-code-inner js-file-line">                  <span class="pl-v">requirements</span><span class="pl-k">=</span><span class="pl-c1">dict</span>(<span class="pl-v">action</span><span class="pl-k">=</span><span class="pl-s"><span class="pl-pds">&#39;</span>|<span class="pl-pds">&#39;</span></span>.join([</td>
      </tr>
      <tr>
        <td id="L298" class="blob-num js-line-number" data-line-number="298"></td>
        <td id="LC298" class="blob-code blob-code-inner js-file-line">                      <span class="pl-s"><span class="pl-pds">&#39;</span>delete<span class="pl-pds">&#39;</span></span>,</td>
      </tr>
      <tr>
        <td id="L299" class="blob-num js-line-number" data-line-number="299"></td>
        <td id="LC299" class="blob-code blob-code-inner js-file-line">                      <span class="pl-s"><span class="pl-pds">&#39;</span>admins<span class="pl-pds">&#39;</span></span>,</td>
      </tr>
      <tr>
        <td id="L300" class="blob-num js-line-number" data-line-number="300"></td>
        <td id="LC300" class="blob-code blob-code-inner js-file-line">                      <span class="pl-s"><span class="pl-pds">&#39;</span>member_new<span class="pl-pds">&#39;</span></span>,</td>
      </tr>
      <tr>
        <td id="L301" class="blob-num js-line-number" data-line-number="301"></td>
        <td id="LC301" class="blob-code blob-code-inner js-file-line">                      <span class="pl-s"><span class="pl-pds">&#39;</span>member_delete<span class="pl-pds">&#39;</span></span>,</td>
      </tr>
      <tr>
        <td id="L302" class="blob-num js-line-number" data-line-number="302"></td>
        <td id="LC302" class="blob-code blob-code-inner js-file-line">                      <span class="pl-s"><span class="pl-pds">&#39;</span>history<span class="pl-pds">&#39;</span></span></td>
      </tr>
      <tr>
        <td id="L303" class="blob-num js-line-number" data-line-number="303"></td>
        <td id="LC303" class="blob-code blob-code-inner js-file-line">                  ])))</td>
      </tr>
      <tr>
        <td id="L304" class="blob-num js-line-number" data-line-number="304"></td>
        <td id="LC304" class="blob-code blob-code-inner js-file-line">        m.connect(<span class="pl-s"><span class="pl-pds">&#39;</span>organization_activity<span class="pl-pds">&#39;</span></span>, <span class="pl-s"><span class="pl-pds">&#39;</span>/organization/activity/<span class="pl-c1">{id}</span>/<span class="pl-c1">{offset}</span><span class="pl-pds">&#39;</span></span>,</td>
      </tr>
      <tr>
        <td id="L305" class="blob-num js-line-number" data-line-number="305"></td>
        <td id="LC305" class="blob-code blob-code-inner js-file-line">                  <span class="pl-v">action</span><span class="pl-k">=</span><span class="pl-s"><span class="pl-pds">&#39;</span>activity<span class="pl-pds">&#39;</span></span>, <span class="pl-v">ckan_icon</span><span class="pl-k">=</span><span class="pl-s"><span class="pl-pds">&#39;</span>clock-o<span class="pl-pds">&#39;</span></span>)</td>
      </tr>
      <tr>
        <td id="L306" class="blob-num js-line-number" data-line-number="306"></td>
        <td id="LC306" class="blob-code blob-code-inner js-file-line">        m.connect(<span class="pl-s"><span class="pl-pds">&#39;</span>organization_read<span class="pl-pds">&#39;</span></span>, <span class="pl-s"><span class="pl-pds">&#39;</span>/organization/<span class="pl-c1">{id}</span><span class="pl-pds">&#39;</span></span>, <span class="pl-v">action</span><span class="pl-k">=</span><span class="pl-s"><span class="pl-pds">&#39;</span>read<span class="pl-pds">&#39;</span></span>)</td>
      </tr>
      <tr>
        <td id="L307" class="blob-num js-line-number" data-line-number="307"></td>
        <td id="LC307" class="blob-code blob-code-inner js-file-line">        m.connect(<span class="pl-s"><span class="pl-pds">&#39;</span>organization_about<span class="pl-pds">&#39;</span></span>, <span class="pl-s"><span class="pl-pds">&#39;</span>/organization/about/<span class="pl-c1">{id}</span><span class="pl-pds">&#39;</span></span>,</td>
      </tr>
      <tr>
        <td id="L308" class="blob-num js-line-number" data-line-number="308"></td>
        <td id="LC308" class="blob-code blob-code-inner js-file-line">                  <span class="pl-v">action</span><span class="pl-k">=</span><span class="pl-s"><span class="pl-pds">&#39;</span>about<span class="pl-pds">&#39;</span></span>, <span class="pl-v">ckan_icon</span><span class="pl-k">=</span><span class="pl-s"><span class="pl-pds">&#39;</span>info-circle<span class="pl-pds">&#39;</span></span>)</td>
      </tr>
      <tr>
        <td id="L309" class="blob-num js-line-number" data-line-number="309"></td>
        <td id="LC309" class="blob-code blob-code-inner js-file-line">        m.connect(<span class="pl-s"><span class="pl-pds">&#39;</span>organization_read<span class="pl-pds">&#39;</span></span>, <span class="pl-s"><span class="pl-pds">&#39;</span>/organization/<span class="pl-c1">{id}</span><span class="pl-pds">&#39;</span></span>, <span class="pl-v">action</span><span class="pl-k">=</span><span class="pl-s"><span class="pl-pds">&#39;</span>read<span class="pl-pds">&#39;</span></span>,</td>
      </tr>
      <tr>
        <td id="L310" class="blob-num js-line-number" data-line-number="310"></td>
        <td id="LC310" class="blob-code blob-code-inner js-file-line">                  <span class="pl-v">ckan_icon</span><span class="pl-k">=</span><span class="pl-s"><span class="pl-pds">&#39;</span>sitemap<span class="pl-pds">&#39;</span></span>)</td>
      </tr>
      <tr>
        <td id="L311" class="blob-num js-line-number" data-line-number="311"></td>
        <td id="LC311" class="blob-code blob-code-inner js-file-line">        m.connect(<span class="pl-s"><span class="pl-pds">&#39;</span>organization_edit<span class="pl-pds">&#39;</span></span>, <span class="pl-s"><span class="pl-pds">&#39;</span>/organization/edit/<span class="pl-c1">{id}</span><span class="pl-pds">&#39;</span></span>,</td>
      </tr>
      <tr>
        <td id="L312" class="blob-num js-line-number" data-line-number="312"></td>
        <td id="LC312" class="blob-code blob-code-inner js-file-line">                  <span class="pl-v">action</span><span class="pl-k">=</span><span class="pl-s"><span class="pl-pds">&#39;</span>edit<span class="pl-pds">&#39;</span></span>, <span class="pl-v">ckan_icon</span><span class="pl-k">=</span><span class="pl-s"><span class="pl-pds">&#39;</span>pencil-square-o<span class="pl-pds">&#39;</span></span>)</td>
      </tr>
      <tr>
        <td id="L313" class="blob-num js-line-number" data-line-number="313"></td>
        <td id="LC313" class="blob-code blob-code-inner js-file-line">        m.connect(<span class="pl-s"><span class="pl-pds">&#39;</span>organization_members<span class="pl-pds">&#39;</span></span>, <span class="pl-s"><span class="pl-pds">&#39;</span>/organization/members/<span class="pl-c1">{id}</span><span class="pl-pds">&#39;</span></span>,</td>
      </tr>
      <tr>
        <td id="L314" class="blob-num js-line-number" data-line-number="314"></td>
        <td id="LC314" class="blob-code blob-code-inner js-file-line">                  <span class="pl-v">action</span><span class="pl-k">=</span><span class="pl-s"><span class="pl-pds">&#39;</span>members<span class="pl-pds">&#39;</span></span>, <span class="pl-v">ckan_icon</span><span class="pl-k">=</span><span class="pl-s"><span class="pl-pds">&#39;</span>users<span class="pl-pds">&#39;</span></span>)</td>
      </tr>
      <tr>
        <td id="L315" class="blob-num js-line-number" data-line-number="315"></td>
        <td id="LC315" class="blob-code blob-code-inner js-file-line">        m.connect(<span class="pl-s"><span class="pl-pds">&#39;</span>organization_bulk_process<span class="pl-pds">&#39;</span></span>,</td>
      </tr>
      <tr>
        <td id="L316" class="blob-num js-line-number" data-line-number="316"></td>
        <td id="LC316" class="blob-code blob-code-inner js-file-line">                  <span class="pl-s"><span class="pl-pds">&#39;</span>/organization/bulk_process/<span class="pl-c1">{id}</span><span class="pl-pds">&#39;</span></span>,</td>
      </tr>
      <tr>
        <td id="L317" class="blob-num js-line-number" data-line-number="317"></td>
        <td id="LC317" class="blob-code blob-code-inner js-file-line">                  <span class="pl-v">action</span><span class="pl-k">=</span><span class="pl-s"><span class="pl-pds">&#39;</span>bulk_process<span class="pl-pds">&#39;</span></span>, <span class="pl-v">ckan_icon</span><span class="pl-k">=</span><span class="pl-s"><span class="pl-pds">&#39;</span>sitemap<span class="pl-pds">&#39;</span></span>)</td>
      </tr>
      <tr>
        <td id="L318" class="blob-num js-line-number" data-line-number="318"></td>
        <td id="LC318" class="blob-code blob-code-inner js-file-line">    lib_plugins.register_package_plugins(<span class="pl-c1">map</span>)</td>
      </tr>
      <tr>
        <td id="L319" class="blob-num js-line-number" data-line-number="319"></td>
        <td id="LC319" class="blob-code blob-code-inner js-file-line">    lib_plugins.register_group_plugins(<span class="pl-c1">map</span>)</td>
      </tr>
      <tr>
        <td id="L320" class="blob-num js-line-number" data-line-number="320"></td>
        <td id="LC320" class="blob-code blob-code-inner js-file-line">
</td>
      </tr>
      <tr>
        <td id="L321" class="blob-num js-line-number" data-line-number="321"></td>
        <td id="LC321" class="blob-code blob-code-inner js-file-line">    <span class="pl-c"><span class="pl-c">#</span> tags</span></td>
      </tr>
      <tr>
        <td id="L322" class="blob-num js-line-number" data-line-number="322"></td>
        <td id="LC322" class="blob-code blob-code-inner js-file-line">    <span class="pl-c1">map</span>.redirect(<span class="pl-s"><span class="pl-pds">&#39;</span>/tags<span class="pl-pds">&#39;</span></span>, <span class="pl-s"><span class="pl-pds">&#39;</span>/tag<span class="pl-pds">&#39;</span></span>)</td>
      </tr>
      <tr>
        <td id="L323" class="blob-num js-line-number" data-line-number="323"></td>
        <td id="LC323" class="blob-code blob-code-inner js-file-line">    <span class="pl-c1">map</span>.redirect(<span class="pl-s"><span class="pl-pds">&#39;</span>/tags/<span class="pl-c1">{url<span class="pl-k">:</span>.*}</span><span class="pl-pds">&#39;</span></span>, <span class="pl-s"><span class="pl-pds">&#39;</span>/tag/<span class="pl-c1">{url}</span><span class="pl-pds">&#39;</span></span>)</td>
      </tr>
      <tr>
        <td id="L324" class="blob-num js-line-number" data-line-number="324"></td>
        <td id="LC324" class="blob-code blob-code-inner js-file-line">    <span class="pl-c1">map</span>.redirect(<span class="pl-s"><span class="pl-pds">&#39;</span>/tag/read/<span class="pl-c1">{url<span class="pl-k">:</span>.*}</span><span class="pl-pds">&#39;</span></span>, <span class="pl-s"><span class="pl-pds">&#39;</span>/tag/<span class="pl-c1">{url}</span><span class="pl-pds">&#39;</span></span>,</td>
      </tr>
      <tr>
        <td id="L325" class="blob-num js-line-number" data-line-number="325"></td>
        <td id="LC325" class="blob-code blob-code-inner js-file-line">                 <span class="pl-v">_redirect_code</span><span class="pl-k">=</span><span class="pl-s"><span class="pl-pds">&#39;</span>301 Moved Permanently<span class="pl-pds">&#39;</span></span>)</td>
      </tr>
      <tr>
        <td id="L326" class="blob-num js-line-number" data-line-number="326"></td>
        <td id="LC326" class="blob-code blob-code-inner js-file-line">    <span class="pl-c1">map</span>.connect(<span class="pl-s"><span class="pl-pds">&#39;</span>/tag<span class="pl-pds">&#39;</span></span>, <span class="pl-v">controller</span><span class="pl-k">=</span><span class="pl-s"><span class="pl-pds">&#39;</span>tag<span class="pl-pds">&#39;</span></span>, <span class="pl-v">action</span><span class="pl-k">=</span><span class="pl-s"><span class="pl-pds">&#39;</span>index<span class="pl-pds">&#39;</span></span>)</td>
      </tr>
      <tr>
        <td id="L327" class="blob-num js-line-number" data-line-number="327"></td>
        <td id="LC327" class="blob-code blob-code-inner js-file-line">    <span class="pl-c1">map</span>.connect(<span class="pl-s"><span class="pl-pds">&#39;</span>/tag/<span class="pl-c1">{id}</span><span class="pl-pds">&#39;</span></span>, <span class="pl-v">controller</span><span class="pl-k">=</span><span class="pl-s"><span class="pl-pds">&#39;</span>tag<span class="pl-pds">&#39;</span></span>, <span class="pl-v">action</span><span class="pl-k">=</span><span class="pl-s"><span class="pl-pds">&#39;</span>read<span class="pl-pds">&#39;</span></span>)</td>
      </tr>
      <tr>
        <td id="L328" class="blob-num js-line-number" data-line-number="328"></td>
        <td id="LC328" class="blob-code blob-code-inner js-file-line">    <span class="pl-c"><span class="pl-c">#</span> users</span></td>
      </tr>
      <tr>
        <td id="L329" class="blob-num js-line-number" data-line-number="329"></td>
        <td id="LC329" class="blob-code blob-code-inner js-file-line">    <span class="pl-c1">map</span>.redirect(<span class="pl-s"><span class="pl-pds">&#39;</span>/users/<span class="pl-c1">{url<span class="pl-k">:</span>.*}</span><span class="pl-pds">&#39;</span></span>, <span class="pl-s"><span class="pl-pds">&#39;</span>/user/<span class="pl-c1">{url}</span><span class="pl-pds">&#39;</span></span>)</td>
      </tr>
      <tr>
        <td id="L330" class="blob-num js-line-number" data-line-number="330"></td>
        <td id="LC330" class="blob-code blob-code-inner js-file-line">    <span class="pl-c1">map</span>.redirect(<span class="pl-s"><span class="pl-pds">&#39;</span>/user/<span class="pl-pds">&#39;</span></span>, <span class="pl-s"><span class="pl-pds">&#39;</span>/user<span class="pl-pds">&#39;</span></span>)</td>
      </tr>
      <tr>
        <td id="L331" class="blob-num js-line-number" data-line-number="331"></td>
        <td id="LC331" class="blob-code blob-code-inner js-file-line">    <span class="pl-k">with</span> SubMapper(<span class="pl-c1">map</span>, <span class="pl-v">controller</span><span class="pl-k">=</span><span class="pl-s"><span class="pl-pds">&#39;</span>user<span class="pl-pds">&#39;</span></span>) <span class="pl-k">as</span> m:</td>
      </tr>
      <tr>
        <td id="L332" class="blob-num js-line-number" data-line-number="332"></td>
        <td id="LC332" class="blob-code blob-code-inner js-file-line">        m.connect(<span class="pl-s"><span class="pl-pds">&#39;</span>/user/edit<span class="pl-pds">&#39;</span></span>, <span class="pl-v">action</span><span class="pl-k">=</span><span class="pl-s"><span class="pl-pds">&#39;</span>edit<span class="pl-pds">&#39;</span></span>)</td>
      </tr>
      <tr>
        <td id="L333" class="blob-num js-line-number" data-line-number="333"></td>
        <td id="LC333" class="blob-code blob-code-inner js-file-line">        m.connect(<span class="pl-s"><span class="pl-pds">&#39;</span>user_generate_apikey<span class="pl-pds">&#39;</span></span>, <span class="pl-s"><span class="pl-pds">&#39;</span>/user/generate_key/<span class="pl-c1">{id}</span><span class="pl-pds">&#39;</span></span>, <span class="pl-v">action</span><span class="pl-k">=</span><span class="pl-s"><span class="pl-pds">&#39;</span>generate_apikey<span class="pl-pds">&#39;</span></span>)</td>
      </tr>
      <tr>
        <td id="L334" class="blob-num js-line-number" data-line-number="334"></td>
        <td id="LC334" class="blob-code blob-code-inner js-file-line">        m.connect(<span class="pl-s"><span class="pl-pds">&#39;</span>/user/activity/<span class="pl-c1">{id}</span>/<span class="pl-c1">{offset}</span><span class="pl-pds">&#39;</span></span>, <span class="pl-v">action</span><span class="pl-k">=</span><span class="pl-s"><span class="pl-pds">&#39;</span>activity<span class="pl-pds">&#39;</span></span>)</td>
      </tr>
      <tr>
        <td id="L335" class="blob-num js-line-number" data-line-number="335"></td>
        <td id="LC335" class="blob-code blob-code-inner js-file-line">        m.connect(<span class="pl-s"><span class="pl-pds">&#39;</span>user_activity_stream<span class="pl-pds">&#39;</span></span>, <span class="pl-s"><span class="pl-pds">&#39;</span>/user/activity/<span class="pl-c1">{id}</span><span class="pl-pds">&#39;</span></span>,</td>
      </tr>
      <tr>
        <td id="L336" class="blob-num js-line-number" data-line-number="336"></td>
        <td id="LC336" class="blob-code blob-code-inner js-file-line">                  <span class="pl-v">action</span><span class="pl-k">=</span><span class="pl-s"><span class="pl-pds">&#39;</span>activity<span class="pl-pds">&#39;</span></span>, <span class="pl-v">ckan_icon</span><span class="pl-k">=</span><span class="pl-s"><span class="pl-pds">&#39;</span>clock-o<span class="pl-pds">&#39;</span></span>)</td>
      </tr>
      <tr>
        <td id="L337" class="blob-num js-line-number" data-line-number="337"></td>
        <td id="LC337" class="blob-code blob-code-inner js-file-line">        m.connect(<span class="pl-s"><span class="pl-pds">&#39;</span>user_dashboard<span class="pl-pds">&#39;</span></span>, <span class="pl-s"><span class="pl-pds">&#39;</span>/dashboard<span class="pl-pds">&#39;</span></span>, <span class="pl-v">action</span><span class="pl-k">=</span><span class="pl-s"><span class="pl-pds">&#39;</span>dashboard<span class="pl-pds">&#39;</span></span>,</td>
      </tr>
      <tr>
        <td id="L338" class="blob-num js-line-number" data-line-number="338"></td>
        <td id="LC338" class="blob-code blob-code-inner js-file-line">                  <span class="pl-v">ckan_icon</span><span class="pl-k">=</span><span class="pl-s"><span class="pl-pds">&#39;</span>list<span class="pl-pds">&#39;</span></span>)</td>
      </tr>
      <tr>
        <td id="L339" class="blob-num js-line-number" data-line-number="339"></td>
        <td id="LC339" class="blob-code blob-code-inner js-file-line">        m.connect(<span class="pl-s"><span class="pl-pds">&#39;</span>user_dashboard_datasets<span class="pl-pds">&#39;</span></span>, <span class="pl-s"><span class="pl-pds">&#39;</span>/dashboard/datasets<span class="pl-pds">&#39;</span></span>,</td>
      </tr>
      <tr>
        <td id="L340" class="blob-num js-line-number" data-line-number="340"></td>
        <td id="LC340" class="blob-code blob-code-inner js-file-line">                  <span class="pl-v">action</span><span class="pl-k">=</span><span class="pl-s"><span class="pl-pds">&#39;</span>dashboard_datasets<span class="pl-pds">&#39;</span></span>, <span class="pl-v">ckan_icon</span><span class="pl-k">=</span><span class="pl-s"><span class="pl-pds">&#39;</span>sitemap<span class="pl-pds">&#39;</span></span>)</td>
      </tr>
      <tr>
        <td id="L341" class="blob-num js-line-number" data-line-number="341"></td>
        <td id="LC341" class="blob-code blob-code-inner js-file-line">        m.connect(<span class="pl-s"><span class="pl-pds">&#39;</span>user_dashboard_groups<span class="pl-pds">&#39;</span></span>, <span class="pl-s"><span class="pl-pds">&#39;</span>/dashboard/groups<span class="pl-pds">&#39;</span></span>,</td>
      </tr>
      <tr>
        <td id="L342" class="blob-num js-line-number" data-line-number="342"></td>
        <td id="LC342" class="blob-code blob-code-inner js-file-line">                  <span class="pl-v">action</span><span class="pl-k">=</span><span class="pl-s"><span class="pl-pds">&#39;</span>dashboard_groups<span class="pl-pds">&#39;</span></span>, <span class="pl-v">ckan_icon</span><span class="pl-k">=</span><span class="pl-s"><span class="pl-pds">&#39;</span>users<span class="pl-pds">&#39;</span></span>)</td>
      </tr>
      <tr>
        <td id="L343" class="blob-num js-line-number" data-line-number="343"></td>
        <td id="LC343" class="blob-code blob-code-inner js-file-line">        m.connect(<span class="pl-s"><span class="pl-pds">&#39;</span>user_dashboard_organizations<span class="pl-pds">&#39;</span></span>, <span class="pl-s"><span class="pl-pds">&#39;</span>/dashboard/organizations<span class="pl-pds">&#39;</span></span>,</td>
      </tr>
      <tr>
        <td id="L344" class="blob-num js-line-number" data-line-number="344"></td>
        <td id="LC344" class="blob-code blob-code-inner js-file-line">                  <span class="pl-v">action</span><span class="pl-k">=</span><span class="pl-s"><span class="pl-pds">&#39;</span>dashboard_organizations<span class="pl-pds">&#39;</span></span>, <span class="pl-v">ckan_icon</span><span class="pl-k">=</span><span class="pl-s"><span class="pl-pds">&#39;</span>building-o<span class="pl-pds">&#39;</span></span>)</td>
      </tr>
      <tr>
        <td id="L345" class="blob-num js-line-number" data-line-number="345"></td>
        <td id="LC345" class="blob-code blob-code-inner js-file-line">        m.connect(<span class="pl-s"><span class="pl-pds">&#39;</span>/dashboard/<span class="pl-c1">{offset}</span><span class="pl-pds">&#39;</span></span>, <span class="pl-v">action</span><span class="pl-k">=</span><span class="pl-s"><span class="pl-pds">&#39;</span>dashboard<span class="pl-pds">&#39;</span></span>)</td>
      </tr>
      <tr>
        <td id="L346" class="blob-num js-line-number" data-line-number="346"></td>
        <td id="LC346" class="blob-code blob-code-inner js-file-line">        m.connect(<span class="pl-s"><span class="pl-pds">&#39;</span>user_follow<span class="pl-pds">&#39;</span></span>, <span class="pl-s"><span class="pl-pds">&#39;</span>/user/follow/<span class="pl-c1">{id}</span><span class="pl-pds">&#39;</span></span>, <span class="pl-v">action</span><span class="pl-k">=</span><span class="pl-s"><span class="pl-pds">&#39;</span>follow<span class="pl-pds">&#39;</span></span>)</td>
      </tr>
      <tr>
        <td id="L347" class="blob-num js-line-number" data-line-number="347"></td>
        <td id="LC347" class="blob-code blob-code-inner js-file-line">        m.connect(<span class="pl-s"><span class="pl-pds">&#39;</span>/user/unfollow/<span class="pl-c1">{id}</span><span class="pl-pds">&#39;</span></span>, <span class="pl-v">action</span><span class="pl-k">=</span><span class="pl-s"><span class="pl-pds">&#39;</span>unfollow<span class="pl-pds">&#39;</span></span>)</td>
      </tr>
      <tr>
        <td id="L348" class="blob-num js-line-number" data-line-number="348"></td>
        <td id="LC348" class="blob-code blob-code-inner js-file-line">        m.connect(<span class="pl-s"><span class="pl-pds">&#39;</span>user_followers<span class="pl-pds">&#39;</span></span>, <span class="pl-s"><span class="pl-pds">&#39;</span>/user/followers/<span class="pl-c1">{id}</span><span class="pl-pds">&#39;</span></span>,</td>
      </tr>
      <tr>
        <td id="L349" class="blob-num js-line-number" data-line-number="349"></td>
        <td id="LC349" class="blob-code blob-code-inner js-file-line">                  <span class="pl-v">action</span><span class="pl-k">=</span><span class="pl-s"><span class="pl-pds">&#39;</span>followers<span class="pl-pds">&#39;</span></span>, <span class="pl-v">ckan_icon</span><span class="pl-k">=</span><span class="pl-s"><span class="pl-pds">&#39;</span>users<span class="pl-pds">&#39;</span></span>)</td>
      </tr>
      <tr>
        <td id="L350" class="blob-num js-line-number" data-line-number="350"></td>
        <td id="LC350" class="blob-code blob-code-inner js-file-line">        m.connect(<span class="pl-s"><span class="pl-pds">&#39;</span>user_edit<span class="pl-pds">&#39;</span></span>, <span class="pl-s"><span class="pl-pds">&#39;</span>/user/edit/<span class="pl-c1">{id}</span><span class="pl-pds">&#39;</span></span>, <span class="pl-v">action</span><span class="pl-k">=</span><span class="pl-s"><span class="pl-pds">&#39;</span>edit<span class="pl-pds">&#39;</span></span>,</td>
      </tr>
      <tr>
        <td id="L351" class="blob-num js-line-number" data-line-number="351"></td>
        <td id="LC351" class="blob-code blob-code-inner js-file-line">                  <span class="pl-v">ckan_icon</span><span class="pl-k">=</span><span class="pl-s"><span class="pl-pds">&#39;</span>cog<span class="pl-pds">&#39;</span></span>)</td>
      </tr>
      <tr>
        <td id="L352" class="blob-num js-line-number" data-line-number="352"></td>
        <td id="LC352" class="blob-code blob-code-inner js-file-line">        m.connect(<span class="pl-s"><span class="pl-pds">&#39;</span>user_delete<span class="pl-pds">&#39;</span></span>, <span class="pl-s"><span class="pl-pds">&#39;</span>/user/delete/<span class="pl-c1">{id}</span><span class="pl-pds">&#39;</span></span>, <span class="pl-v">action</span><span class="pl-k">=</span><span class="pl-s"><span class="pl-pds">&#39;</span>delete<span class="pl-pds">&#39;</span></span>)</td>
      </tr>
      <tr>
        <td id="L353" class="blob-num js-line-number" data-line-number="353"></td>
        <td id="LC353" class="blob-code blob-code-inner js-file-line">        m.connect(<span class="pl-s"><span class="pl-pds">&#39;</span>/user/reset/<span class="pl-c1">{id}</span><span class="pl-pds">&#39;</span></span>, <span class="pl-v">action</span><span class="pl-k">=</span><span class="pl-s"><span class="pl-pds">&#39;</span>perform_reset<span class="pl-pds">&#39;</span></span>)</td>
      </tr>
      <tr>
        <td id="L354" class="blob-num js-line-number" data-line-number="354"></td>
        <td id="LC354" class="blob-code blob-code-inner js-file-line">        m.connect(<span class="pl-s"><span class="pl-pds">&#39;</span>register<span class="pl-pds">&#39;</span></span>, <span class="pl-s"><span class="pl-pds">&#39;</span>/user/register<span class="pl-pds">&#39;</span></span>, <span class="pl-v">action</span><span class="pl-k">=</span><span class="pl-s"><span class="pl-pds">&#39;</span>register<span class="pl-pds">&#39;</span></span>)</td>
      </tr>
      <tr>
        <td id="L355" class="blob-num js-line-number" data-line-number="355"></td>
        <td id="LC355" class="blob-code blob-code-inner js-file-line">        m.connect(<span class="pl-s"><span class="pl-pds">&#39;</span>login<span class="pl-pds">&#39;</span></span>, <span class="pl-s"><span class="pl-pds">&#39;</span>/user/login<span class="pl-pds">&#39;</span></span>, <span class="pl-v">action</span><span class="pl-k">=</span><span class="pl-s"><span class="pl-pds">&#39;</span>login<span class="pl-pds">&#39;</span></span>)</td>
      </tr>
      <tr>
        <td id="L356" class="blob-num js-line-number" data-line-number="356"></td>
        <td id="LC356" class="blob-code blob-code-inner js-file-line">        m.connect(<span class="pl-s"><span class="pl-pds">&#39;</span>/user/_logout<span class="pl-pds">&#39;</span></span>, <span class="pl-v">action</span><span class="pl-k">=</span><span class="pl-s"><span class="pl-pds">&#39;</span>logout<span class="pl-pds">&#39;</span></span>)</td>
      </tr>
      <tr>
        <td id="L357" class="blob-num js-line-number" data-line-number="357"></td>
        <td id="LC357" class="blob-code blob-code-inner js-file-line">        m.connect(<span class="pl-s"><span class="pl-pds">&#39;</span>/user/logged_in<span class="pl-pds">&#39;</span></span>, <span class="pl-v">action</span><span class="pl-k">=</span><span class="pl-s"><span class="pl-pds">&#39;</span>logged_in<span class="pl-pds">&#39;</span></span>)</td>
      </tr>
      <tr>
        <td id="L358" class="blob-num js-line-number" data-line-number="358"></td>
        <td id="LC358" class="blob-code blob-code-inner js-file-line">        m.connect(<span class="pl-s"><span class="pl-pds">&#39;</span>/user/logged_out<span class="pl-pds">&#39;</span></span>, <span class="pl-v">action</span><span class="pl-k">=</span><span class="pl-s"><span class="pl-pds">&#39;</span>logged_out<span class="pl-pds">&#39;</span></span>)</td>
      </tr>
      <tr>
        <td id="L359" class="blob-num js-line-number" data-line-number="359"></td>
        <td id="LC359" class="blob-code blob-code-inner js-file-line">        m.connect(<span class="pl-s"><span class="pl-pds">&#39;</span>/user/logged_out_redirect<span class="pl-pds">&#39;</span></span>, <span class="pl-v">action</span><span class="pl-k">=</span><span class="pl-s"><span class="pl-pds">&#39;</span>logged_out_page<span class="pl-pds">&#39;</span></span>)</td>
      </tr>
      <tr>
        <td id="L360" class="blob-num js-line-number" data-line-number="360"></td>
        <td id="LC360" class="blob-code blob-code-inner js-file-line">        m.connect(<span class="pl-s"><span class="pl-pds">&#39;</span>/user/reset<span class="pl-pds">&#39;</span></span>, <span class="pl-v">action</span><span class="pl-k">=</span><span class="pl-s"><span class="pl-pds">&#39;</span>request_reset<span class="pl-pds">&#39;</span></span>)</td>
      </tr>
      <tr>
        <td id="L361" class="blob-num js-line-number" data-line-number="361"></td>
        <td id="LC361" class="blob-code blob-code-inner js-file-line">        m.connect(<span class="pl-s"><span class="pl-pds">&#39;</span>/user/me<span class="pl-pds">&#39;</span></span>, <span class="pl-v">action</span><span class="pl-k">=</span><span class="pl-s"><span class="pl-pds">&#39;</span>me<span class="pl-pds">&#39;</span></span>)</td>
      </tr>
      <tr>
        <td id="L362" class="blob-num js-line-number" data-line-number="362"></td>
        <td id="LC362" class="blob-code blob-code-inner js-file-line">        m.connect(<span class="pl-s"><span class="pl-pds">&#39;</span>/user/set_lang/<span class="pl-c1">{lang}</span><span class="pl-pds">&#39;</span></span>, <span class="pl-v">action</span><span class="pl-k">=</span><span class="pl-s"><span class="pl-pds">&#39;</span>set_lang<span class="pl-pds">&#39;</span></span>)</td>
      </tr>
      <tr>
        <td id="L363" class="blob-num js-line-number" data-line-number="363"></td>
        <td id="LC363" class="blob-code blob-code-inner js-file-line">        m.connect(<span class="pl-s"><span class="pl-pds">&#39;</span>user_datasets<span class="pl-pds">&#39;</span></span>, <span class="pl-s"><span class="pl-pds">&#39;</span>/user/<span class="pl-c1">{id}</span><span class="pl-pds">&#39;</span></span>, <span class="pl-v">action</span><span class="pl-k">=</span><span class="pl-s"><span class="pl-pds">&#39;</span>read<span class="pl-pds">&#39;</span></span>,</td>
      </tr>
      <tr>
        <td id="L364" class="blob-num js-line-number" data-line-number="364"></td>
        <td id="LC364" class="blob-code blob-code-inner js-file-line">                  <span class="pl-v">ckan_icon</span><span class="pl-k">=</span><span class="pl-s"><span class="pl-pds">&#39;</span>sitemap<span class="pl-pds">&#39;</span></span>)</td>
      </tr>
      <tr>
        <td id="L365" class="blob-num js-line-number" data-line-number="365"></td>
        <td id="LC365" class="blob-code blob-code-inner js-file-line">        m.connect(<span class="pl-s"><span class="pl-pds">&#39;</span>user_index<span class="pl-pds">&#39;</span></span>, <span class="pl-s"><span class="pl-pds">&#39;</span>/user<span class="pl-pds">&#39;</span></span>, <span class="pl-v">action</span><span class="pl-k">=</span><span class="pl-s"><span class="pl-pds">&#39;</span>index<span class="pl-pds">&#39;</span></span>)</td>
      </tr>
      <tr>
        <td id="L366" class="blob-num js-line-number" data-line-number="366"></td>
        <td id="LC366" class="blob-code blob-code-inner js-file-line">
</td>
      </tr>
      <tr>
        <td id="L367" class="blob-num js-line-number" data-line-number="367"></td>
        <td id="LC367" class="blob-code blob-code-inner js-file-line">    <span class="pl-k">with</span> SubMapper(<span class="pl-c1">map</span>, <span class="pl-v">controller</span><span class="pl-k">=</span><span class="pl-s"><span class="pl-pds">&#39;</span>revision<span class="pl-pds">&#39;</span></span>) <span class="pl-k">as</span> m:</td>
      </tr>
      <tr>
        <td id="L368" class="blob-num js-line-number" data-line-number="368"></td>
        <td id="LC368" class="blob-code blob-code-inner js-file-line">        m.connect(<span class="pl-s"><span class="pl-pds">&#39;</span>/revision<span class="pl-pds">&#39;</span></span>, <span class="pl-v">action</span><span class="pl-k">=</span><span class="pl-s"><span class="pl-pds">&#39;</span>index<span class="pl-pds">&#39;</span></span>)</td>
      </tr>
      <tr>
        <td id="L369" class="blob-num js-line-number" data-line-number="369"></td>
        <td id="LC369" class="blob-code blob-code-inner js-file-line">        m.connect(<span class="pl-s"><span class="pl-pds">&#39;</span>/revision/edit/<span class="pl-c1">{id}</span><span class="pl-pds">&#39;</span></span>, <span class="pl-v">action</span><span class="pl-k">=</span><span class="pl-s"><span class="pl-pds">&#39;</span>edit<span class="pl-pds">&#39;</span></span>)</td>
      </tr>
      <tr>
        <td id="L370" class="blob-num js-line-number" data-line-number="370"></td>
        <td id="LC370" class="blob-code blob-code-inner js-file-line">        m.connect(<span class="pl-s"><span class="pl-pds">&#39;</span>/revision/diff/<span class="pl-c1">{id}</span><span class="pl-pds">&#39;</span></span>, <span class="pl-v">action</span><span class="pl-k">=</span><span class="pl-s"><span class="pl-pds">&#39;</span>diff<span class="pl-pds">&#39;</span></span>)</td>
      </tr>
      <tr>
        <td id="L371" class="blob-num js-line-number" data-line-number="371"></td>
        <td id="LC371" class="blob-code blob-code-inner js-file-line">        m.connect(<span class="pl-s"><span class="pl-pds">&#39;</span>/revision/list<span class="pl-pds">&#39;</span></span>, <span class="pl-v">action</span><span class="pl-k">=</span><span class="pl-s"><span class="pl-pds">&#39;</span>list<span class="pl-pds">&#39;</span></span>)</td>
      </tr>
      <tr>
        <td id="L372" class="blob-num js-line-number" data-line-number="372"></td>
        <td id="LC372" class="blob-code blob-code-inner js-file-line">        m.connect(<span class="pl-s"><span class="pl-pds">&#39;</span>/revision/<span class="pl-c1">{id}</span><span class="pl-pds">&#39;</span></span>, <span class="pl-v">action</span><span class="pl-k">=</span><span class="pl-s"><span class="pl-pds">&#39;</span>read<span class="pl-pds">&#39;</span></span>)</td>
      </tr>
      <tr>
        <td id="L373" class="blob-num js-line-number" data-line-number="373"></td>
        <td id="LC373" class="blob-code blob-code-inner js-file-line">
</td>
      </tr>
      <tr>
        <td id="L374" class="blob-num js-line-number" data-line-number="374"></td>
        <td id="LC374" class="blob-code blob-code-inner js-file-line">    <span class="pl-c"><span class="pl-c">#</span> feeds</span></td>
      </tr>
      <tr>
        <td id="L375" class="blob-num js-line-number" data-line-number="375"></td>
        <td id="LC375" class="blob-code blob-code-inner js-file-line">    <span class="pl-k">with</span> SubMapper(<span class="pl-c1">map</span>, <span class="pl-v">controller</span><span class="pl-k">=</span><span class="pl-s"><span class="pl-pds">&#39;</span>feed<span class="pl-pds">&#39;</span></span>) <span class="pl-k">as</span> m:</td>
      </tr>
      <tr>
        <td id="L376" class="blob-num js-line-number" data-line-number="376"></td>
        <td id="LC376" class="blob-code blob-code-inner js-file-line">        m.connect(<span class="pl-s"><span class="pl-pds">&#39;</span>/feeds/group/<span class="pl-c1">{id}</span>.atom<span class="pl-pds">&#39;</span></span>, <span class="pl-v">action</span><span class="pl-k">=</span><span class="pl-s"><span class="pl-pds">&#39;</span>group<span class="pl-pds">&#39;</span></span>)</td>
      </tr>
      <tr>
        <td id="L377" class="blob-num js-line-number" data-line-number="377"></td>
        <td id="LC377" class="blob-code blob-code-inner js-file-line">        m.connect(<span class="pl-s"><span class="pl-pds">&#39;</span>/feeds/organization/<span class="pl-c1">{id}</span>.atom<span class="pl-pds">&#39;</span></span>, <span class="pl-v">action</span><span class="pl-k">=</span><span class="pl-s"><span class="pl-pds">&#39;</span>organization<span class="pl-pds">&#39;</span></span>)</td>
      </tr>
      <tr>
        <td id="L378" class="blob-num js-line-number" data-line-number="378"></td>
        <td id="LC378" class="blob-code blob-code-inner js-file-line">        m.connect(<span class="pl-s"><span class="pl-pds">&#39;</span>/feeds/tag/<span class="pl-c1">{id}</span>.atom<span class="pl-pds">&#39;</span></span>, <span class="pl-v">action</span><span class="pl-k">=</span><span class="pl-s"><span class="pl-pds">&#39;</span>tag<span class="pl-pds">&#39;</span></span>)</td>
      </tr>
      <tr>
        <td id="L379" class="blob-num js-line-number" data-line-number="379"></td>
        <td id="LC379" class="blob-code blob-code-inner js-file-line">        m.connect(<span class="pl-s"><span class="pl-pds">&#39;</span>/feeds/dataset.atom<span class="pl-pds">&#39;</span></span>, <span class="pl-v">action</span><span class="pl-k">=</span><span class="pl-s"><span class="pl-pds">&#39;</span>general<span class="pl-pds">&#39;</span></span>)</td>
      </tr>
      <tr>
        <td id="L380" class="blob-num js-line-number" data-line-number="380"></td>
        <td id="LC380" class="blob-code blob-code-inner js-file-line">        m.connect(<span class="pl-s"><span class="pl-pds">&#39;</span>/feeds/custom.atom<span class="pl-pds">&#39;</span></span>, <span class="pl-v">action</span><span class="pl-k">=</span><span class="pl-s"><span class="pl-pds">&#39;</span>custom<span class="pl-pds">&#39;</span></span>)</td>
      </tr>
      <tr>
        <td id="L381" class="blob-num js-line-number" data-line-number="381"></td>
        <td id="LC381" class="blob-code blob-code-inner js-file-line">
</td>
      </tr>
      <tr>
        <td id="L382" class="blob-num js-line-number" data-line-number="382"></td>
        <td id="LC382" class="blob-code blob-code-inner js-file-line">    <span class="pl-c1">map</span>.connect(<span class="pl-s"><span class="pl-pds">&#39;</span>ckanadmin_index<span class="pl-pds">&#39;</span></span>, <span class="pl-s"><span class="pl-pds">&#39;</span>/ckan-admin<span class="pl-pds">&#39;</span></span>, <span class="pl-v">controller</span><span class="pl-k">=</span><span class="pl-s"><span class="pl-pds">&#39;</span>admin<span class="pl-pds">&#39;</span></span>,</td>
      </tr>
      <tr>
        <td id="L383" class="blob-num js-line-number" data-line-number="383"></td>
        <td id="LC383" class="blob-code blob-code-inner js-file-line">                <span class="pl-v">action</span><span class="pl-k">=</span><span class="pl-s"><span class="pl-pds">&#39;</span>index<span class="pl-pds">&#39;</span></span>, <span class="pl-v">ckan_icon</span><span class="pl-k">=</span><span class="pl-s"><span class="pl-pds">&#39;</span>gavel<span class="pl-pds">&#39;</span></span>)</td>
      </tr>
      <tr>
        <td id="L384" class="blob-num js-line-number" data-line-number="384"></td>
        <td id="LC384" class="blob-code blob-code-inner js-file-line">    <span class="pl-c1">map</span>.connect(<span class="pl-s"><span class="pl-pds">&#39;</span>ckanadmin_config<span class="pl-pds">&#39;</span></span>, <span class="pl-s"><span class="pl-pds">&#39;</span>/ckan-admin/config<span class="pl-pds">&#39;</span></span>, <span class="pl-v">controller</span><span class="pl-k">=</span><span class="pl-s"><span class="pl-pds">&#39;</span>admin<span class="pl-pds">&#39;</span></span>,</td>
      </tr>
      <tr>
        <td id="L385" class="blob-num js-line-number" data-line-number="385"></td>
        <td id="LC385" class="blob-code blob-code-inner js-file-line">                <span class="pl-v">action</span><span class="pl-k">=</span><span class="pl-s"><span class="pl-pds">&#39;</span>config<span class="pl-pds">&#39;</span></span>, <span class="pl-v">ckan_icon</span><span class="pl-k">=</span><span class="pl-s"><span class="pl-pds">&#39;</span>check-square-o<span class="pl-pds">&#39;</span></span>)</td>
      </tr>
      <tr>
        <td id="L386" class="blob-num js-line-number" data-line-number="386"></td>
        <td id="LC386" class="blob-code blob-code-inner js-file-line">    <span class="pl-c1">map</span>.connect(<span class="pl-s"><span class="pl-pds">&#39;</span>ckanadmin_trash<span class="pl-pds">&#39;</span></span>, <span class="pl-s"><span class="pl-pds">&#39;</span>/ckan-admin/trash<span class="pl-pds">&#39;</span></span>, <span class="pl-v">controller</span><span class="pl-k">=</span><span class="pl-s"><span class="pl-pds">&#39;</span>admin<span class="pl-pds">&#39;</span></span>,</td>
      </tr>
      <tr>
        <td id="L387" class="blob-num js-line-number" data-line-number="387"></td>
        <td id="LC387" class="blob-code blob-code-inner js-file-line">                <span class="pl-v">action</span><span class="pl-k">=</span><span class="pl-s"><span class="pl-pds">&#39;</span>trash<span class="pl-pds">&#39;</span></span>, <span class="pl-v">ckan_icon</span><span class="pl-k">=</span><span class="pl-s"><span class="pl-pds">&#39;</span>trash-o<span class="pl-pds">&#39;</span></span>)</td>
      </tr>
      <tr>
        <td id="L388" class="blob-num js-line-number" data-line-number="388"></td>
        <td id="LC388" class="blob-code blob-code-inner js-file-line">    <span class="pl-c1">map</span>.connect(<span class="pl-s"><span class="pl-pds">&#39;</span>ckanadmin<span class="pl-pds">&#39;</span></span>, <span class="pl-s"><span class="pl-pds">&#39;</span>/ckan-admin/<span class="pl-c1">{action}</span><span class="pl-pds">&#39;</span></span>, <span class="pl-v">controller</span><span class="pl-k">=</span><span class="pl-s"><span class="pl-pds">&#39;</span>admin<span class="pl-pds">&#39;</span></span>)</td>
      </tr>
      <tr>
        <td id="L389" class="blob-num js-line-number" data-line-number="389"></td>
        <td id="LC389" class="blob-code blob-code-inner js-file-line">
</td>
      </tr>
      <tr>
        <td id="L390" class="blob-num js-line-number" data-line-number="390"></td>
        <td id="LC390" class="blob-code blob-code-inner js-file-line">    <span class="pl-k">with</span> SubMapper(<span class="pl-c1">map</span>, <span class="pl-v">controller</span><span class="pl-k">=</span><span class="pl-s"><span class="pl-pds">&#39;</span>ckan.controllers.storage:StorageController<span class="pl-pds">&#39;</span></span>) <span class="pl-k">as</span> m:</td>
      </tr>
      <tr>
        <td id="L391" class="blob-num js-line-number" data-line-number="391"></td>
        <td id="LC391" class="blob-code blob-code-inner js-file-line">        m.connect(<span class="pl-s"><span class="pl-pds">&#39;</span>storage_file<span class="pl-pds">&#39;</span></span>, <span class="pl-s"><span class="pl-pds">&#39;</span>/storage/f/<span class="pl-c1">{label<span class="pl-k">:</span>.*}</span><span class="pl-pds">&#39;</span></span>,</td>
      </tr>
      <tr>
        <td id="L392" class="blob-num js-line-number" data-line-number="392"></td>
        <td id="LC392" class="blob-code blob-code-inner js-file-line">                  <span class="pl-v">action</span><span class="pl-k">=</span><span class="pl-s"><span class="pl-pds">&#39;</span>file<span class="pl-pds">&#39;</span></span>)</td>
      </tr>
      <tr>
        <td id="L393" class="blob-num js-line-number" data-line-number="393"></td>
        <td id="LC393" class="blob-code blob-code-inner js-file-line">
</td>
      </tr>
      <tr>
        <td id="L394" class="blob-num js-line-number" data-line-number="394"></td>
        <td id="LC394" class="blob-code blob-code-inner js-file-line">    <span class="pl-k">with</span> SubMapper(<span class="pl-c1">map</span>, <span class="pl-v">controller</span><span class="pl-k">=</span><span class="pl-s"><span class="pl-pds">&#39;</span>util<span class="pl-pds">&#39;</span></span>) <span class="pl-k">as</span> m:</td>
      </tr>
      <tr>
        <td id="L395" class="blob-num js-line-number" data-line-number="395"></td>
        <td id="LC395" class="blob-code blob-code-inner js-file-line">        m.connect(<span class="pl-s"><span class="pl-pds">&#39;</span>/i18n/strings_<span class="pl-c1">{lang}</span>.js<span class="pl-pds">&#39;</span></span>, <span class="pl-v">action</span><span class="pl-k">=</span><span class="pl-s"><span class="pl-pds">&#39;</span>i18n_js_strings<span class="pl-pds">&#39;</span></span>)</td>
      </tr>
      <tr>
        <td id="L396" class="blob-num js-line-number" data-line-number="396"></td>
        <td id="LC396" class="blob-code blob-code-inner js-file-line">        m.connect(<span class="pl-s"><span class="pl-pds">&#39;</span>/util/redirect<span class="pl-pds">&#39;</span></span>, <span class="pl-v">action</span><span class="pl-k">=</span><span class="pl-s"><span class="pl-pds">&#39;</span>redirect<span class="pl-pds">&#39;</span></span>)</td>
      </tr>
      <tr>
        <td id="L397" class="blob-num js-line-number" data-line-number="397"></td>
        <td id="LC397" class="blob-code blob-code-inner js-file-line">        m.connect(<span class="pl-s"><span class="pl-pds">&#39;</span>/testing/primer<span class="pl-pds">&#39;</span></span>, <span class="pl-v">action</span><span class="pl-k">=</span><span class="pl-s"><span class="pl-pds">&#39;</span>primer<span class="pl-pds">&#39;</span></span>)</td>
      </tr>
      <tr>
        <td id="L398" class="blob-num js-line-number" data-line-number="398"></td>
        <td id="LC398" class="blob-code blob-code-inner js-file-line">        m.connect(<span class="pl-s"><span class="pl-pds">&#39;</span>/testing/markup<span class="pl-pds">&#39;</span></span>, <span class="pl-v">action</span><span class="pl-k">=</span><span class="pl-s"><span class="pl-pds">&#39;</span>markup<span class="pl-pds">&#39;</span></span>)</td>
      </tr>
      <tr>
        <td id="L399" class="blob-num js-line-number" data-line-number="399"></td>
        <td id="LC399" class="blob-code blob-code-inner js-file-line">
</td>
      </tr>
      <tr>
        <td id="L400" class="blob-num js-line-number" data-line-number="400"></td>
        <td id="LC400" class="blob-code blob-code-inner js-file-line">    <span class="pl-c"><span class="pl-c">#</span> robots.txt</span></td>
      </tr>
      <tr>
        <td id="L401" class="blob-num js-line-number" data-line-number="401"></td>
        <td id="LC401" class="blob-code blob-code-inner js-file-line">    <span class="pl-c1">map</span>.connect(<span class="pl-s"><span class="pl-pds">&#39;</span>/(robots.txt)<span class="pl-pds">&#39;</span></span>, <span class="pl-v">controller</span><span class="pl-k">=</span><span class="pl-s"><span class="pl-pds">&#39;</span>template<span class="pl-pds">&#39;</span></span>, <span class="pl-v">action</span><span class="pl-k">=</span><span class="pl-s"><span class="pl-pds">&#39;</span>view<span class="pl-pds">&#39;</span></span>)</td>
      </tr>
      <tr>
        <td id="L402" class="blob-num js-line-number" data-line-number="402"></td>
        <td id="LC402" class="blob-code blob-code-inner js-file-line">
</td>
      </tr>
      <tr>
        <td id="L403" class="blob-num js-line-number" data-line-number="403"></td>
        <td id="LC403" class="blob-code blob-code-inner js-file-line">    <span class="pl-c"><span class="pl-c">#</span> Mark all unmarked routes added up until now as core routes</span></td>
      </tr>
      <tr>
        <td id="L404" class="blob-num js-line-number" data-line-number="404"></td>
        <td id="LC404" class="blob-code blob-code-inner js-file-line">    <span class="pl-k">for</span> route <span class="pl-k">in</span> <span class="pl-c1">map</span>.matchlist:</td>
      </tr>
      <tr>
        <td id="L405" class="blob-num js-line-number" data-line-number="405"></td>
        <td id="LC405" class="blob-code blob-code-inner js-file-line">        <span class="pl-k">if</span> <span class="pl-k">not</span> <span class="pl-c1">hasattr</span>(route, <span class="pl-s"><span class="pl-pds">&#39;</span>_ckan_core<span class="pl-pds">&#39;</span></span>):</td>
      </tr>
      <tr>
        <td id="L406" class="blob-num js-line-number" data-line-number="406"></td>
        <td id="LC406" class="blob-code blob-code-inner js-file-line">            route._ckan_core <span class="pl-k">=</span> <span class="pl-c1">True</span></td>
      </tr>
      <tr>
        <td id="L407" class="blob-num js-line-number" data-line-number="407"></td>
        <td id="LC407" class="blob-code blob-code-inner js-file-line">
</td>
      </tr>
      <tr>
        <td id="L408" class="blob-num js-line-number" data-line-number="408"></td>
        <td id="LC408" class="blob-code blob-code-inner js-file-line">    <span class="pl-k">for</span> plugin <span class="pl-k">in</span> p.PluginImplementations(p.IRoutes):</td>
      </tr>
      <tr>
        <td id="L409" class="blob-num js-line-number" data-line-number="409"></td>
        <td id="LC409" class="blob-code blob-code-inner js-file-line">        <span class="pl-c1">map</span> <span class="pl-k">=</span> plugin.after_map(<span class="pl-c1">map</span>)</td>
      </tr>
      <tr>
        <td id="L410" class="blob-num js-line-number" data-line-number="410"></td>
        <td id="LC410" class="blob-code blob-code-inner js-file-line">
</td>
      </tr>
      <tr>
        <td id="L411" class="blob-num js-line-number" data-line-number="411"></td>
        <td id="LC411" class="blob-code blob-code-inner js-file-line">    <span class="pl-c"><span class="pl-c">#</span> Mark all routes added from extensions on the `after_map` extension point</span></td>
      </tr>
      <tr>
        <td id="L412" class="blob-num js-line-number" data-line-number="412"></td>
        <td id="LC412" class="blob-code blob-code-inner js-file-line">    <span class="pl-c"><span class="pl-c">#</span> as non-core</span></td>
      </tr>
      <tr>
        <td id="L413" class="blob-num js-line-number" data-line-number="413"></td>
        <td id="LC413" class="blob-code blob-code-inner js-file-line">    <span class="pl-k">for</span> route <span class="pl-k">in</span> <span class="pl-c1">map</span>.matchlist:</td>
      </tr>
      <tr>
        <td id="L414" class="blob-num js-line-number" data-line-number="414"></td>
        <td id="LC414" class="blob-code blob-code-inner js-file-line">        <span class="pl-k">if</span> <span class="pl-k">not</span> <span class="pl-c1">hasattr</span>(route, <span class="pl-s"><span class="pl-pds">&#39;</span>_ckan_core<span class="pl-pds">&#39;</span></span>):</td>
      </tr>
      <tr>
        <td id="L415" class="blob-num js-line-number" data-line-number="415"></td>
        <td id="LC415" class="blob-code blob-code-inner js-file-line">            route._ckan_core <span class="pl-k">=</span> <span class="pl-c1">False</span></td>
      </tr>
      <tr>
        <td id="L416" class="blob-num js-line-number" data-line-number="416"></td>
        <td id="LC416" class="blob-code blob-code-inner js-file-line">
</td>
      </tr>
      <tr>
        <td id="L417" class="blob-num js-line-number" data-line-number="417"></td>
        <td id="LC417" class="blob-code blob-code-inner js-file-line">    <span class="pl-c"><span class="pl-c">#</span> sometimes we get requests for favicon.ico we should redirect to</span></td>
      </tr>
      <tr>
        <td id="L418" class="blob-num js-line-number" data-line-number="418"></td>
        <td id="LC418" class="blob-code blob-code-inner js-file-line">    <span class="pl-c"><span class="pl-c">#</span> the real favicon location.</span></td>
      </tr>
      <tr>
        <td id="L419" class="blob-num js-line-number" data-line-number="419"></td>
        <td id="LC419" class="blob-code blob-code-inner js-file-line">    <span class="pl-c1">map</span>.redirect(<span class="pl-s"><span class="pl-pds">&#39;</span>/favicon.ico<span class="pl-pds">&#39;</span></span>, config.get(<span class="pl-s"><span class="pl-pds">&#39;</span>ckan.favicon<span class="pl-pds">&#39;</span></span>))</td>
      </tr>
      <tr>
        <td id="L420" class="blob-num js-line-number" data-line-number="420"></td>
        <td id="LC420" class="blob-code blob-code-inner js-file-line">
</td>
      </tr>
      <tr>
        <td id="L421" class="blob-num js-line-number" data-line-number="421"></td>
        <td id="LC421" class="blob-code blob-code-inner js-file-line">    <span class="pl-c1">map</span>.redirect(<span class="pl-s"><span class="pl-pds">&#39;</span>/*(url)/<span class="pl-pds">&#39;</span></span>, <span class="pl-s"><span class="pl-pds">&#39;</span>/<span class="pl-c1">{url}</span><span class="pl-pds">&#39;</span></span>,</td>
      </tr>
      <tr>
        <td id="L422" class="blob-num js-line-number" data-line-number="422"></td>
        <td id="LC422" class="blob-code blob-code-inner js-file-line">                 <span class="pl-v">_redirect_code</span><span class="pl-k">=</span><span class="pl-s"><span class="pl-pds">&#39;</span>301 Moved Permanently<span class="pl-pds">&#39;</span></span>)</td>
      </tr>
      <tr>
        <td id="L423" class="blob-num js-line-number" data-line-number="423"></td>
        <td id="LC423" class="blob-code blob-code-inner js-file-line">    <span class="pl-c1">map</span>.connect(<span class="pl-s"><span class="pl-pds">&#39;</span>/*url<span class="pl-pds">&#39;</span></span>, <span class="pl-v">controller</span><span class="pl-k">=</span><span class="pl-s"><span class="pl-pds">&#39;</span>template<span class="pl-pds">&#39;</span></span>, <span class="pl-v">action</span><span class="pl-k">=</span><span class="pl-s"><span class="pl-pds">&#39;</span>view<span class="pl-pds">&#39;</span></span>, <span class="pl-v">ckan_core</span><span class="pl-k">=</span><span class="pl-c1">True</span>)</td>
      </tr>
      <tr>
        <td id="L424" class="blob-num js-line-number" data-line-number="424"></td>
        <td id="LC424" class="blob-code blob-code-inner js-file-line">
</td>
      </tr>
      <tr>
        <td id="L425" class="blob-num js-line-number" data-line-number="425"></td>
        <td id="LC425" class="blob-code blob-code-inner js-file-line">    <span class="pl-k">return</span> <span class="pl-c1">map</span></td>
      </tr>
</table>

  <div class="BlobToolbar position-absolute js-file-line-actions dropdown js-menu-container js-select-menu d-none" aria-hidden="true">
    <button class="btn-octicon ml-0 px-2 p-0 bg-white border border-gray-dark rounded-1 dropdown-toggle js-menu-target" id="js-file-line-action-button" type="button" aria-expanded="false" aria-haspopup="true" aria-label="Inline file action toolbar" aria-controls="inline-file-actions">
      <svg aria-hidden="true" class="octicon" height="16" version="1.1" viewBox="0 0 13 4" width="14">
        <g stroke="none" stroke-width="1" fill-rule="evenodd">
            <g transform="translate(-1.000000, -6.000000)">
                <path d="M2.5,9.5 C1.67157288,9.5 1,8.82842712 1,8 C1,7.17157288 1.67157288,6.5 2.5,6.5 C3.32842712,6.5 4,7.17157288 4,8 C4,8.82842712 3.32842712,9.5 2.5,9.5 Z M7.5,9.5 C6.67157288,9.5 6,8.82842712 6,8 C6,7.17157288 6.67157288,6.5 7.5,6.5 C8.32842712,6.5 9,7.17157288 9,8 C9,8.82842712 8.32842712,9.5 7.5,9.5 Z M12.5,9.5 C11.6715729,9.5 11,8.82842712 11,8 C11,7.17157288 11.6715729,6.5 12.5,6.5 C13.3284271,6.5 14,7.17157288 14,8 C14,8.82842712 13.3284271,9.5 12.5,9.5 Z"></path>
            </g>
        </g>
      </svg>
    </button>
    <div class="dropdown-menu-content js-menu-content" id="inline-file-actions">
      <ul class="BlobToolbar-dropdown dropdown-menu dropdown-menu-se mt-2">
        <li><a class="js-zeroclipboard dropdown-item" style="cursor:pointer;" id="js-copy-lines" data-original-text="Copy lines">Copy lines</a></li>
        <li><a class="js-zeroclipboard dropdown-item" id= "js-copy-permalink" style="cursor:pointer;" data-original-text="Copy permalink">Copy permalink</a></li>
        <li><a href="/ckan/ckan/blame/2c1a6389456ce8706618998af2d8b3fa8dbb86a3/ckan/config/routing.py" class="dropdown-item js-update-url-with-hash" id="js-view-git-blame">View git blame</a></li>
          <li><a href="/ckan/ckan/issues/new" class="dropdown-item" id="js-new-issue">Open new issue</a></li>
      </ul>
    </div>
  </div>

  </div>

  </div>

  <button type="button" data-facebox="#jump-to-line" data-facebox-class="linejump" data-hotkey="l" class="d-none">Jump to Line</button>
  <div id="jump-to-line" style="display:none">
    <!-- '"` --><!-- </textarea></xmp> --></option></form><form accept-charset="UTF-8" action="" class="js-jump-to-line-form" method="get"><div style="margin:0;padding:0;display:inline"><input name="utf8" type="hidden" value="&#x2713;" /></div>
      <input class="form-control linejump-input js-jump-to-line-field" type="text" placeholder="Jump to line&hellip;" aria-label="Jump to line" autofocus>
      <button type="submit" class="btn">Go</button>
</form>  </div>

  </div>
  <div class="modal-backdrop js-touch-events"></div>
</div>

    </div>
  </div>

  </div>

      
<div class="footer container-lg px-3" role="contentinfo">
  <div class="position-relative d-flex flex-justify-between py-6 mt-6 f6 text-gray border-top border-gray-light ">
    <ul class="list-style-none d-flex flex-wrap ">
      <li class="mr-3">&copy; 2017 <span title="0.23788s from unicorn-4162071540-zz449">GitHub</span>, Inc.</li>
        <li class="mr-3"><a href="https://github.com/site/terms" data-ga-click="Footer, go to terms, text:terms">Terms</a></li>
        <li class="mr-3"><a href="https://github.com/site/privacy" data-ga-click="Footer, go to privacy, text:privacy">Privacy</a></li>
        <li class="mr-3"><a href="https://github.com/security" data-ga-click="Footer, go to security, text:security">Security</a></li>
        <li class="mr-3"><a href="https://status.github.com/" data-ga-click="Footer, go to status, text:status">Status</a></li>
        <li><a href="https://help.github.com" data-ga-click="Footer, go to help, text:help">Help</a></li>
    </ul>

    <a href="https://github.com" aria-label="Homepage" class="footer-octicon" title="GitHub">
      <svg aria-hidden="true" class="octicon octicon-mark-github" height="24" version="1.1" viewBox="0 0 16 16" width="24"><path fill-rule="evenodd" d="M8 0C3.58 0 0 3.58 0 8c0 3.54 2.29 6.53 5.47 7.59.4.07.55-.17.55-.38 0-.19-.01-.82-.01-1.49-2.01.37-2.53-.49-2.69-.94-.09-.23-.48-.94-.82-1.13-.28-.15-.68-.52-.01-.53.63-.01 1.08.58 1.23.82.72 1.21 1.87.87 2.33.66.07-.52.28-.87.51-1.07-1.78-.2-3.64-.89-3.64-3.95 0-.87.31-1.59.82-2.15-.08-.2-.36-1.02.08-2.12 0 0 .67-.21 2.2.82.64-.18 1.32-.27 2-.27.68 0 1.36.09 2 .27 1.53-1.04 2.2-.82 2.2-.82.44 1.1.16 1.92.08 2.12.51.56.82 1.27.82 2.15 0 3.07-1.87 3.75-3.65 3.95.29.25.54.73.54 1.48 0 1.07-.01 1.93-.01 2.2 0 .21.15.46.55.38A8.013 8.013 0 0 0 16 8c0-4.42-3.58-8-8-8z"/></svg>
</a>
    <ul class="list-style-none d-flex flex-wrap ">
        <li class="mr-3"><a href="https://github.com/contact" data-ga-click="Footer, go to contact, text:contact">Contact GitHub</a></li>
      <li class="mr-3"><a href="https://developer.github.com" data-ga-click="Footer, go to api, text:api">API</a></li>
      <li class="mr-3"><a href="https://training.github.com" data-ga-click="Footer, go to training, text:training">Training</a></li>
      <li class="mr-3"><a href="https://shop.github.com" data-ga-click="Footer, go to shop, text:shop">Shop</a></li>
        <li class="mr-3"><a href="https://github.com/blog" data-ga-click="Footer, go to blog, text:blog">Blog</a></li>
        <li><a href="https://github.com/about" data-ga-click="Footer, go to about, text:about">About</a></li>

    </ul>
  </div>
</div>



  <div id="ajax-error-message" class="ajax-error-message flash flash-error">
    <svg aria-hidden="true" class="octicon octicon-alert" height="16" version="1.1" viewBox="0 0 16 16" width="16"><path fill-rule="evenodd" d="M8.865 1.52c-.18-.31-.51-.5-.87-.5s-.69.19-.87.5L.275 13.5c-.18.31-.18.69 0 1 .19.31.52.5.87.5h13.7c.36 0 .69-.19.86-.5.17-.31.18-.69.01-1L8.865 1.52zM8.995 13h-2v-2h2v2zm0-3h-2V6h2v4z"/></svg>
    <button type="button" class="flash-close js-flash-close js-ajax-error-dismiss" aria-label="Dismiss error">
      <svg aria-hidden="true" class="octicon octicon-x" height="16" version="1.1" viewBox="0 0 12 16" width="12"><path fill-rule="evenodd" d="M7.48 8l3.75 3.75-1.48 1.48L6 9.48l-3.75 3.75-1.48-1.48L4.52 8 .77 4.25l1.48-1.48L6 6.52l3.75-3.75 1.48 1.48z"/></svg>
    </button>
    You can't perform that action at this time.
  </div>


    
    <script crossorigin="anonymous" integrity="sha256-czU4RQWbYESUvSm8kTsprEUDXcKw4U+fmhKYf65Sr1k=" src="https://assets-cdn.github.com/assets/frameworks-73353845059b604494bd29bc913b29ac45035dc2b0e14f9f9a12987fae52af59.js"></script>
    
    <script async="async" crossorigin="anonymous" integrity="sha256-0VwIZ1ArEsk1ZjrlP0aL1WeO5qlQqrxv04H3z/DCdIs=" src="https://assets-cdn.github.com/assets/github-d15c0867502b12c935663ae53f468bd5678ee6a950aabc6fd381f7cff0c2748b.js"></script>
    
    
    
    
  <div class="js-stale-session-flash stale-session-flash flash flash-warn flash-banner d-none">
    <svg aria-hidden="true" class="octicon octicon-alert" height="16" version="1.1" viewBox="0 0 16 16" width="16"><path fill-rule="evenodd" d="M8.865 1.52c-.18-.31-.51-.5-.87-.5s-.69.19-.87.5L.275 13.5c-.18.31-.18.69 0 1 .19.31.52.5.87.5h13.7c.36 0 .69-.19.86-.5.17-.31.18-.69.01-1L8.865 1.52zM8.995 13h-2v-2h2v2zm0-3h-2V6h2v4z"/></svg>
    <span class="signed-in-tab-flash">You signed in with another tab or window. <a href="">Reload</a> to refresh your session.</span>
    <span class="signed-out-tab-flash">You signed out in another tab or window. <a href="">Reload</a> to refresh your session.</span>
  </div>
  <div class="facebox" id="facebox" style="display:none;">
  <div class="facebox-popup">
    <div class="facebox-content" role="dialog" aria-labelledby="facebox-header" aria-describedby="facebox-description">
    </div>
    <button type="button" class="facebox-close js-facebox-close" aria-label="Close modal">
      <svg aria-hidden="true" class="octicon octicon-x" height="16" version="1.1" viewBox="0 0 12 16" width="12"><path fill-rule="evenodd" d="M7.48 8l3.75 3.75-1.48 1.48L6 9.48l-3.75 3.75-1.48-1.48L4.52 8 .77 4.25l1.48-1.48L6 6.52l3.75-3.75 1.48 1.48z"/></svg>
    </button>
  </div>
</div>


  </body>
</html>

