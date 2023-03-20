import React, {useContext} from 'react';
import {useLocation, useNavigate} from "react-router-dom";
import {UserContext} from "../../context/userContext";
import RoomsAPI from "../../API/Rooms";
import Button from "../../components/UI/Button/Button";
import RoomPlayer from "../../components/Rooms/RoomPlayer/RoomPlayer";
import Loader from "../../components/UI/Loader/Loader";
import {useRoom} from "../../hooks/useRoom";

const Room = () => {
    const {user} = useContext(UserContext)
    const roomId = useLocation().state
    const navigate = useNavigate()

    const [room, roomName, isLoading, setRoomName, changeRoomName] = useRoom(roomId)

    async function leaveRoom() {
        await RoomsAPI.leaveRoom(user.id, roomId)
        navigate("/")
    }

    return (
        isLoading
            ? <Loader/>
            : <div>
                <div className="is-flex">
                    <Button className="is-danger is-outlined" onClick={leaveRoom}>
                        Выйти из комнаты
                    </Button>
                    <input
                        value={roomName}
                        className="input mx-2"
                        onChange={e => setRoomName(e.target.value)}
                    />
                    <Button className="is-outlined is-success"
                            disabled={room?.name === roomName}
                            onClick={changeRoomName}>
                        Сменить название
                    </Button>
                </div>
                {room.players && room.players.map(player =>
                    <RoomPlayer player={player} key={player.id}/>
                )}
            </div>
    );
};

export default Room;