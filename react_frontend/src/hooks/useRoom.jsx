import {useEffect, useState} from "react";
import {useFetching} from "./useFetching";
import RoomsAPI from "../API/Rooms";

export function useRoom(roomId) {
    const [room, setRoom] = useState({})
    const [roomName, setRoomName] = useState("")

    const [initRoom, isLoading] = useFetching(async () => {
        const roomData = await RoomsAPI.getRoom(roomId)
        setRoom(roomData)
        setRoomName(roomData.name)
    })

    useEffect(() => {
        initRoom()
    }, [])

    useEffect(() => {
        setRoomName(room.name)
    }, [room?.name])

    async function changeRoomName() {
        await RoomsAPI.changeRoomName(roomId, roomName)
        initRoom()
    }

    useEffect(() => {
        const roomWS = new WebSocket(`ws://localhost:8000/ws/rooms/${roomId}`)
        roomWS.onmessage = event => {
            console.log(event.data)
            setRoom(JSON.parse(event.data))
        }
        return () => {
            roomWS.close()
        }
    }, [roomId])

    return [room, roomName, isLoading, setRoomName, changeRoomName]
}