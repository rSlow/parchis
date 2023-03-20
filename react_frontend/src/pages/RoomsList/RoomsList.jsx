import React, {useContext} from 'react';
import RoomTab from "../../components/Rooms/RoomTab/RoomTab";
import {UserContext} from "../../context/userContext";
import RoomsAPI from "../../API/Rooms";
import {useNavigate} from "react-router-dom";
import Button from "../../components/UI/Button/Button";
import Loader from "../../components/UI/Loader/Loader";
import {useRooms} from "../../hooks/useRooms";

const RoomsList = () => {
    const {user, isAuth} = useContext(UserContext)
    const navigate = useNavigate()

    const [rooms, isRoomsLoading, canAddRoom] = useRooms(user)

    async function addRoom() {
        const room = await RoomsAPI.createRoom(user.id)
        const roomId = room.id
        navigate(`/room/${roomId}`, {state: roomId})
    }

    return (
        isRoomsLoading
            ? <Loader/>
            : <div className={"rooms_list"}>
                {isAuth && canAddRoom &&
                    <Button className="button is-dark is-light is-outlined" onClick={addRoom}>
                        Создать комнату
                    </Button>
                }
                {rooms.length !== 0
                    ? rooms.map(room => <RoomTab room={room} key={room.id}/>)
                    : <h1 className="title has-text-centered">{isAuth
                        ? "Нет ни одной комнаты, создай первую!"
                        : "Еще никто не создал игру. Регистрируйся и будешь первым!"}
                    </h1>
                }
            </div>
    );
};

export default RoomsList;