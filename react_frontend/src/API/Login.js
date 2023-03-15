import axios from "axios";

export async function loginAPI(username, password, setToken) {
    const form = new FormData()
    form.append("username", username)
    form.append("password", password)

    try {
        const response = await axios.post(
            "/api/users/token/",
            form
        )
        return response.data["access_token"]

    } catch (e) {
        if (e.response.status === 401) {
            console.log(e.response.data["detail"])
        }
    }

}