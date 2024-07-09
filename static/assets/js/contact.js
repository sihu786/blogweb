
const bt=document.getElementById('form-submit')

bt.addEventListener('click',(e)=>{
  let name=document.getElementById('name').value;
  let email=document.getElementById('email').value;
  let sub=document.getElementById('subject').value;
  let mes=document.getElementById('message').value;
  

  if(name==""){

    alert("Enter Your Name")
  }else if(email==""){
    alert("Enter Your Email")
  }else if(sub==""){
    alert("Enter Your Subject")
  }else if(mes==""){
    alert("Enter Your Message")
  }else{


  let body="Name: " + name + "<br/> Email: " + email + "<br/> Subject: " + sub + "<br/> Message: " + mes + "<br/>"



    e.preventDefault()
   
  
    Email.send({
      SecureToken : "77b3b9d7-4698-4e30-9fdc-9461b7b8b694 ",
      
      To : 'bikramadak15@gmail.com',
      From : 'bikramadak15@gmail.com',
      Subject : sub,
      Body : body,
      
  }).then(
    message => {
      if(message=='OK'){
        swal("Successfull", "Your Data is Successfull Recived!", "success");
        console.log(body)
  
      }else{
        swal("Somthing Wrong", "Your Data Not Recived!", "error");
  
  }
  
    });
  
}



 

 

})

// 77b3b9d7-4698-4e30-9fdc-9461b7b8b694 