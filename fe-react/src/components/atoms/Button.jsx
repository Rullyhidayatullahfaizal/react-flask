import React from "react"

const Button = ({ children, onClick, variant = "primary", type = "button", className = "" }) => {
  const baseClasses =
    "px-4 py-1 rounded font-normal transition-colors focus:outline-none focus:ring-2 focus:ring-opacity-50 hover:cursor-pointer"

  const variantClasses = {
    primary: "bg-[#6FCBFF] hover:bg-blue-600 text-[#0F0F0F] focus:ring-blue-300 rounded-lg",
    danger: "bg-[#FF6F6F] hover:bg-red-600 text-[#0F0F0F] focus:ring-red-300",
    secondary: "bg-[#FFB46F] hover:bg-gray-300 text-[#0F0F0F] focus:ring-gray-300",
  }

  return (
    <button type={type} onClick={onClick} className={`${baseClasses} ${variantClasses[variant]} ${className}`}>
      {children}
    </button>
  )
}

export default Button
