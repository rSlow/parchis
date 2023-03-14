import axios from "axios";

export async function checkEmailAPI(email) {
    const response = await axios.get(
        "/api/users/check/email/",
        {params: {email: email}}
    )
    return response.data === true
}

export async function checkUsernameAPI(username) {
    const response = await axios.get(
        "/api/users/check/username/",
        {params: {username: username}}
    )
    return response.data === true
}

export async function registerUserAPI(email, password, username) {
    return await axios.post(
        '/api/users/',
        {
            email: email,
            password: password,
            username: username
        }
    )
}

