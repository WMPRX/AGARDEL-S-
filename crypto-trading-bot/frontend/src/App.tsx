import { Routes, Route } from 'react-router-dom'
import Sidebar from './components/Sidebar'
import Dashboard from './pages/Dashboard'
import TradingView from './pages/TradingView'
import Strategies from './pages/Strategies'
import Backtest from './pages/Backtest'
import Portfolio from './pages/Portfolio'
import RiskManager from './pages/RiskManager'
import TradeHistory from './pages/TradeHistory'
import Settings from './pages/Settings'

export default function App(){
  return <div className='flex bg-[#0a0e1a] min-h-screen text-[#f9fafb]'><Sidebar /><main className='p-6 flex-1'><Routes>
    <Route path='/' element={<Dashboard/>}/><Route path='/tradingview' element={<TradingView/>}/><Route path='/strategies' element={<Strategies/>}/><Route path='/backtest' element={<Backtest/>}/><Route path='/portfolio' element={<Portfolio/>}/><Route path='/riskmanager' element={<RiskManager/>}/><Route path='/tradehistory' element={<TradeHistory/>}/><Route path='/settings' element={<Settings/>}/>
  </Routes></main></div>
}
