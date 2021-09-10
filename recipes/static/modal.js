console.log('hello world')


#a.jax({
    type: 'GET',
    url: '',
    success: function(response){
        console.log(response)
        const data = JSON.parse(response.data)
        console.log(data)
    },
    error: function(error){
        console.log(error)
    }
})