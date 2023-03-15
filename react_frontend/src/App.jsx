import {BrowserRouter, Route, Routes} from "react-router-dom";
import RoomsList from "./pages/RoomsList/RoomsList";
import Register from "./pages/Register/Register";
import Header from "./components/Header/Header";
import NotFound from "./pages/NotFound/NotFound";
import Login from "./pages/Login/Login";
import Room from "./pages/Room/Room";


function App() {
    return (
        <BrowserRouter>
            <Header/>
            <Routes>
                <Route path={"/"} element={<RoomsList/>}/>
                <Route path={"/room/:id"} element={<Room/>}/>
                <Route path={"/login/"} element={<Login/>}/>
                <Route path={"/register/"} element={<Register/>}/>
                <Route path="*" element={<NotFound/>}/>
            </Routes>
        </BrowserRouter>
    )
}

export default App;
