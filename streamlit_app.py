<!DOCTYPE html>
<html lang="ko">
<head>
<script>
window.onerror=function(msg,src,line,col,err){window.parent.postMessage({type:'app-error',message:msg,source:src,lineno:line,colno:col,stack:err&&err.stack||''},'*');};
window.onunhandledrejection=function(e){window.parent.postMessage({type:'app-error',message:'Unhandled promise rejection: '+(e.reason&&e.reason.message||e.reason||'unknown'),stack:e.reason&&e.reason.stack||''},'*');};
window.addEventListener('error',function(e){var t=e&&e.target;if(t&&t!==window&&t.tagName==='SCRIPT'){var u=t.src||'';window.parent.postMessage({type:'app-error',message:'Failed to load script'+(u?': '+u:' (inline module)'),source:u},'*');}},true);
(function(){var _f=window.fetch;window.fetch=function(){var a=arguments,u=typeof a[0]==='string'?a[0]:(a[0]&&a[0].url)||'';var p=_f.apply(this,a);p.then(function(r){if(r.status===500){r.clone().text().then(function(b){window.parent.postMessage({type:'fetch-error',url:u,status:500,body:b},'*');}).catch(function(){window.parent.postMessage({type:'fetch-error',url:u,status:500,body:''},'*');});}}).catch(function(e){window.parent.postMessage({type:'fetch-error',url:u,status:0,body:e.message||'fetch failed'},'*');});return p;};})();
</script>
<script src="https://builder.puter.com/runtime.js" defer></script>
<meta charset="UTF-8" />
<meta name="viewport" content="width=device-width, initial-scale=1.0" />
<title>waiter — 대리 웨이팅 플랫폼</title>
<meta name="description" content="줄 서는 시간을 돈으로 바꾸세요. 인기 상품, 팝업, 맛집 웨이팅을 안전하게 맡기는 대리 웨이팅 플랫폼." />
<meta name="theme-color" content="#0B0D12" />
<link rel="preconnect" href="https://cdn.jsdelivr.net" />
<link href="https://cdn.jsdelivr.net/gh/orioncactus/pretendard@v1.3.9/dist/web/variable/pretendardvariable-dynamic-subset.min.css" rel="stylesheet" />
<script src="https://cdn.tailwindcss.com"></script>
<script>
tailwind.config = {
  theme: {
    extend: {
      fontFamily: { sans: ['"Pretendard Variable"', 'Pretendard', 'system-ui', 'sans-serif'] },
      colors: {
        bg: '#0B0D12', panel: '#12151C', card: '#171B24', line: '#232835',
        ink: '#E9ECF2', mute: '#8B93A5', dim: '#5B6273',
        brand: { DEFAULT: '#FF6A3D', soft: 'rgba(255,106,61,0.12)' },
        ok: '#34D399', warn: '#FBBF24', bad: '#F87171', info: '#60A5FA'
      }
    }
  }
}
</script>
<link rel="stylesheet" href="styles.css" />
    <!-- puter-pwa: generated, do not edit -->
    <link rel="manifest" href="manifest.json">
    <link rel="icon" type="image/png" sizes="192x192" href="icons/icon-192.png">
    <link rel="apple-touch-icon" href="icons/apple-touch-icon-180.png">
    <meta name="mobile-web-app-capable" content="yes">
    <meta name="apple-mobile-web-app-capable" content="yes">
    <meta name="apple-mobile-web-app-status-bar-style" content="default">
    <meta name="apple-mobile-web-app-title" content="waiter">
    <!-- /puter-pwa -->
</head>
<body class="bg-bg text-ink font-sans antialiased">
<div class="flex min-h-screen">
  <!-- Sidebar -->
  <aside class="hidden lg:flex w-64 shrink-0 flex-col border-r border-line bg-panel sticky top-0 h-screen">
    <div class="px-6 pt-7 pb-6 flex items-center gap-3">
      <img src="icon.svg" alt="" class="w-9 h-9" />
      <div>
        <div class="text-lg font-bold tracking-tight leading-none">waiter</div>
        <div class="text-xs text-mute mt-1">대리 웨이팅 플랫폼</div>
      </div>
    </div>
    <div class="px-6 text-[11px] font-semibold uppercase tracking-wider text-dim mb-2">메뉴</div>
    <nav id="sideNav" class="px-3 flex flex-col gap-0.5"></nav>
    <div class="mt-auto p-4">
      <div class="rounded-xl border border-line bg-card p-4">
        <div class="flex items-center gap-2 text-sm font-semibold"><i data-lucide="shield-check" class="w-4 h-4 text-ok"></i>안심 보장</div>
        <p class="text-xs text-mute mt-1.5 leading-relaxed">안전결제 · 익명채팅 · 신고시스템으로 모든 거래를 보호해요.</p>
      </div>
      <div class="flex items-center gap-3 mt-4 px-1">
        <div class="w-8 h-8 rounded-full bg-brand-soft text-brand grid place-items-center text-xs font-bold">익</div>
        <div class="text-sm">
          <div class="font-medium">익명 사용자</div>
          <div class="text-xs text-mute">#A7F2</div>
        </div>
      </div>
    </div>
  </aside>

  <!-- Main -->
  <div class="flex-1 min-w-0 flex flex-col">
    <header class="sticky top-0 z-20 h-16 border-b border-line bg-bg/90 backdrop-blur flex items-center px-5 lg:px-10 gap-4">
      <img src="icon.svg" alt="" class="w-8 h-8 lg:hidden" />
      <h1 id="pageTitle" class="text-base font-semibold">홈</h1>
      <div class="ml-auto flex items-center gap-2">
        <span class="hidden sm:inline-flex items-center gap-1.5 text-xs text-mute border border-line rounded-full px-3 py-1.5"><span class="w-1.5 h-1.5 rounded-full bg-ok pulse"></span>실시간 시세 업데이트 중</span>
        <button data-go="request" class="btn-primary h-9 px-4 text-sm"><i data-lucide="plus" class="w-4 h-4"></i><span class="hidden sm:inline">의뢰하기</span></button>
      </div>
    </header>

    <main id="view" class="flex-1 px-5 lg:px-10 py-8 pb-28 lg:pb-12 w-full max-w-6xl mx-auto"></main>
  </div>
</div>

<!-- Mobile tab bar -->
<nav id="tabNav" class="lg:hidden fixed bottom-0 inset-x-0 z-30 border-t border-line bg-panel grid grid-cols-6"></nav>

<div id="toast" class="fixed left-1/2 -translate-x-1/2 bottom-24 lg:bottom-8 z-50 hidden"></div>

<script type="module" src="app.js"></script>
</body>
</html>
