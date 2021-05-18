

const Like= {
    like(){
        document.querySelector('.bi-hand-thumbs-up').classList.add('bi-hand-thumbs-up-fill')
        document.querySelector('.bi-hand-thumbs-up').classList.remove('bi-hand-thumbs-up')
        document.querySelector('#like').classList.add('text-primary')
        
    },
    deslike(){
        document.querySelector('.bi-hand-thumbs-down').classList.add('bi-hand-thumbs-down-fill')
        document.querySelector('.bi-hand-thumbs-down').classList.remove('bi-hand-thumbs-down')
        document.querySelector('#deslike').classList.add('text-danger')
        let a = true
    }
    
}