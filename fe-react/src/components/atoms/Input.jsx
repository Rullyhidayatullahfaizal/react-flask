const Input = ({ type = "text", placeholder, value, onChange, name, className = "", required = false }) => {
    return (
      <input
        type={type}
        placeholder={placeholder}
        value={value}
        onChange={onChange}
        name={name}
        required={required}
        className={`w-full px-3 py-2 border  rounded-lg focus:outline-none focus:ring-2 focus:ring-blue-300 focus:border-transparent ${className}`}
      />
    )
  }
  
  export default Input
  