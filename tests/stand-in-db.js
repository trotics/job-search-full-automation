// Stand-in for the Claude artifact database, for testing tracker-page.html on your own computer.
// It is NOT used by the published artifact. It copies the small part of the db API the page calls:
//   claude.use("db") -> db
//   db.collection(name).onSnapshot(onNext, onError)
//   db.doc("collection/id").update(fields) / .set(fields) / .get()
// Data comes from window.STAND_IN_DATA = {companies:[...], coverage:[...], listings:[...], answers:[...], settings:[...]}.
// Every write is recorded in window.standInWrites so a test can check what the page saved.
(function(){
  var data={}, listeners={};
  window.standInWrites=[];
  function clone(o){ return JSON.parse(JSON.stringify(o)); }
  function load(src){
    Object.keys(src||{}).forEach(function(name){
      data[name]={};
      (src[name]||[]).forEach(function(row){ var r=clone(row), id=r.id; delete r.id; data[name][id]=r; });
    });
  }
  function snap(name){
    var rows=data[name]||{};
    var docs=Object.keys(rows).map(function(id){ return {id:id, data:function(){ return clone(rows[id]); }}; });
    return {docs:docs, size:docs.length, empty:!docs.length};
  }
  function notify(name){ (listeners[name]||[]).forEach(function(fn){ setTimeout(function(){ fn(snap(name)); },0); }); }
  function split(path){ var p=String(path).split("/"); return {col:p[0], id:p[1]}; }
  var db={
    collection:function(name){
      return {
        onSnapshot:function(onNext){
          (listeners[name]=listeners[name]||[]).push(onNext);
          setTimeout(function(){ onNext(snap(name)); },0);
          return function(){ listeners[name]=(listeners[name]||[]).filter(function(f){return f!==onNext;}); };
        }
      };
    },
    doc:function(path){
      var p=split(path);
      return {
        get:function(){ var r=(data[p.col]||{})[p.id]; return Promise.resolve({id:p.id, exists:!!r, data:function(){ return r?clone(r):undefined; }}); },
        set:function(fields){ data[p.col]=data[p.col]||{}; data[p.col][p.id]=clone(fields); window.standInWrites.push({op:"set",path:path,fields:clone(fields)}); notify(p.col); return Promise.resolve(); },
        update:function(fields){
          var r=(data[p.col]||{})[p.id];
          if(!r) return Promise.reject(new Error("not_found"));
          Object.keys(fields).forEach(function(k){ r[k]=fields[k]; });
          window.standInWrites.push({op:"update",path:path,fields:clone(fields)});
          notify(p.col); return Promise.resolve();
        }
      };
    }
  };
  load(window.STAND_IN_DATA||{});
  window.standInDump=function(){ var out={}; Object.keys(data).forEach(function(n){ out[n]=Object.keys(data[n]).map(function(id){ var r=clone(data[n][id]); r.id=id; return r; }); }); return out; };
  window.claude={ use:function(name){ return Promise.resolve(name==="db"?db:null); } };
})();
