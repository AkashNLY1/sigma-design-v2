import os
SITE="SIGMA Coin";BASE="https://www.example.com"  # TODO: replace with final domain
NAV=[("index.html","Home"),("about.html","About"),("blog.html","Blog"),("faq.html","FAQ")]
SOC=[("Telegram","https://t.me/"),("YouTube","https://youtube.com/"),("WhatsApp","https://wa.me/"),("X","https://x.com/"),("Instagram","https://instagram.com/")]
def head(t,d,f):
    return f'''<!doctype html><html lang="en"><head><meta charset="utf-8"><meta name="viewport" content="width=device-width,initial-scale=1">
<title>{t}</title><meta name="description" content="{d}"><link rel="canonical" href="{BASE}/{f}">
<meta property="og:title" content="{t}"><meta property="og:description" content="{d}"><meta property="og:type" content="website">
<link rel="preconnect" href="https://fonts.googleapis.com"><link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
<link href="https://fonts.googleapis.com/css2?family=Inter:wght@400;500;600&family=Sora:wght@600;700&display=swap" rel="stylesheet">
<script>document.documentElement.classList.add("js");try{{var t=localStorage.getItem("sigma_theme");if(t)document.documentElement.dataset.theme=t}}catch(e){{}}</script><link rel="stylesheet" href="css/styles.css">
<script type="application/ld+json">{{"@context":"https://schema.org","@type":"Organization","name":"{SITE}","url":"{BASE}"}}</script>
<!-- Meta Pixel: replace YOUR_PIXEL_ID -->
<script>!function(f,b,e,v,n,t,s){{if(f.fbq)return;n=f.fbq=function(){{n.callMethod?n.callMethod.apply(n,arguments):n.queue.push(arguments)}};if(!f._fbq)f._fbq=n;n.push=n;n.loaded=!0;n.version='2.0';n.queue=[];t=b.createElement(e);t.async=!0;t.src=v;s=b.getElementsByTagName(e)[0];s.parentNode.insertBefore(t,s)}}(window,document,'script','https://connect.facebook.net/en_US/fbevents.js');fbq('init','YOUR_PIXEL_ID');fbq('track','PageView');</script></head>'''
def nav(f):
    li="".join(f'<li><a href="{h}"{" aria-current=page" if h==f else ""}>{n}</a></li>' for h,n in NAV)
    return f'''<body data-page="{f[:-5]}"><header class="nav"><div class="progress"></div><div class="wrap"><a class="logo" href="index.html"><i>Σ</i>SIGMA Coin</a>
<button class="burger" aria-label="Menu" aria-expanded="false">☰</button><ul id="menu">{li}<li><a class="btn gold" href="get-coins.html">Get Coins</a></li><li><button class="theme" type="button" aria-label="Switch to dark theme">☾</button></li></ul></div></header><main>'''
def foot():
    s="".join(f'<li><a href="{u}" target="_blank" rel="noopener">{n}</a></li>' for n,u in SOC)
    return f'''</main><footer><div class="wrap"><div class="cols"><div><a class="logo" href="index.html"><i>Σ</i>SIGMA Coin</a><p style="margin-top:14px">A simple, transparent way to hold SIGMA on the TRON network.</p></div>
<div><h3>Explore</h3><ul><li><a href="about.html">About</a></li><li><a href="blog.html">Blog</a></li><li><a href="faq.html">FAQ</a></li><li><a href="get-coins.html">Get Coins</a></li></ul></div>
<div><h3>Legal</h3><ul><li><a href="terms.html">Terms &amp; Conditions</a></li><li><a href="privacy.html">Privacy Policy</a></li></ul></div>
<div><h3>Community</h3><ul>{s}</ul></div></div>
<p class="risk">Risk warning: crypto assets are volatile and you may lose some or all of your money. Nothing on this site is financial advice. Do your own research. © 2026 {SITE}.</p></div></footer>
<div class="ov" id="leadPopup" role="dialog" aria-modal="true" aria-labelledby="pt"><div class="modal"><button class="x" aria-label="Close">×</button>
<form id="leadForm" novalidate><h3 id="pt">Stay in the loop with SIGMA</h3><p style="color:var(--mute);font-size:.95rem">Register to get updates and a personal walkthrough from our team.</p>
<label class="f" for="n">Full name</label><input id="n" name="name" type="text" autocomplete="name" required>
<label class="f" for="e">Email</label><input id="e" name="email" type="email" autocomplete="email" required>
<label class="f" for="p">Phone number</label><input id="p" name="phone" type="tel" autocomplete="tel" required>
<label class="chk"><input type="checkbox" name="terms" required><span>I accept the <a href="terms.html" target="_blank">Terms &amp; Conditions</a></span></label>
<label class="chk"><input type="checkbox" name="privacy" required><span>I accept the <a href="privacy.html" target="_blank">Privacy Policy</a></span></label>
<p class="err" id="leadErr" role="alert"></p><button class="btn" type="submit">Register</button></form></div></div>
<script src="js/main.js"></script></body></html>'''
def page(f,t,d,body):
    open(f,"w").write(head(t,d,f)+nav(f)+body+foot())
