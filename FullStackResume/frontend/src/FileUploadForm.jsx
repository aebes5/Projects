import React, { useState } from 'react';
import Select from 'react-select';

const FileUploadForm = ( {onUploadComplete}) => {

    const [isUploading, setIsUploading] = useState(false);

    const [formData, setFormData] = useState({
        file: null,
        jobDesc: '',
        sections: [],
        otherSection: '',
    });

    const options = [
        { value: 'Education', label: 'Education' },
        { value: 'Experience', label: 'Experience' },
        { value: 'Projects', label: 'Projects' },
        { value: 'Skills', label: 'Skills' },
        { value: 'Other', label: 'Other' }, 
    ];


    const handleFileChange = (e) => {
        const file = e.target.files[0];
        setFormData((prevState) => ({
            ...prevState,
            file: file,
        }));
    };


    const handleSectionChange = (selectedOptions) => {
        const sections = selectedOptions ? selectedOptions.map(option => option.value) : [];
        setFormData((prevState) => ({
            ...prevState,
            sections: sections,
        }));
    };

    
    const handleInputChange = (e) => {
        const { name, value } = e.target;
        setFormData((prevState) => ({
            ...prevState,
            [name]: value,
        }));
    };

    
    const handleSubmit = async (e) => {
        e.preventDefault();

        setIsUploading(true);

        const data = new FormData();
        data.append('file', formData.file);
        data.append('jobDesc', formData.jobDesc);
        data.append('sections', JSON.stringify(formData.sections));
        data.append('otherSection', formData.otherSection);

        try {
            const response = await fetch('http://localhost:5000/upload', {
                method: 'POST',
                body: data,
            });

            const result = await response.json();
            if (response.ok) {
                onUploadComplete(result);
            }
            console.log('Server Response', result);
        }
        catch (error) {
            console.error('Error uploading data:', error)
        }
        finally {
            setIsUploading(false);
        }

    };

    return (
        <form onSubmit={handleSubmit}>
            <div>
                <label htmlFor="file">Upload Resume(.pdf/.docx):</label>
                <input
                    type="file"
                    name="file"
                    onChange={handleFileChange}
                    accept=".pdf,.docx"
                    required
                />
            </div>
            <div>
                <label htmlFor="jobDesc">Job Description:</label>
                <textarea
                    name="jobDesc"
                    value={formData.jobDesc}
                    onChange={handleInputChange}
                    placeholder="Enter the job description"
                    required
                />
            </div>
            <div>
                <label htmlFor="sections">Sections to Include in Resume:</label>
                <Select
                    isMulti
                    options={options}
                    value={options.filter((option) =>
                        formData.sections.includes(option.value)
                    )}
                    onChange={handleSectionChange}
                    placeholder="Select sections"
                    styles={{
                        option: (provided) => ({
                            ...provided,
                            color: "black", 
                        }),
                        singleValue: (provided) => ({
                            ...provided,
                            color: "black",
                        }),
                        multiValueLabel: (provided) => ({
                            ...provided,
                            color: "black", 
                        }),
                    }}
                    required
                />
            </div>
            {formData.sections.includes("Other") && (
                <div>
                    <label htmlFor="otherSection">Please specify "Other":</label>
                    <input
                        type="text"
                        name="otherSection"
                        required
                        value={formData.otherSection}
                        onChange={handleInputChange}
                        placeholder="Enter your section"
                    />
                </div>
            )}
            <button type="submit">Submit</button>
            {isUploading && (
                <div className="spinner-container">
                    <div className="spinner"></div>
                    <div>This may take a minute</div>
                </div>)}
        </form>
    );
};

export default FileUploadForm;
