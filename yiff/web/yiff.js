async function yiff(){
        let link = document.getElementById('inp').value;
        alert('Wait');
        document.getElementById('inp').value = 'Wait';
        let k = await eel.scrapyiff(link)();
        if (k === 404){
          alert('Status code 404');
          document.getElementById('inp').value = 'Status code 404';
          }else{
        alert('Done');
        document.getElementById('inp').value = 'Done';
        }
        }

    async function paste(){
        let link2ch = await eel.paste()();
        document.getElementById('inp').value = link2ch;
        }