def ph(t,p):return f'<section class="page-head"><span class="blob b1"></span><span class="blob b2"></span><div class="wrap"><h1>{t}</h1><p class="lead">{p}</p></div></section>'
BUY="get-coins.html"
ITEMS="".join(f"<span>{w}</span>" for w in ["TRON Network","Pay with USDT","TronLink Wallet","TRC-20 Token","Fast transfers","Low fees","Human support"])
M='<div class="marq" aria-hidden="true"><div>'+ITEMS+ITEMS+'</div></div>'
page("index.html","SIGMA Coin | Buy SIGMA Token with USDT on TRON","SIGMA Coin is a TRON-based token you can buy with USDT. Learn how it works and how to get started in minutes.",f'''
<section class="hero"><span class="blob b1"></span><span class="blob b2"></span><div class="wrap"><div><h1>Digital value, made simple.</h1><p class="lead">SIGMA is a token on the TRON network. Buy it with USDT using the TronLink wallet in a few guided steps.</p>
<div class="cta"><a class="btn gold" href="{BUY}" data-buy>Get Coins</a><a class="btn ghost" href="about.html">Learn about SIGMA</a></div></div><div class="coin-wrap" aria-hidden="true"><div class="coin">Σ</div></div></div>{M}</section>
<div class="wrap"><div class="stats"><div><b>TRON</b><span>Network</span></div><div><b>USDT</b><span>Payment currency</span></div><div><b>TronLink</b><span>Supported wallet</span></div><div><b>[Add]</b><span>Total supply (confirm with client)</span></div></div></div>
<section class="sec"><div class="wrap"><h2>Why SIGMA</h2><p class="lead">Everything you need to know, without the jargon.</p><div class="grid">
<div class="card"><div class="ic">⚡</div><h3>Fast and low-cost</h3><p>Built on TRON, known for quick transfers and low network fees.</p></div>
<div class="card"><div class="ic">🔒</div><h3>You hold your coins</h3><p>Your tokens live in your own wallet, not on our platform.</p></div>
<div class="card"><div class="ic">💬</div><h3>Real people to help</h3><p>Register and our team will guide you through your first purchase.</p></div></div></div></section>
<section class="sec" style="padding-top:0"><div class="wrap split"><div><h2>Buy SIGMA in four steps</h2><p class="lead">No account needed. It takes a few minutes.</p></div>
<ol class="steps" style="padding:0;margin:0"><li><div><h3>Connect your wallet</h3><p>Open the purchase page and connect.</p></div></li><li><div><h3>Install TronLink</h3><p>Download the app if you do not have it yet.</p></div></li>
<li><div><h3>Search “Sigma Token”</h3><p>Find the token inside the TronLink app.</p></div></li><li><div><h3>Pay with USDT</h3><p>Confirm the amount and complete your purchase.</p></div></li></ol></div></section>
<section class="sec" style="padding-top:0"><div class="wrap"><div class="band"><h2>Ready to get started?</h2><p>Open the secure purchase page and follow the steps.</p><a class="btn gold" href="{BUY}" data-buy>Get Coins</a></div></div></section>''')
page("about.html","About SIGMA Coin | Our Mission and Token","Learn who is behind SIGMA Coin, our mission, and how the token works on the TRON network.",ph("About SIGMA Coin","Our mission is to make owning digital assets clear and approachable.")+'''
<section class="sec"><div class="wrap split"><div><h2>Our story</h2><p>[Client to supply: company background, founding team, and launch date.]</p><p>SIGMA was created so everyday users can buy and hold a digital token without needing deep technical knowledge.</p></div>
<div class="grid"><div class="card"><h3>Mission</h3><p>Clear, honest access to digital assets.</p></div><div class="card"><h3>Values</h3><p>Transparency, security, and support.</p></div></div></div></section>
<section class="sec" style="padding-top:0"><div class="wrap"><h2>Token details</h2><div class="grid"><div class="card"><h3>Network</h3><p>TRON (TRC-20)</p></div><div class="card"><h3>Pay with</h3><p>USDT</p></div><div class="card"><h3>Contract address</h3><p>[Add verified contract address]</p></div><div class="card"><h3>Total supply</h3><p>[Add]</p></div></div></div></section>''')
faqs=[("What is SIGMA Coin?","SIGMA is a token on the TRON network that you can buy with USDT."),("How do I buy SIGMA?","Go to Get Coins, connect your wallet, install TronLink if needed, search for “Sigma Token”, and pay with USDT."),("Do I need an account?","No. Your wallet is your account. Registering on this site is optional and lets our team help you."),("Which wallet should I use?","TronLink is the supported wallet."),("Is crypto risky?","Yes. Prices can change quickly and you can lose money. Only invest what you can afford to lose."),("Why did I get a call from your team?","If you registered and have not bought yet, our team may call to answer questions. You can ask us to stop at any time.")]
page("faq.html","SIGMA Coin FAQ | Buying and Wallet Questions","Answers to common questions about SIGMA Coin, TronLink, USDT and how to buy.",ph("Frequently asked questions","Quick answers about SIGMA.")+'<section class="sec"><div class="wrap" style="max-width:820px">'+"".join(f"<details><summary>{q}</summary><p>{a}</p></details>" for q,a in faqs)+"</div></section>")
posts=[("Guide","How to buy SIGMA with USDT using TronLink","A step-by-step walkthrough for first-time buyers."),("Education","Bitcoin vs Ethereum vs TRON: what is the difference?","A plain-language comparison of popular networks."),("Safety","5 ways to keep your crypto wallet safe","Simple habits that protect your funds.")]
page("blog.html","SIGMA Coin Blog | Crypto Guides and News","Guides, education and updates on SIGMA Coin, Bitcoin, Ethereum and the TRON ecosystem.",ph("Blog","Guides and updates from the SIGMA team.")+'<section class="sec"><div class="wrap grid">'+"".join(f'<article class="card post"><span class="tag">{c}</span><h3>{t}</h3><p>{d}</p><small>Coming soon</small></article>' for c,t,d in posts)+"</div></section>")
page(BUY,"Get SIGMA Coins | Buy with USDT on TRON","Buy SIGMA tokens with USDT. Follow the guided steps and open the secure purchase page.",ph("Get Coins","Follow these steps, then open the purchase page.")+f'''
<section class="sec"><div class="wrap split"><ol class="steps" style="padding:0;margin:0"><li><div><h3>Open the purchase page</h3><p>Connect your wallet there.</p></div></li><li><div><h3>Download TronLink</h3><p>Install it on your phone if prompted.</p></div></li><li><div><h3>Search “Sigma Token”</h3><p>Add the token in the app.</p></div></li><li><div><h3>Pay with USDT</h3><p>Check the amount and confirm.</p></div></li></ol>
<div class="card"><h3>Ready?</h3><p>You will be taken to our secure purchase site.</p><a class="btn" href="https://sigma-token.com/" target="_blank" rel="noopener" data-buy>Open purchase page</a></div></div></section>''')
def legal(f,t,secs):
    page(f,f"{t} | {SITE}",f"{t} for {SITE}.",ph(t,"Last updated: [date]")+'<section class="sec legal"><div class="wrap" style="max-width:780px"><p class="note"><b>DRAFT.</b> For client and legal review. Do not publish until approved.</p>'+"".join(f"<h2>{h}</h2><p>{p}</p>" for h,p in secs)+"</div></section>")
