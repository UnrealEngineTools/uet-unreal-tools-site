const toggle=document.querySelector('#nav-toggle');
const nav=document.querySelector('#docs-nav');
function closeNav(){nav.classList.remove('open');toggle.setAttribute('aria-expanded','false');}
toggle.addEventListener('click',()=>{const open=nav.classList.toggle('open');toggle.setAttribute('aria-expanded',String(open));});
document.addEventListener('keydown',e=>{if(e.key==='Escape'&&nav.classList.contains('open')){closeNav();toggle.focus();}});
nav.addEventListener('click',e=>{if(e.target.closest('a'))closeNav();});
document.querySelectorAll('.copy').forEach(button=>button.addEventListener('click',async()=>{
  try{await navigator.clipboard.writeText(button.closest('.code').querySelector('code').textContent);button.textContent='Copied';}
  catch{button.textContent='Select code to copy';}
  setTimeout(()=>button.textContent='Copy',1800);
}));
const input=document.querySelector('#doc-search'),results=document.querySelector('#search-results');
let indexPromise;
input.addEventListener('input',async()=>{
  const query=input.value.trim().toLowerCase();results.replaceChildren();if(!query)return;
  try{
    indexPromise??=fetch('/deck-toolkit/assets/search.json').then(r=>{if(!r.ok)throw Error('Search unavailable');return r.json();});
    const pages=await indexPromise;if(input.value.trim().toLowerCase()!==query)return;
    const words=query.split(/\s+/);const matches=pages.filter(p=>words.every(w=>(p.title+' '+p.summary+' '+p.text).toLowerCase().includes(w))).sort((a,b)=>Number(b.title.toLowerCase().includes(query))-Number(a.title.toLowerCase().includes(query)));
    if(!matches.length){const p=document.createElement('p');p.textContent='No matching topics. Try “save”, “Blueprint” or “trace”.';results.append(p);}
    for(const item of matches.slice(0,6)){const a=document.createElement('a');a.href=item.url;a.textContent=item.title;const s=document.createElement('small');s.textContent=item.summary;a.append(s);results.append(a);}
  }catch{results.textContent='Search is unavailable. Browse the topics below.';indexPromise=undefined;}
});
