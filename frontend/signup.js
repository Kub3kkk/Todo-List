const username = document.getElementById('username')
const password = document.getElementById('password')
const email = document.getElementById('email')
const form = document.getElementById('signup')

form.addEventListener('submit', async (e) => {
    e.preventDefault()

    const data = {
        username: username.value,
        password: password.value,
        email: email.value
    }

    try {
        const response = await fetch('http://127.0.0.1:5000/signup',{
            method: 'POST',
            headers: {
                'Content-Type': 'application/json'
            },
            body: JSON.stringify(data)
        })

        if (response.ok) {
            const result = await response.json()
            console.log('Success', result)
        } else {
            console.error('Failed', response.status)

        }
    } catch (error) {
        console.error('Failed to connect', error)
    }
})