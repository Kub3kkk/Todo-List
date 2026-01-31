const password = document.getElementById('password')
const email = document.getElementById('email')
const form = document.getElementById('login')
const remember = document.getElementById('remember')

form.addEventListener('submit', async (e) => {
    e.preventDefault()

    const data = {
        password: password.value,
        email: email.value,
        remember: remember.checked
    }

    try {
        const response = await fetch('http://127.0.0.1:5000/login',{
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