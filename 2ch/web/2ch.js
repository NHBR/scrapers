async function ch2(){
    let l2ch = document.getElementById('inp').value;
    let k = await eel.main(l2ch)();
    if (k === 404){
      document.getElementById('inp').value = 'Ошибка 404 нет доступа';
      }
    }

async function paste(){
    let link2ch = await eel.paste()();
    document.getElementById('inp').value = link2ch;
    }
