import {BrowserRouter, Route, Routes} from "react-router-dom";
import Rooms from "./pages/Rooms/Rooms";
import Register from "./pages/Register/Register";
import Header from "./components/Header/Header";
import NotFound from "./pages/NotFound/NotFound";


function App() {
    return (
        <BrowserRouter>
            <Header/>
            <Routes>
                <Route path={"/"} element={<Rooms/>}/>
                <Route path={"/register/"} element={<Register/>}/>
                <Route path="*" element={<NotFound/>}/>
            </Routes>
        </BrowserRouter>
    )
}

export default App;
