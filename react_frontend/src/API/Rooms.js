import axios from "axios";

export default class RoomsAPI {
    static async join(userId, roomId) {
        await axios.put(
            `/api/rooms/${roomId}/`,
            userId
        )
    }
    static async getRooms() {
        const response = await axios.get("/api/rooms/")
        return response.data
    }
    static async getRoom(roomId) {
        const response = await axios.get(`/api/rooms/${roomId}`)
        return response.data
    }

    static async createRoom(userId) {
        const response = await axios.post(
            "/api/rooms/",
            userId
        )
        return response.data
    }
}

