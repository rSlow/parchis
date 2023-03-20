import {useEffect, useState} from "react";
import {useFetching} from "./useFetching";
import RoomsAPI from "../API/Rooms";

export function useRooms(user) {
    const [rooms, setRooms] = useState([])
    const [canAddRoom, setCanAddRoom] = useState(true)
    const [initRooms, isRoomsLoading] = useFetching(async () => {
        const roomsData = await RoomsAPI.getRooms()
        validateAndSetRooms(roomsData, user?.id)
    })

    function validateAndSetRooms(notValidatedRoomsData, userId) {
        const validatedRoomsData = []
        let currentRoomId = null
        for (const room of notValidatedRoomsData) {
            for (const player of room["players"]) {
                if (player["current_room_id"] === room.id && player.user.id === userId) {
                    currentRoomId = player["current_room_id"]
                    setCanAddRoom(false)
                    break
                }
            }
            if (currentRoomId !== null) {
                break
            }
        }
        if (currentRoomId !== null) {
            for (const room of notValidatedRoomsData) {
                room["is_joinable"] = false
                if (room.id === currentRoomId) {
                    room["is_current"] = true
                }
                validatedRoomsData.push(room)
            }
            setRooms(validatedRoomsData)
        } else {
            setRooms(notValidatedRoomsData)
        }
    }

    useEffect(() => {
        initRooms()

        let url = "ws://localhost:8000/ws/rooms/"
        if (user?.id) {
            url += `?user_id=${user?.id}`
        }
        const roomsWS = new WebSocket(url)
        roomsWS.onmessage = event => {
            validateAndSetRooms(JSON.parse(event.data), user?.id)
        }

        return () => {
            roomsWS.close()
        }

    }, [user])


    return [rooms, isRoomsLoading, canAddRoom]
}