import axios from "axios";

export default class RoomsAPI {
    static async join(userId, roomId) {
        console.log(roomId)
        await axios.put(
            `/api/rooms/${roomId}/`,
            userId
        )
    }

    static async getRoom(roomId) {
        const response = await axios.get(`/api/rooms/${roomId}`)
        return response.data
    }

}

