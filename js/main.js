/* ===== CONFIG: edit before launch ===== */
const CONFIG={leadEndpoint:"",buyUrl:"https://sigma-token.com/",popupDelayMs:5000}; // leadEndpoint: your CRM/webhook URL (JSON POST)
(function(){
  const $=s=>document.querySelector(s);
  const burger=$(".burger"),menu=$("#menu");
  burger&&burger.addEventListener("click",()=>{const o=menu.classList.toggle("open");burger.setAttribute("aria-expanded",o)});
  const tb=$(".theme"),root=document.documentElement,mq=matchMedia("(prefers-color-scheme: dark)");
  const cur=()=>root.dataset.theme||(mq.matches?"dark":"light");
  const paint=()=>{const d=cur()==="dark";tb.textContent=d?"☀":"☾";tb.setAttribute("aria-label","Switch to "+(d?"light":"dark")+" theme")};
  if(tb){paint();tb.addEventListener("click",()=>{const n=cur()==="dark"?"light":"dark";root.dataset.theme=n;try{localStorage.setItem("sigma_theme",n)}catch(e){}paint()})}
  const rm=matchMedia("(prefers-reduced-motion: reduce)").matches,pg=$(".progress");
  addEventListener("scroll",()=>{const h=root;pg.style.transform="scaleX("+(h.scrollTop/((h.scrollHeight-h.clientHeight)||1))+")"},{passive:true});
  const io=new IntersectionObserver(es=>es.forEach(e=>{if(e.isIntersecting){e.target.classList.add("in");io.unobserve(e.target)}}),{threshold:.12});
  document.querySelectorAll(".card,.steps li,details,.band,.stats div,.sec h2,.sec .lead").forEach(el=>{el.setAttribute("data-r","");el.style.setProperty("--d",([].indexOf.call(el.parentNode.children,el)%4)*90+"ms");io.observe(el)});
  document.querySelectorAll(".card").forEach(c=>c.addEventListener("pointermove",e=>{const r=c.getBoundingClientRect();c.style.setProperty("--mx",e.clientX-r.left+"px");c.style.setProperty("--my",e.clientY-r.top+"px")}));
  const coin=$(".coin"),hero=$(".hero");
  if(coin&&!rm)hero.addEventListener("pointermove",e=>{const r=coin.getBoundingClientRect();coin.style.setProperty("--ry",(e.clientX-r.left-r.width/2)/r.width*24+"deg");coin.style.setProperty("--rx",-(e.clientY-r.top-r.height/2)/r.height*24+"deg")});
  if(coin)hero.addEventListener("pointerleave",()=>{coin.style.setProperty("--ry","0deg");coin.style.setProperty("--rx","0deg")});
  const px=(e,d)=>window.fbq&&fbq("track",e,d||{});
  document.addEventListener("click",e=>{if(e.target.closest("[data-buy]"))px("InitiateCheckout")});
  if(document.body.dataset.page==="get-coins")px("ViewContent",{content_name:"SIGMA Token"});
  const KEY="sigma_lead",ov=$("#leadPopup");if(!ov)return;
  const getLead=()=>{try{return JSON.parse(localStorage.getItem(KEY))}catch(e){return null}};
  const close=()=>{ov.classList.remove("on");try{sessionStorage.setItem("sigma_dismissed","1")}catch(e){}};
  let dismissed=false;try{dismissed=!!sessionStorage.getItem("sigma_dismissed")}catch(e){}
  if(!getLead()&&!dismissed)setTimeout(()=>{ov.classList.add("on");ov.querySelector("input").focus()},CONFIG.popupDelayMs);
  ov.querySelector(".x").addEventListener("click",close);
  ov.addEventListener("click",e=>{if(e.target===ov)close()});
  document.addEventListener("keydown",e=>{if(e.key==="Escape")close()});
  const wallet=()=>{try{return window.tronWeb&&tronWeb.defaultAddress&&tronWeb.defaultAddress.base58||""}catch(e){return""}};
  const send=l=>{if(!CONFIG.leadEndpoint)return console.info("Lead (no endpoint set):",l);
    return fetch(CONFIG.leadEndpoint,{method:"POST",headers:{"Content-Type":"application/json"},body:JSON.stringify(l),keepalive:true}).catch(console.error)};
  $("#leadForm").addEventListener("submit",e=>{
    e.preventDefault();const f=e.target,err=$("#leadErr");
    const name=f.name.value.trim(),email=f.email.value.trim(),phone=f.phone.value.trim();
    if(name.length<2)return err.textContent="Enter your full name.";
    if(!/^\S+@\S+\.\S+$/.test(email))return err.textContent="Enter a valid email address.";
    if(!/^[+]?[\d\s-]{8,15}$/.test(phone))return err.textContent="Enter a valid phone number.";
    if(!f.terms.checked||!f.privacy.checked)return err.textContent="Please accept the Terms & Conditions and Privacy Policy.";
    err.textContent="";
    const lead={name,email,phone,wallet:wallet(),termsAccepted:true,privacyAccepted:true,page:location.href,ts:new Date().toISOString(),purchased:false};
    localStorage.setItem(KEY,JSON.stringify(lead));send(lead);px("Lead");
    f.innerHTML='<h3>Thank you, '+name.replace(/[<>&"]/g,"")+'!</h3><p>Our team will reach out shortly. You can buy SIGMA any time.</p><a class="btn gold" data-buy href="get-coins.html">Get Coins</a>';
  });
  let n=0;const t=setInterval(()=>{const w=wallet(),l=getLead();
    if(w&&l&&!l.wallet){l.wallet=w;localStorage.setItem(KEY,JSON.stringify(l));send({...l,event:"wallet_connected"});clearInterval(t)}
    if(++n>60)clearInterval(t)},3000);
})();
