import axios from "axios";

export default class RegisterAPI {
    static async checkEmail(email) {
        const response = await axios.get(
            "/api/users/check/email/",
            {params: {email: email}}
        )
        return response.data === true
    }

    static async checkUsername(username) {
        const response = await axios.get(
            "/api/users/check/username/",
            {params: {username: username}}
        )
        return response.data === true
    }

    static async registerUser(email, password, username) {
        return await axios.post(
            '/api/users/',
            {
                email: email,
                password: password,
                username: username
            }
        )
    }

}