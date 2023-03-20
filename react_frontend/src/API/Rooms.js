import axios from "axios";

export default class RoomsAPI {
    static async joinRoom(userId, roomId) {
        await axios.put(
            `/api/rooms/${roomId}/`, {"user_id": userId}
        )
    }

    static async getRooms() {
        const response = await axios.get("/api/rooms/")
        return response.data
    }


    static async getRoom(roomId) {
        const response = await axios.get(`/api/rooms/${roomId}/`)
        return response.data
    }

    static async createRoom(userId) {
        const response = await axios.post(
            "/api/rooms/", {"user_id": userId}
        )
        return response.data
    }

    static async leaveRoom(userId, roomId) {
        await axios.delete(
            "/api/rooms/",
            {
                params: {
                    "room_id": roomId,
                    "user_id": userId
                }
            }
        )
    }

    static async changeRoomName(roomId, name) {
        await axios.patch(`/api/rooms/${roomId}/`, {name})
    }
}

