const openDetailsIfAnchorHidden = evt => {
  const targetDIV = document.querySelector(evt.target.getAttribute("href"));
  if ( !! targetDIV.offsetHeight || targetDIV.getClientRects().length ) return;
  targetDIV.closest("details").open = true;
}


[...document.querySelectorAll("[href^='#']")].forEach(
   el => el.addEventListener("click", openDetailsIfAnchorHidden )
);
