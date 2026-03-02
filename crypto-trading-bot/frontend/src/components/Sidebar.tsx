import { NavLink } from 'react-router-dom'
const items = ['Dashboard','TradingView','Strategies','Backtest','Portfolio','RiskManager','TradeHistory','Settings']
export default function Sidebar(){return <aside className='w-56 p-4 border-r border-[#1f2937] min-h-screen'>{items.map(i=><NavLink key={i} to={i==='Dashboard'?'/':'/'+i.toLowerCase()} className='block p-2'>{i}</NavLink>)}<div className='text-xs text-gray-400 mt-8'>v1.0.0</div></aside>}
