import React from "react";
import { BrowserRouter, Route, Routes } from "react-router-dom";
import ScrollToTop from "./component/scrollToTop";
import { Home } from "./pages/home";
import { Demo } from "./pages/demo";
import { Single } from "./pages/single";
import Logout from "./pages/logout"; 
import injectContext from "./store/appContext";
import { Navbar } from "./component/navbar";
import { Login } from "./component/login";
import Private from "./component/private"; 

const Layout = () => {
    return (
        <div>
            <BrowserRouter>
                <ScrollToTop>
                    <Navbar />
                    <Routes>
                        <Route element={<Home />} path="/" />
                        <Route element={<Private><Demo /></Private>} path="/demo" />
                        <Route element={<Private><Single /></Private>} path="/single/:theid" />
                        <Route element={<Logout />} path="/logout" /> 
                       
                    </Routes>
                    <Login />
                </ScrollToTop>
            </BrowserRouter>
        </div>
    );
};

export default injectContext(Layout);
