async function download(){
    let link_2ch = document.getElementById('inp').value;
    let checkbox_value = document.getElementById('htmlcheck').checked
    let res = await eel.download_all(link_2ch,checkbox_value)();
    if (res === 404){
        alert('Status code 404');
        document.getElementById('inp').value = 'Status code 404';
    }else if(res=== 400){
        alert('this thread is already downloaded please move folder to another place and try again')}
    else{
        alert('Done');
        document.getElementById('inp').value = 'Done';
        }
    }

async function paste(){
    let link2ch = await eel.paste()();
    document.getElementById('inp').value = link2ch;
    }