legal("terms.html","Terms & Conditions",[("1. Acceptance","By using this website you agree to these terms."),("2. No financial advice","Content is for information only and is not investment advice."),("3. Risks","Crypto assets are volatile. You may lose all funds you commit."),("4. Eligibility","You must be 18+ and legally allowed to buy crypto where you live."),("5. Purchases","Purchases happen on third-party sites and wallets. Transactions on a blockchain are final."),("6. Communications","If you register, you agree that we may contact you by phone, email or WhatsApp about SIGMA."),("7. Liability","To the extent permitted by law, we are not liable for losses from use of this site."),("8. Governing law","[Jurisdiction to be confirmed by legal counsel].")])
legal("privacy.html","Privacy Policy",[("1. Data we collect","Name, email, phone number, and your wallet address if you connect one. We also collect usage data through cookies and Meta Pixel."),("2. Why we collect it","To contact you about SIGMA, support purchases, and measure and improve our marketing."),("3. Meta Pixel and retargeting","We use Meta Pixel to understand site activity and show relevant ads. You can control ads in your Meta settings."),("4. Sharing","We share data only with service providers needed to run our business, or when required by law."),("5. Your rights","You can ask to access, correct or delete your data, or opt out of calls, by emailing [privacy email]."),("6. Retention and security","We keep data only as long as needed and use reasonable safeguards."),("7. Contact","[Company name and address].")])
open("robots.txt","w").write(f"User-agent: *\nAllow: /\nSitemap: {BASE}/sitemap.xml\n")
open("sitemap.xml","w").write('<?xml version="1.0" encoding="UTF-8"?><urlset xmlns="http://www.sitemaps.org/schemas/sitemap/0.9">'+"".join(f"<url><loc>{BASE}/{f}</loc></url>" for f in ["index.html","about.html","blog.html","faq.html",BUY,"terms.html","privacy.html"])+"</urlset>")
