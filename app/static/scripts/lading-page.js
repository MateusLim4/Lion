let like = false
let deslike = false

const Like= {
    like(){
        document.querySelector('.bi-hand-thumbs-up').classList.add('bi-hand-thumbs-up-fill')
        document.querySelector('.bi-hand-thumbs-up').classList.remove('bi-hand-thumbs-up')
        document.querySelector('#like').classList.add('text-primary')
        if (deslike===true){
            document.querySelector('.bi-hand-thumbs-down-fill').classList.add('bi-hand-thumbs-down')
            document.querySelector('.bi-hand-thumbs-down-fill').classList.remove('bi-hand-thumbs-down-fill')
            document.querySelector('#deslike').classList.remove('text-danger')
        }
        like = true
        deslike = false
    },
    deslike(){
        document.querySelector('.bi-hand-thumbs-down').classList.add('bi-hand-thumbs-down-fill')
        document.querySelector('.bi-hand-thumbs-down').classList.remove('bi-hand-thumbs-down')
        document.querySelector('#deslike').classList.add('text-danger')
        if (like === true){
            document.querySelector('.bi-hand-thumbs-up-fill').classList.add('bi-hand-thumbs-up')
            document.querySelector('.bi-hand-thumbs-up-fill').classList.remove('bi-hand-thumbs-up-fill')
            document.querySelector('#like').classList.remove('text-primary')
        }
        deslike = true
        like = false
    }
    
}