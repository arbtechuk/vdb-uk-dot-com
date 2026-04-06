// Welsh Language Kill Switch
// Set WELSH_ENABLED to true when translations have been verified.
// Secret unlock: visit any page with ?cymraeg in the URL.
// Clear unlock: visit any page with ?nocymraeg in the URL.
// Secret toggle: Shift+W toggles between EN and CY.
(function () {
  var WELSH_ENABLED = false;

  if (location.search.includes('cymraeg') && !location.search.includes('nocymraeg')) {
    localStorage.setItem('vdb-welsh-unlock', '1');
  }
  if (location.search.includes('nocymraeg')) {
    localStorage.removeItem('vdb-welsh-unlock');
    localStorage.removeItem('vdb-lang');
  }
  if (localStorage.getItem('vdb-welsh-unlock') === '1') {
    WELSH_ENABLED = true;
  }

  window.VDB_WELSH_ENABLED = WELSH_ENABLED;

  // Shift+W: toggle language (works even when toggle is hidden)
  document.addEventListener('keydown', function (e) {
    if (e.shiftKey && e.key === 'W' && !e.ctrlKey && !e.metaKey && !e.altKey) {
      var tag = e.target.tagName;
      if (tag === 'INPUT' || tag === 'TEXTAREA' || e.target.isContentEditable) return;
      var current = document.documentElement.getAttribute('data-lang') || 'en';
      var next = current === 'en' ? 'cy' : 'en';
      if (typeof window.setLang === 'function') {
        window.setLang(next);
      }
    }
  });
})();
