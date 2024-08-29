import React from "react";
import { BrowserRouter, Route, Routes } from "react-router-dom";
import ScrollToTop from "./component/scrollToTop";
import { Login } from "./pages/login";
import { SignUp } from "./pages/signUp";
import { Single } from "./pages/single";
import Logout from "./pages/logout"; 
import injectContext from "./store/appContext";
import { Navbar } from "./component/navbar";
import { UserPage } from "./component/userPage";
import Private from "./component/private"; 

const Layout = () => {
    return (
        <div>
            <BrowserRouter>
                <ScrollToTop>
                    <Navbar />
                    <Routes>
                        <Route element={<Login />} path="/" />
                        <Route element={<Private><SignUp /></Private>} path="/signUp" />
                        <Route element={<Private><Single /></Private>} path="/single/:theid" />
                        <Route element={<Logout />} path="/logout" /> 
                       
                    </Routes>
                    <UserPage />
                </ScrollToTop>
            </BrowserRouter>
        </div>
    );
};

export default injectContext(Layout);
