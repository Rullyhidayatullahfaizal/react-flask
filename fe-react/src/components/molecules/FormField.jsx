"use client"
import Label from "../atoms/Label"
import Input from "../atoms/Input"

const FormField = ({ label, type = "text", placeholder, value, onChange, name, required = false }) => {
  return (
    <div className="mb-4">
      <Label htmlFor={name}>{label}</Label>
      <Input type={type} placeholder={placeholder} value={value} onChange={onChange} name={name} required={required} />
    </div>
  )
}

export default FormField
