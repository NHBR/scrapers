async function download(){
        let link = document.getElementById('inp').value;
        let checkbox_value = document.getElementById('htmlcheck').checked
        alert('Wait');
        document.getElementById('inp').value = 'Wait';
        let res = await eel.download_all(link,checkbox_value)();
        if (res === 404){
          alert('Status code 404');
          document.getElementById('inp').value = 'Status code 404';
        }else if(res === 400){
        alert('this pages is already downloaded please move folder to another place and try again');
        }else{
        alert('Done');
        document.getElementById('inp').value = 'Done';
        }
    }
    async function paste(){
        let link_on_yiff = await eel.paste()();
        document.getElementById('inp').value = link_on_yiff;
        }