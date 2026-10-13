import React from 'react';
import { ThemeProvider } from './context/ThemeContext';
import MainLayout from './layouts/MainLayout';
import AppRoutes from './routes/AppRoutes';

export default function App() {
  return (
    <ThemeProvider>
      <MainLayout>
        <AppRoutes />
      </MainLayout>
    </ThemeProvider>
  );
}
